from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()  




client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)




def chiamata_openai(modello="gpt-4.1-nano", message=""):
    risposta = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {"role": "user", "content": message}]
        )
    return risposta


risposta = chiamata_openai(message="Genera un numero pari tra 1 e 100")


numero_pari = int(risposta.choices[0].message.content.strip())

if numero_pari % 2 == 0:
    print(f"Il numero pari ritornato è: {numero_pari}")




print(risposta.choices[0].message.content);
