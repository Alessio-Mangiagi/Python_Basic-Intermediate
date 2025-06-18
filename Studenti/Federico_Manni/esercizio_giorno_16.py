from openai import OpenAI
from dotenv import load_dotenv
import os

#! realizziamo un app dove chiediamo al utente di scrivere una frase e faremo un controllo ortografico e la correggeremo
#! per lui ritornando la frase corretta



load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)

richiesta = input("Scrivi una frase da correggere: ")

response = client.chat.completions.create(
    model="gpt-4.1-nano",
    messages=[
        {"role": "user", "content": f"Correggi questa frase: '{richiesta}'"}
    ]
    )

print(response.choices[0].message.content)