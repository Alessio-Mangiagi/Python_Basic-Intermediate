### Giorno 18
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