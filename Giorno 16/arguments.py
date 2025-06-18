import argparse
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)


def genera_testo(prompt, temperature=0.7, max_tokens=300, model="gpt-4.1-nano"):
    """Funzione per chiedere a OpenAI di generare una risposta"""
    completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        max_tokens=max_tokens,
        temperature=temperature,
    )
    return completion.choices[0].message.content


parser = argparse.ArgumentParser(description="Genera testo con OpenAI")
parser.add_argument("prompt", help="Il prompt da inviare")
parser.add_argument("--output", help="File di output per salvare la risposta")
parser.add_argument("--tokens", type=int, default=100, help="Numero massimo di token")
args = parser.parse_args()
risposta = genera_testo(args.prompt, max_tokens=args.tokens)
if args.output:
    with open(args.output, "w") as f:
        f.write(risposta)
else:
    print(risposta)
