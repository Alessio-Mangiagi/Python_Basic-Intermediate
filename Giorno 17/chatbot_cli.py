import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

messages = [
    {"role": "system", "content": "Sei un assistente gentile."}
]

while True:
    user_input = input("Utente: ")
    messages.append({"role": "user", "content": user_input})
    try:
        response = openai.resources.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=150
        )
        reply = response.choices[0].message.content
        print("Assistant:", reply)
        messages.append({"role": "assistant", "content": reply})
    except openai.OpenAIError as e:
        print("Errore API:", e)