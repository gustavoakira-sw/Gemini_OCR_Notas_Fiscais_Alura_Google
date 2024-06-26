

# Gemini AI - Assistente Financeiro

Esta é uma aplicação web projetada para ajudar os usuários a extrair informações de cupons fiscais e recibos através das capacidades de visão computacional e output JSON do modelo Gemini 1.5 PRO, da Google.

Demo do projeto encerrada.

## Funcionalidades

- Upload de imagens de cupons fiscais ou recibos.
- Análise automatizada do conteúdo dos recibos para extração de informações.
- Apresentação dos itens adquiridos, com detalhamento de quantidade e valor.
- Possibilidade de download das informações extraídas em formato CSV.

## Tecnologias Utilizadas

- Frontend:
  - HTML
  - CSS (Bootstrap)
  - JavaScript (Vue.js)
- Backend:
  - Python com Flask
  - Google Gemini 1.5 PRO

## Como executar o projeto

Para executar o projeto em sua máquina local, siga os seguintes passos:

1. Clone o repositório utilizando o Git:
`git clone https://github.com/gustavoakira-sw/Gemini_OCR_Notas_Fiscais_Alura_Google.git && cd Gemini_OCR_Notas_Fiscais_Alura_Google`
2. Configure a chave da API:
	- Opção 1: Crie um arquivo `.env` na raíz do projeto, contendo a chave `GOOGLE_AISTUDIO_API_KEY` e o valor com a API key. O conteúdo do arquivo deve ser o seguinte:
`GOOGLE_AISTUDIO_API_KEY="SUA_CHAVE_AQUI"`
	- Opção 2: Também é possível apenas renomear o arquivo `.env.example` para `.env`  e preenchê-lo com o valor da chave da API, seguindo o padrão do exemplo acima.

3. Após criar o `.env`, o projeto deve ter a seguinte estrutura:
```
.
├── .env
├── .gitignore
├── uploads
│   ├── cf3.png
│   ├── cf2.jpg
│   ├── cf1.png
│   └── cf4.jpg
├── app.py
├── requirements.txt
├── static
│   ├── styles.css
│   └── app.js
└── templates
    └── index.html
```
4. Crie um ambiente virtual do Python com `venv` e ative-o:
`python3 -m venv venv && source venv/bin/activate`
- No Windows, o ambiente pode ser ativado com `venv\Scripts\activate`

5. Instale as dependências no ambiente virtual com o comando:
`pip install -r requirements.txt`

6. Com as dependências instaladas no ambiente virtual, execute a aplicação:
`python3 app.py`
- A aplicação será iniciada no endereço `http://localhost:5000` por padrão.

## Utilização da ferramenta
1. Acesse a aplicação (http://localhost:5000) e clique no botão de escolher um arquivo ("Choose File").
2. Faça o upload de uma nota ou cupom fiscal.
	- Como exemplo, utilizamos o arquivo `./uploads/cf4.jpg`
3. Clique no botão para fazer upload da imagem ("Processar").
4. A aplicação irá retornar os itens listados no recibo, as unidades adquiridas, o valor unitário e a categoria do produto.
	- Também é possível fazer o download destes dados como um arquivo CSV.

## Screenshots
Tela inicial:

![image](https://github.com/gustavoakira-sw/Gemini_OCR_Notas_Fiscais_Alura_Google/assets/125785377/b32c2dbb-ec07-4e01-be67-0fdd8e7e1453)

Nota fiscal já inserida:

![image](https://github.com/gustavoakira-sw/Gemini_OCR_Notas_Fiscais_Alura_Google/assets/125785377/df0d3c37-c6d9-4a2e-8a0c-de6f09a8d409)

Documento sendo processado:

![image](https://github.com/gustavoakira-sw/Gemini_OCR_Notas_Fiscais_Alura_Google/assets/125785377/77deadee-e721-4985-96d1-8a029bd0ce93)

Resultados fornecidos pelo modelo de IA:

![image](https://github.com/gustavoakira-sw/Gemini_OCR_Notas_Fiscais_Alura_Google/assets/125785377/0de4a1e1-350e-44ee-ab44-cc04121e3630)

Dados em formato .CSV:
```
$ curl https://gustavoakira.tech/static/cf4.csv
Item,Un,Val,Cat
HIDRAT JOHNSONS SOFT,1,10.39,Higiene
ESPONJA BRITE 3M,1,6.29,Limpeza
CHOC KINDER OVO MENI,1,5.49,Alimentos
CHOC LEITE MM SINGLE,1,1.99,Alimentos
ESPONJA N RISCA S SC,1,6.99,Limpeza
GOMA MASCAR TRIDENT,1,1.49,Alimentos
GOMA MASCAR TRIDENT,1,1.49,Alimentos
PANO M USO S-BRITE A,1,6.99,Limpeza
```

## Autoria
Desenvolvido por: Gustavo Akira Morita Gagliardi
[Contato](mailto:gustavoakira.ti@gmail.com)

