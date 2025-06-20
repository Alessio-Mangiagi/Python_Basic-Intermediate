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