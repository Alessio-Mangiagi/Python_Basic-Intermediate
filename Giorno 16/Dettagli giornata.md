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
2. Impostazione della API Key tramite variabile.
3. Creazione della prima richiesta `openai.chat.completions.create`.
4. Specificare il modello (es. `gpt-3.5-turbo`).
5. Definire il prompt base.
6. Impostare il parametro `max_tokens`.
7. Controllare il parametro `temperature`.
8. Ricevere e stampare la risposta.
9. Gestire errori comuni delle API.
10. Creare una funzione riutilizzabile.
11. Logging delle risposte.
12. Gestire limiti di quota e rate limiting.
13. Prova di prompt differenti.
14. Salvare il risultato in un file.
15. Integrare la funzione in un semplice script CLI.