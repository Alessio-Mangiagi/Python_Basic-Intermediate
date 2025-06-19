# Importa la libreria OpenAI per interagire con le API
import openai

# Importa NumPy per operazioni su array numerici
import numpy as np

# Importa os per accedere alle variabili d'ambiente
import os

# Importa la funzione per calcolare la similarità coseno da scikit-learn
from sklearn.metrics.pairwise import cosine_similarity

# Importa la funzione per normalizzare i vettori da scikit-learn
from sklearn.preprocessing import normalize

# Inizializza il client OpenAI usando la chiave API dalle variabili d'ambiente
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def search_similarity(embedding, embeddings):
    """
    Calcola la similarità coseno tra un embedding e una lista di embeddings.
    """
    # Calcola la similarità coseno tra un singolo embedding e una lista di embeddings
    # [embedding] trasforma il singolo embedding in una lista per compatibilità con cosine_similarity
    # [0] estrae il primo (e unico) array di risultati
    similarities = cosine_similarity([embedding], embeddings)[0]
    return similarities


def search_similarity_and_return_best(embedding, embeddings, texts):
    """
    Calcola la similarità coseno tra un embedding e una lista di embeddings,
    e restituisce il testo con la massima similarità.
    """
    # Richiama la funzione precedente per calcolare le similarità
    similarities = search_similarity(embedding, embeddings)
    # Trova l'indice dell'elemento con la massima similarità
    best_index = np.argmax(similarities)
    # Restituisce il testo corrispondente e la sua similarità
    return texts[best_index], similarities[best_index]


def search_similarity_and_return_best_with_threshold(
    embedding, embeddings, texts, threshold=0.7
):
    """
    Calcola la similarità coseno tra un embedding e una lista di embeddings,
    e restituisce il testo con la massima similarità se supera una soglia.
    """
    # Calcola le similarità usando la funzione base
    similarities = search_similarity(embedding, embeddings)
    # Trova l'indice dell'elemento con la massima similarità
    best_index = np.argmax(similarities)
    # Estrae il valore della massima similarità
    best_similarity = similarities[best_index]

    # Verifica se la similarità supera la soglia minima
    if best_similarity >= threshold:
        # Se supera la soglia, restituisce testo e similarità
        return texts[best_index], best_similarity
    else:
        # Se non supera la soglia, restituisce None per entrambi i valori
        return None, None


def search_similarity_and_return_top_n(embedding, embeddings, texts, n=3):
    """
    Calcola la similarità coseno tra un embedding e una lista di embeddings,
    e restituisce i primi n testi con le massime similarità.
    """
    # Calcola le similarità coseno tra l'embedding input e tutti gli embeddings
    similarities = search_similarity(embedding, embeddings)

    # Trova gli indici dei top n elementi con maggiore similarità
    # np.argsort ordina dal più piccolo al più grande, quindi prendiamo gli ultimi n elementi
    # [::-1] inverte l'ordine per avere dal più grande al più piccolo
    top_indices = np.argsort(similarities)[-n:][::-1]

    # Restituisce una lista di tuple (testo, similarità) per i top n risultati
    return [(texts[i], similarities[i]) for i in top_indices]


def cosine_sim_normalized(vec1, vec2):
    # Calcola il prodotto scalare tra due vettori normalizzati
    # (equivale alla similarità coseno se i vettori sono già normalizzati)
    return np.dot(vec1, vec2)


def cosine_sim_normalized_array(vec1, vec2_list):
    """
    Calcola la similarità coseno tra un vettore e una lista di vettori normalizzati.
    """
    # Calcola il prodotto scalare tra vec1 e ogni vettore in vec2_list
    return [np.dot(vec1, vec2) for vec2 in vec2_list]


# Lista di frasi di esempio per il confronto
frasi = [
    "Questa è una frase.",
    "Questa è un'altra frase.",
    "la pizza è buona",
    "la pasta è buona",
    "Questa macchina è veloce",
    "Questa macchina è lenta",
]

# Crea gli embeddings per tutte le frasi usando il modello text-embedding-3-small
response = client.embeddings.create(model="text-embedding-3-small", input=frasi)
# Estrae solo i vettori embedding dalla risposta dell'API
embeddings = [e.embedding for e in response.data]
# print(np.array(embeddings))  # Riga commentata per debug

# Chiede all'utente di inserire una frase per il confronto
risposta = input("Inserisci una frase per il confronto: ")

# Crea l'embedding per la frase inserita dall'utente
embedding_1 = (
    client.embeddings.create(
        model="text-embedding-3-small",
        input=[risposta],
    )
    .data[0]  # Prende il primo elemento della risposta
    .embedding  # Estrae il vettore embedding
)

# Normalizza l'embedding dell'input utente
# reshape(1, -1) trasforma il vettore in una matrice 1xN per compatibilità
embedding_1_norm = normalize(np.array(embedding_1).reshape(1, -1))

# Normalizza tutti gli embeddings delle frasi di riferimento
# reshape crea una matrice dove ogni riga è un embedding
embeddings_norm = normalize(np.array(embeddings).reshape(len(embeddings), -1))

# Calcola la similarità usando vettori normalizzati
similarity = cosine_sim_normalized_array(embedding_1_norm, embeddings_norm)
print("Similarità coseno tra l'input e gli embeddings normalizzati:")
# Itera attraverso i risultati di similarità
for i, sim in enumerate(similarity):
    sim2 = round(sim[0], 3)  # Arrotonda a 3 decimali (sim[0] perché sim è un array)
    perc = sim2 * 100  # Converte in percentuale
    print(f"Frase {i + 1}: {perc}% → {frasi[i]}")

# Calcola la similarità usando la funzione standard (senza normalizzazione manuale)
similarity = search_similarity(embedding_1, embeddings)
print("Similarità coseno tra l'input e gli embeddings:")
# Itera attraverso i risultati
for i, sim in enumerate(similarity):
    sim2 = round(sim, 3)  # Arrotonda a 3 decimali
    perc = sim2 * 100  # Converte in percentuale
    print(f"Frase {i + 1}: {perc}% → {frasi[i]}")

# Trova la frase più simile usando la funzione dedicata
best_text, best_similarity = search_similarity_and_return_best(
    embedding_1, embeddings, frasi
)

# Trova i top 3 risultati più simili
top_n_results = search_similarity_and_return_top_n(embedding_1, embeddings, frasi, n=3)
print("\nTop 3 risultati:")
# Stampa i risultati ordinati per similarità
for i, (text, sim) in enumerate(top_n_results):
    sim2 = round(sim, 3)  # Arrotonda a 3 decimali
    perc = sim2 * 100  # Converte in percentuale
    print(f"{i + 1}. {perc}% → {text}")

# Stampa il risultato finale con la frase più simile
print(
    f"\nLa frase più simile è: '{best_text}' con una similarità di {best_similarity:.4f}"
)
