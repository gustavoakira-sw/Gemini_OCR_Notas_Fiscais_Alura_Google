new Vue({
    el: '#app',
    data: {
        file: null,
        data: null,
        csvFileUrl: '',
        showResult: false,
        isLoading: false,
    },
    methods: {
        handleFileUpload(event) {
            this.file = event.target.files[0];
        },
        processRequest() {
            if (!this.file) {
                alert('Por favor, faça o upload de um arquivo.');
                return;
            }

            this.isLoading = true;
            const formData = new FormData();
            formData.append('file', this.file);

            axios.post('/process', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                }
            })
            .then(response => {
                this.data = JSON.stringify(response.data.data, null, 2);
                this.csvFileUrl = response.data.csv_file;
                this.showResult = true;
                this.isLoading = false;
            })
            .catch(error => {
                console.error('Erro:', error);
                alert('Ocorreu um erro ao processar sua solicitação.');
                this.isLoading = false;
            });
        }
    }
});

