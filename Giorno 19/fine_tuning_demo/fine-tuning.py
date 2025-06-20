import openai
import os

MODEL_NAME = "ft:gpt-4.1-nano:personalizzato-2025-06-20-12-00-00"
SYSTEM_PROMPT = "Sei un assistente gentile."

openai.api_key = os.getenv("OPENAI_API_KEY")

def main():
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]
    print("Chatbot avviato. Scrivi 'esci' per terminare.\n")
    while True:
        user_input = input("Utente: ").strip()
        if user_input.lower() in ("esci", "exit", "quit"): 
            print("Assistant: Arrivederci!")
            break
        if not user_input:
            continue
        messages.append({"role": "user", "content": user_input})
        try:
            response = openai.chat.completions.create(
                model=MODEL_NAME,
                messages=messages,
                max_tokens=150
            )
            reply = response.choices[0].message.content.strip()
            print("Assistant:", reply)
            messages.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"[ERRORE] {e}")
            continue

if __name__ == "__main__":
    main()
