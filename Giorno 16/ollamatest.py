from ollama import chat
from ollama import ChatResponse


def ask_ollama(input, model="deepseek-r1:8b"):
    """Funzione per chiedere a Ollama di generare una risposta"""
    response: ChatResponse = chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": input,
            }
        ],
        options={
            "temperature": 0.7,
            "max_tokens": 300,  # Imposta a True se vuoi ricevere lo stream della risposta
        },
    )
    return response.message.content


print(ask_ollama("Parlami dei pianeti."))  # printa il testo della risposta
