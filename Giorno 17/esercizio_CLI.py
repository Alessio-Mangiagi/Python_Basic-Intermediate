import argparse
from openai import OpenAI
from dotenv import load_dotenv
import numpy as np
import os
from sklearn.metrics.pairwise import cosine_similarity
from PyPDF2 import PdfReader

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def main():
    parser = argparse.ArgumentParser(description="Ricerca semantica di frasi")
    parser.add_argument("query", type=str, help="La frase da cercare")
    parser.add_argument(
        "--top", type=int, default=3, help="Numero di risultati da restituire"
    )
    parser.add_argument(
        "--dataset", type=str, default="frasi-txt", help="File del dataset"
    )

    args = parser.parse_args()

    # Carica il dataset
    dataset = load_dataset(args.dataset)
    embeddings = call_openai(dataset)
    embeddings_query = call_openai(args.query)

    top_n_results = search_similarity_and_return_top_n(
        embeddings_query, embeddings, dataset, n=int(args.top)
    )
    print("\nTop 3 risultati:")
    print_top_n_results(top_n_results)


# Stampa i risultati ordinati per similarità


def print_top_n_results(results):
    for i, (text, sim) in enumerate(results):
        sim2 = round(sim, 3)  # Arrotonda a 3 decimali
        perc = sim2 * 100  # Converte in percentuale
        print(f"{i + 1}. {perc}% → {text}")


def load_dataset(file_path):
    # Controlla se il file ha estensione .pdf
    if file_path.endswith(".pdf"):
        # Se è un PDF, chiama la funzione specifica per caricare PDF
        return load_pdf(file_path)
    # Controlla se il file ha estensione .txt
    elif file_path.endswith(".txt"):
        # Apre il file di testo in modalità lettura con codifica UTF-8
        with open(file_path, "r", encoding="utf-8") as f:
            # Legge tutte le righe, rimuove spazi/caratteri di fine riga e restituisce una lista
            return [line.strip() for line in f.readlines()]


def load_pdf(file_path):
    # Crea un oggetto reader per leggere il file PDF
    reader = PdfReader(file_path)
    # Inizializza una stringa vuota per contenere tutto il testo estratto
    text = ""
    # Itera attraverso tutte le pagine del PDF
    for page in reader.pages:
        # Estrae il testo dalla pagina corrente e lo aggiunge alla stringa totale
        text += page.extract_text() + " "

    # Suddividi il testo in chunks da 400 caratteri
    # Inizializza una lista vuota per contenere i chunks di testo
    chunks = []
    # Itera attraverso il testo con step di 400 caratteri
    for i in range(0, len(text), 400):
        # Estrae un chunk di 400 caratteri a partire dalla posizione i
        chunk = text[i : i + 400].strip()
        # Verifica che il chunk non sia vuoto
        if chunk:  # Aggiungi solo chunks non vuoti
            # Aggiunge il chunk alla lista dei chunks
            chunks.append(chunk)

    # Restituisce la lista di tutti i chunks
    return chunks


def semantic_search(embedding, embeddings):
    similarities = cosine_similarity(embedding, embeddings)[0]
    return similarities


def search_similarity_and_return_top_n(embedding, embeddings, texts, n=3):
    similarities = semantic_search(embedding, embeddings)
    top_indices = np.argsort(similarities)[-n:][::-1]
    return [(texts[i], similarities[i]) for i in top_indices]


def call_openai(text):
    response = client.embeddings.create(model="text-embedding-3-small", input=text)
    return [e.embedding for e in response.data]


if __name__ == "__main__":
    main()
