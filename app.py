from flask import Flask, render_template, request, jsonify, send_file
from pathlib import Path
import json
import google.generativeai as genai
import PIL.Image
import csv
import os
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

# Garantir que existe uma variável chamada GOOGLE_AISTUDIO_API_KEY no arquivo .env
genai.configure(api_key=os.getenv("GOOGLE_AISTUDIO_API_KEY"))

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 0,
    "max_output_tokens": 8192,
    "response_mime_type": "application/json",
}

safety_settings = [
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
]

system_instruction = "Aja como um assistente financeiro. Você deve analisar as imagens ou arquivos enviados e extrair as informações de item, unidades e valor sempre que possível, na mesma ordem em que encontrá-los na lista. Forneça dados no formato JSON para que eu possa administrar minhas finanças e integrar as respostas com outro sistema. Não dê informações adicionais. Caso não consiga identificar um dos itens ou valores, inclua-o como NAO IDENTIFICADO (\"NI\"). Não julgue o conteúdo dos recibos dos usuários, apenas auxilie a extrair as informações e categorizá-las. Tente ao máximo incluir a categoria dos produtos. NÃO INCLUA ITENS QUE NÃO APARECEM NA IMAGEM. \n\nExemplo:\n\nPrompt: [img1.jpg] Quais os itens que comprei, quantas unidades, seus valores unitários, e suas categorias?\n\nResposta: \n[\n    {\n        \"Item\": \"Leite\",\n        \"Un\": 2,\n        \"Val\": 3.99,\n        \"Cat\": \"Alimentos\"\n    },\n    {\n        \"Item\": \"Esponja\",\n        \"Un\": 1,\n        \"Val\": 7.90,\n        \"Cat\": \"Limpeza\"\n    }\n]\n\n\nPrompt: [img2.jpg] Quais os itens que comprei, quantas unidades, seus valores unitários, e suas categorias?\nResposta:\n[\n    {\n        \"Item\": \"HIDRAT JOHNSONS SOFT\",\n        \"Un\": 1,\n        \"Val\": 10.39,\n        \"Cat\": \"Higiene\"\n    },\n    {\n        \"Item\": \"ESPONJA BRITE 3M\",\n        \"Un\": 1,\n        \"Val\": 6.29,\n        \"Cat\": \"Limpeza\"\n    }\n]\n\n"

model = genai.GenerativeModel(
    model_name="gemini-1.5-pro-latest",
    generation_config=generation_config,
    system_instruction=system_instruction,
    safety_settings=safety_settings,
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']

    # Salvar o upload localmente
    file_path = Path('./uploads') / file.filename
    file.save(str(file_path))

    # GGerar conteúdo com base na imagem
    img = PIL.Image.open(file_path)
    response = model.generate_content([system_instruction, img])

    # Parsear o JSON
    data = json.loads(response.text)
    print(data)

    # Gerar arquivo CSV
    csv_file = Path('./static') / f'{file.filename.split(".")[0]}.csv'
    with open(csv_file, 'w', newline='') as csvfile:
        fieldnames = ['Item', 'Un', 'Val', 'Cat']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow(item)

    return jsonify({'data': data, 'csv_file': str(csv_file)})

if __name__ == '__main__':
    app.run(debug=True)