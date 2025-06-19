### Giorno 17
- **Teoria: Embeddings e loro utilizzo**

1. Definizione di embedding.
2. Perché gli embeddings sono utili.
3. Differenza tra embeddings e completions.
4. Cos’è lo spazio vettoriale.
5. Misura di similarità: cosine similarity.
6. Introduzione a `openai.Embedding.create()`.
7. Tipici usi: ricerca semantica.
8. Usi in classificazione di testo.
9. Usi in clustering e raggruppamento.
10. Embedding di frasi, documenti e paragrafi.
11. Limiti dimensionali e prestazionali.
12. Persistenza degli embeddings in database.
13. Librerie ausiliarie: numpy, faiss.
14. Visualizzazione di embeddings con PCA/t-SNE.
15. Considerazioni etiche sull’uso degli embeddings.

- **Pratica: Ricerca semantica di frasi e similitudini**

1. Preparazione di un dataset di frasi.
2. Creazione degli embeddings tramite `openai.resources.embeddings.create()`.
3. Conversione degli embeddings in vettori numpy.
4. Calcolo della similarità con `cosine_similarity`.
5. Funzione di ricerca semantica base.
6. Normalizzazione dei vettori.
7. Gestione batch per chiamate multiple.
8. Ordinamento dei risultati per similarità.
9. Test di frasi simili e frasi diverse.
10. Creazione di un’interfaccia CLI per ricerca.
11. Gestione dell’API Key e parametri.
12. Logging delle chiamate API.
13. Salvataggio degli embeddings su file.
14. Utilizzo di database vettoriali (es. FAISS).
15. Testing su dataset esteso.