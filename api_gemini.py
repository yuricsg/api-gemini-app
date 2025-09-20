import google.generativeai as genai
import os


API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    print("Erro: A variável de ambiente GOOGLE_API_KEY não está definida.")
    print("Por favor, defina-a com sua chave de API para continuar.")
    exit()

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash')

def get_gemini_response(prompt_text):
    
    try:
        response = model.generate_content(prompt_text)
        return response.text
    except Exception as e:
        return f"Ocorreu um erro: {e}"

print("Bem-vindo ao app de comunicação com Gemini!")
print("Digite sua mensagem e pressione Enter. Digite 'sair' para encerrar.")

while True:
    user_prompt = input("\nVocê: ")

    if user_prompt.lower() == 'sair':
        print("Até logo!")
        break
    
    print("Gemini: ", end="") 
    response_text = get_gemini_response(user_prompt)
    print(response_text)