import argparse
from openai import OpenAI
from dotenv import load_dotenv
import numpy as np
import os
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def main():
    parser = argparse.ArgumentParser(description="Ricerca semantica di frasi")
    parser.add_argument("query", type=str, help="La frase da cercare")
    parser.add_argument("--top", type=int, default=3, help="Numero di risultati da restituire")
    parser.add_argument("--dataset", type=str, default="frasi-txt", help="File del dataset")

    

    args = parser.parse_args()

    # Carica il dataset
    dataset = load_dataset(args.dataset)
    embeddings = call_openai(dataset)
    embeddings_query = call_openai(args.query)
   

    top_n_results = search_similarity_and_return_top_n(embeddings_query, embeddings, dataset, n=int(args.top))
    print("\nTop 3 risultati:")
    print_top_n_results(top_n_results)
# Stampa i risultati ordinati per similarità

def print_top_n_results(results):
    for i, (text, sim) in enumerate(results):
        sim2 = round(sim, 3)  # Arrotonda a 3 decimali
        perc = sim2 * 100  # Converte in percentuale
        print(f"{i + 1}. {perc}% → {text}")

def load_dataset(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]
    
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
