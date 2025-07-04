import openai
import os
import sys
import time
import logging
# Usa il modulo pubblico per le eccezioni
try:
    from openai.error import RateLimitError, AuthenticationError, OpenAIError
except ImportError:
    # Fallback per versioni diverse
    from openai._exceptions import RateLimitError, AuthenticationError, OpenAIError

# 2. Impostazione API Key tramite variabile d'ambiente o input
API_KEY = os.getenv('OPENAI_API_KEY')
# Debug: mostra se la variabile d'ambiente è stata letta (non stampa la chiave per sicurezza)
if not API_KEY:
    print("Inserisci la tua OpenAI API Key:")
    API_KEY = input().strip()
openai.api_key = API_KEY

# 11. Logging delle risposte
logging.basicConfig(filename='openai_responses.log', level=logging.INFO, format='%(asctime)s %(message)s')

def call_openai(prompt, model="gpt-4.1-nano", max_tokens=100, temperature=0.7, retries=3):
    """
    Funzione riutilizzabile per chiamare OpenAI API (nuova interfaccia >=1.0.0) con gestione errori e logging.
    """
    for attempt in range(retries):
        try:
            response = openai.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                max_tokens=max_tokens,
                temperature=temperature
            )
            text = response.choices[0].message.content.strip()
            logging.info(f"Prompt: {prompt}\nRisposta: {text}")
            return text
        except RateLimitError as e:
            print(f"[!] Rate limit raggiunto. Attendo 10 secondi e riprovo... Dettaglio: {e}")
            time.sleep(10)
        except AuthenticationError as e:
            print(f"[!] Errore di autenticazione. Controlla la tua API Key. Dettaglio: {e}")
            logging.error(f"Errore autenticazione: {e}")
            break
        except OpenAIError as e:
            print(f"[!] Errore OpenAI: {e}")
            logging.error(f"Errore OpenAI: {e}")
            break
        except Exception as e:
            print(f"[!] Errore generico: {type(e).__name__}: {e}")
            logging.error(f"Errore generico: {type(e).__name__}: {e}")
            break
    return None

def main():
    print("Prompt di esempio (puoi modificarlo):")
    prompt = input("Inserisci il prompt: ") or "Scrivi una poesia su un fiume."
    model = "gpt-4.1-nano"  # Modello economico
    max_tokens = 50   # Risposta breve per risparmiare
    temperature = 0.5  # Risposta più concisa
    print(f"[INFO] Uso modello economico: {model}, max_tokens={max_tokens}, temperature={temperature}")

    risposta = call_openai(prompt, model, max_tokens, temperature)
    if risposta:
        print("\nRisposta OpenAI:\n", risposta)
        with open("risposta_openai.txt", "w", encoding="utf-8") as f:
            f.write(risposta)
    else:
        print("Nessuna risposta ricevuta.")

if __name__ == "__main__":
    main()
