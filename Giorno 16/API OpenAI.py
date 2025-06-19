from openai import OpenAI
from dotenv import load_dotenv
import os
import logging

load_dotenv()
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("openai_api.log"),
        logging.StreamHandler(),  # Per continuare a vedere i log anche in console
    ],
)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


def ask_openai(input, temperature=0.7, max_tokens=300, model="gpt-4.1-nano"):
    """Funzione per chiedere a OpenAI di generare una risposta"""
    logging.info(
        f"Making API request with model: {model}, temperature: {temperature}, max_tokens: {max_tokens}"
    )
    logging.debug(f"Input message: {input}")

    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": input,
                }
            ],  # role può essere "system", "user" o "assistant"
            max_tokens=max_tokens,
            temperature=temperature,
        )
        logging.info("API request successful")
        return completion.choices[0].message.content
    except Exception as e:
        logging.error(f"API request failed: {str(e)}")
        raise


# print(completion.choices[0].message)
print(ask_openai("Parlami dei pianeti."))  # printa il testo della risposta
print("\n#######\n")
print(
    ask_openai(
        "Elenca i pianeti del sistema solare in ordine di distanza dal sole.",
    )
)  # printa il testo della risposta
print("\n#######\n")
print(
    ask_openai(
        "Elenca i pianeti del sistema solare in formato JSON con nome e diametro."
    )
)
