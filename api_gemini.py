import google.generativeai as genai
import os
import sys


API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    print("Erro: A variável de ambiente GOOGLE_API_KEY não está definida.")
    print("Por favor, defina-a com sua chave de API para continuar.")
    sys.exit(1)

genai.configure(api_key=API_KEY)

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
model = genai.GenerativeModel(MODEL_NAME)

def get_gemini_response(prompt_text: str) -> str:
    
    try:
        response = model.generate_content(prompt_text)
        return response.text
    except Exception as e:
        return f"Ocorreu um erro: {e}"

def main() -> None:
    print(f"Bem-vindo ao app de comunicação com Gemini (modelo: {MODEL_NAME})!")
    print("Digite sua mensagem e pressione Enter. Digite 'sair' para encerrar.")

    while True:
        try:
            user_prompt = input("\nVocê: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAté logo!")
            break

        if not user_prompt:
            print("Por favor, digite algo ou 'sair' para encerrar.")
            continue

        if user_prompt.lower() in ('sair', 'exit', 'quit'):
            print("Até logo!")
            break
        
        print("Gemini: ", end="")
        response_text = get_gemini_response(user_prompt)
        print(response_text)


if __name__ == "__main__":
    main()