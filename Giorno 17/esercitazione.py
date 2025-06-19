"""
mini_semantic_search.py
Esempio didattico: OpenAI + FAISS
Autore: … (CC-BY 4.0) – Giugno 2025
"""

# Docstring del modulo che descrive lo scopo del file: un esempio educativo
# che combina OpenAI per gli embedding e FAISS per la ricerca semantica

import numpy as np  # Libreria per operazioni matematiche su array multidimensionali
import faiss  # Facebook AI Similarity Search - libreria per ricerca di similarità vettoriale
import openai  # Libreria ufficiale OpenAI per accedere alle API (versione 1.x)
import os  # Modulo per interagire con il sistema operativo (variabili d'ambiente)
from dotenv import load_dotenv  # Carica variabili d'ambiente da file .env

load_dotenv()  # Carica automaticamente le variabili dal file .env nella directory corrente
client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)  # Inizializza il client OpenAI usando la chiave API dalle variabili d'ambiente

# 1) Dataset giocattolo -----------------------------------------------------
documents = [  # Lista di documenti di esempio per testare il sistema
    {
        "id": 0,
        "text": "Il Colosseo è uno degli anfiteatri romani più famosi.",
    },  # Documento 0: informazione storica su Roma
    {
        "id": 1,  # Documento 1: informazione culinaria sulla pizza napoletana
        "text": "La pizza napoletana tradizionale prevede pomodoro San Marzano e mozzarella di bufala.",
    },
    {
        "id": 2,  # Documento 2: informazione scientifica su Einstein
        "text": "La teoria della relatività ristretta fu pubblicata da Einstein nel 1905.",
    },
    {
        "id": 3,  # Documento 3: informazione geografica sul Vesuvio
        "text": "Il Vesuvio domina il golfo di Napoli ed è un vulcano ancora attivo.",
    },
]

# 2) Funzione di embedding ---------------------------------------------------
MODEL_NAME = "text-embedding-3-small"  # Nome del modello OpenAI per generare embedding - versione piccola ed efficiente


def embed(
    texts: list[str],
) -> np.ndarray:  # Funzione che prende una lista di stringhe e restituisce array NumPy
    """
    Restituisce un array 2-D NumPy (n_frasi × dim) con gli embedding normalizzati.
    """
    # API batch (max 2048 token per chiamata)
    response = client.embeddings.create(
        model=MODEL_NAME, input=texts
    )  # Chiama l'API OpenAI per ottenere embedding dei testi
    data = [
        d.embedding for d in response.data
    ]  # Estrae solo i vettori embedding dalla risposta dell'API
    # Normalizzazione L2 ⇒ coseno ≈ prodotto scalare
    X = np.array(
        data, dtype="float32"
    )  # Converte la lista in array NumPy con tipo float32 per efficienza
    faiss.normalize_L2(
        X
    )  # Normalizza i vettori: dopo questa operazione il coseno diventa equivalente al prodotto scalare
    return X  # Restituisce l'array di embedding normalizzati


# 3) Calcola embedding e costruisci indice -----------------------------------
corpus_texts = [
    d["text"] for d in documents
]  # Estrae solo il testo da ogni documento, ignorando gli ID
corpus_emb = embed(corpus_texts)  # Calcola gli embedding per tutti i testi del corpus

dim = corpus_emb.shape[
    1
]  # Ottiene la dimensione dei vettori embedding (seconda dimensione dell'array)
index = faiss.IndexFlatIP(
    dim
)  # Crea un indice FAISS per prodotto scalare (Inner Product) - adatto per vettori normalizzati
index.add(
    corpus_emb
)  # Aggiunge tutti i vettori embedding all'indice per renderli ricercabili

print(
    f"Indice creato: {index.ntotal} vettori di dimensione {dim}"
)  # Stampa informazioni sull'indice creato


# 4) Ricerca di esempio -------------------------------------------------------
def semantic_search(
    query: str, k: int = 3
):  # Funzione di ricerca semantica che prende una query e il numero di risultati desiderati
    q_emb = embed([query])  # Calcola l'embedding della query (array 1 × dim)
    D, I = index.search(
        q_emb, k
    )  # Esegue la ricerca: D contiene i punteggi di similarità, I gli indici dei documenti più simili
    results = [
        {"score": float(D[0, j]), **documents[I[0, j]]} for j in range(k)
    ]  # Crea lista di risultati combinando punteggi e documenti originali
    return results  # Restituisce i k documenti più simili con i loro punteggi


if (
    __name__ == "__main__"
):  # Blocco eseguito solo se il file viene lanciato direttamente (non importato)
    while True:  # Loop infinito per permettere query multiple
        q = input(
            "\nDomanda (ENTER per uscire): "
        ).strip()  # Chiede all'utente di inserire una domanda, rimuove spazi iniziali/finali
        if not q:  # Se l'input è vuoto (solo ENTER)
            break  # Esce dal loop
        for r in semantic_search(
            q, k=3
        ):  # Per ogni risultato della ricerca semantica (top 3)
            print(
                f"[{r['score']:.3f}]  {r['text']}"
            )  # Stampa il punteggio (3 decimali) e il testo del documento
