# - API OpenAI -

### Giorno 15
- **Teoria: Concetti di API REST, metodi HTTP, JSON**

1. Introduzione alle API REST: definizione e scopo.
2. Il concetto di *stateless* nelle API REST.
3. Struttura di un endpoint REST.
4. I principali metodi HTTP: GET.
5. I principali metodi HTTP: POST.
6. I principali metodi HTTP: PUT.
7. I principali metodi HTTP: DELETE.
8. Differenza tra PUT e PATCH.
9. I codici di stato HTTP (status codes): 200, 201, 400, 404, 500.
10. Autenticazione nelle API REST: token, header, OAuth.
11. Sicurezza nelle API REST: HTTPS, CORS.
12. Formato JSON: struttura base (oggetti e array).
13. Serializzazione e deserializzazione JSON.
14. Differenza tra XML e JSON.
15. Perché REST è così diffuso nelle applicazioni moderne.

- **Pratica: Chiamate base con la libreria requests**

1. Installazione della libreria `requests`.
2. Eseguire una semplice chiamata GET.
3. Parsing della risposta JSON.
4. Gestire errori con `response.status_code`.
5. Aggiungere parametri alle richieste GET.
6. Eseguire una chiamata POST con dati JSON.
7. Inviare header personalizzati.
8. Gestire autenticazione base con `requests.auth`.
9. Timeout delle richieste.
10. Retry automatici con `requests.adapters`.
11. Logging delle chiamate HTTP.
12. Scaricare file tramite API.
13. Upload di file con `requests`.
14. Gestire eccezioni di rete.
15. Creare una semplice funzione wrapper per chiamate REST.

---

### Giorno 16
- **Teoria: Installazione e configurazione del pacchetto openai, gestione delle API Key**

1. Introduzione al pacchetto `openai`.
2. Installazione tramite pip.
3. Differenza tra le versioni API.
4. Creazione di un account OpenAI.
5. Generazione della API Key.
6. Regole di sicurezza per gestire la API Key.
7. Dove NON salvare la API Key.
8. Uso di variabili d'ambiente per la API Key.
9. Configurazione locale della API Key.
10. Configurazione cloud della API Key.
11. Introduzione ai costi e ai limiti delle API OpenAI.
12. Limitazioni di utilizzo gratuite vs a pagamento.
13. Monitoring dell’uso tramite la dashboard OpenAI.
14. Aggiornamenti e versioning delle API.
15. Lettura della documentazione ufficiale OpenAI.

- **Pratica: Richiesta di un semplice completion (testuale)**

1. Importazione del pacchetto `openai`.
2. Impostazione della API Key tramite variabile d'ambiente o `openai.api_key`.
3. Creazione della prima richiesta `openai.resources.chat.completions.create`.
4. Specificare il modello (es. `gpt-3.5-turbo`).
5. Definire il prompt base come lista di messaggi (dizionario con ruolo e contenuto).
6. Impostare il parametro `max_tokens`.
7. Controllare il parametro `temperature`.
8. Ricevere e stampare la risposta (`response.choices[0].message.content`).
9. Gestire errori comuni delle API (usare try/except su `openai.OpenAIError`).
10. Creare una funzione riutilizzabile.
11. Logging delle risposte.
12. Gestire limiti di quota e rate limiting.
13. Prova di prompt differenti.
14. Salvare il risultato in un file.
15. Integrare la funzione in un semplice script CLI.

---

### Giorno 17
- **Teoria: Chat Completions vs Completion, Prompt design e temperature**

1. Differenza tra completions e chat completions.
2. Struttura dei messaggi in chat completions.
3. Ruoli: system, user, assistant.
4. Come la storia del dialogo influenza il contesto.
5. Temperature: cosa controlla realmente.
6. Temperature bassa: output deterministico.
7. Temperature alta: output creativo.
8. Uso del top_p per il nucleus sampling.
9. Prompt design: definizione chiara del contesto.
10. Esempi di prompt ben progettati.
11. Prompt chaining: concatenare più chiamate.
12. Prompt injection: rischi e attenzioni.
13. Come valutare la qualità delle risposte.
14. Limiti del contesto (token limit).
15. Quando usare completion vs chat completion.

- **Pratica: Costruzione di un chatbot CLI**

1. Creazione di uno script Python base.
2. Gestione dell’input utente da terminale.
3. Invio dell’input a `openai.resources.chat.completions.create`.
4. Costruzione del contesto iniziale (`system` prompt).
5. Memorizzazione dello storico dei messaggi (lista di dizionari con ruolo/contenuto).
6. Aggiunta di loop per conversazioni multiple.
7. Gestione degli errori delle API (`openai.OpenAIError`).
8. Gestione dell’interruzione con `KeyboardInterrupt`.
9. Logging delle conversazioni su file.
10. Aggiunta del parametro `temperature` configurabile.
11. Limite massimo di token per evitare errori.
12. Modularizzazione del codice.
13. Creazione di un file di configurazione.
14. Debug con stampa del payload inviato.
15. Testare il chatbot con prompt vari.

---

### Giorno 18
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

---

### Giorno 19
- **Teoria: File upload e fine-tuning (overview)**

1. Cos'è il fine-tuning in OpenAI.
2. Quando ha senso usare il fine-tuning.
3. Limiti e casi d'uso del fine-tuning.
4. Formato richiesto per il training file (JSONL).
5. Creazione dei prompt per fine-tuning.
6. Validazione del dataset.
7. Upload del dataset via API o CLI.
8. Creazione del job di fine-tuning.
9. Monitoraggio del job di fine-tuning.
10. Differenza tra modelli base e fine-tuned.
11. Costi e tempi per il fine-tuning.
12. Considerazioni etiche e di bias.
13. Versionamento e gestione dei modelli.
14. Testing del modello fine-tuned.
15. Limiti attuali del fine-tuning su GPT-4/3.5.

- **Pratica: Upload di un dataset di esempio e creazione di un fine-tune**

1. Preparare un dataset in formato JSONL.
2. Validare il dataset con `openai tools fine_tunes.prepare_data`.
3. Correggere eventuali errori segnalati.
4. Upload del dataset con `client.files.create()`.
5. Verifica dell’ID file caricato.
6. Creazione del job di fine-tuning via API.
7. Monitoraggio dello stato del job.
8. Gestione di job falliti o con warning.
9. Verifica del modello generato.
10. Creazione di chiamate test sul modello fine-tuned.
11. Confronto output modello base vs fine-tuned.
12. Logging degli output di test.
13. Documentazione del processo.
14. Gestione e pulizia dei file caricati.
15. Best practice per conservare i dataset.

---

### Giorno 20
- **Teoria: Buone pratiche di sicurezza e rate limiting, scalabilità di un’app basata su API**

1. Importanza della sicurezza nelle API.
2. Gestione sicura delle chiavi API.
3. Limitare accessi non autorizzati.
4. Logging sicuro: non salvare chiavi.
5. Uso di rotazione delle chiavi.
6. Implementazione di retry intelligenti.
7. Comprendere il rate limiting di OpenAI.
8. Gestione delle risposte 429.
9. Pianificare il carico nelle chiamate massive.
10. Scalabilità verticale vs orizzontale.
11. Uso di caching per risposte frequenti.
12. Separazione di front-end e back-end.
13. Monitoraggio proattivo dell’utilizzo API.
14. Budgeting dei costi di consumo API.
15. Strategie di failover e business continuity.

- **Pratica: Progetto finale: integrare l’interfaccia grafica con chiamate OpenAI (chatbot grafico)**

1. Scelta del framework GUI (es. Tkinter, PyQt).
2. Creazione della finestra principale.
3. Inserimento del campo input utente.
4. Visualizzazione delle risposte nella chat.
5. Collegamento del backend con OpenAI API.
6. Gestione asincrona delle chiamate API.
7. Gestione di errori e timeout.
8. Logging delle conversazioni su file.
9. Aggiunta di personalizzazione del prompt.
10. Inserimento di parametri modificabili (temperature, model).
11. Gestione dello storico conversazione.
12. Pulizia dell’interfaccia e UX.
13. Creazione di un file di configurazione.
14. Pacchettizzazione dell’applicazione.
15. Test finale e deploy locale.