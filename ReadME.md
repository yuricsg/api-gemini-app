# 🚀 Projeto de IA com a API do Google Gemini

Este projeto feito para a matéria de Engenharia de Software e IA é uma aplicação simples em Python para interagir com o modelo de IA do Google Gemini. A aplicação captura a entrada do usuário (prompt), envia para a API e exibe a resposta.

### **Funcionalidades**
- Envio de prompts para o modelo Gemini.
- Recebimento e exibição da resposta do modelo.

### 💻 **Tecnologias Utilizadas**
- **Linguagem:** Python
- **API:** Google Gemini (modelo `gemini-1.5-flash`)
- **Biblioteca:** `google-generativeai`

### 🔧 **Instalação e Configuração**

1.  **Instale a biblioteca necessária:**
    ```sh
    pip install google-generativeai
    ```

2.  **Obtenha sua Chave de API:**
    Acesse o [Google AI Studio](https://aistudio.google.com/) para criar sua chave de API.

3.  **Configure a Chave de API:**
    Defina a chave como uma variável de ambiente antes de executar o script.

    * **Windows (PowerShell):**
        ```sh
        $env:GOOGLE_API_KEY="SUA_CHAVE_AQUI"
        ```
    * **macOS/Linux:**
        ```sh
        export GOOGLE_API_KEY="SUA_CHAVE_AQUI"
        ```

### ▶️ **Como Executar a Aplicação**

Execute o script diretamente do terminal:

```sh
python api_gemini.py
