# Esempio Didattico di Fine-Tuning con OpenAI (openai 1.87, modello gpt-4.1-nano)

Questo esercizio mostra come effettuare il fine-tuning di un modello OpenAI per creare un chatbot personalizzato usando la versione 1.87 della libreria openai e il modello gpt-4.1-nano.

## Passaggi

### 1. Prepara il dataset
- Il file `dataset_finetune.jsonl` contiene esempi di conversazione (prompt e risposte) che il modello userà per imparare.
- Puoi aggiungere altre conversazioni seguendo lo stesso formato.

### 2. Prepara il dataset per OpenAI
Apri il terminale nella cartella dove si trova il dataset e lancia:

```
openai tools fine_tunes.prepare_data -f dataset_finetune.jsonl
```

Questo comando genera un file pronto per il fine-tuning (es: `dataset_finetune_prepared.jsonl`).

### 3. Avvia il fine-tuning
Lancia il comando:

```
openai api fine_tunes.create -t "dataset_finetune_prepared.jsonl" -m "gpt-4.1-nano"
```

Annota il nome del modello fine-tuned che viene restituito (es: `ft:gpt-4.1-nano:personalizzato-2025-06-20-12-00-00`).

### 4. Modifica il chatbot
Nel file `fine-tuning.py`, sostituisci il valore della chiave `model` con il nome del tuo modello fine-tuned.

### 5. Avvia il chatbot
Assicurati di avere la variabile d'ambiente `OPENAI_API_KEY` impostata, poi esegui:

```
python chatbot_cli.py
```

Per dubbi o problemi, consulta la documentazione ufficiale OpenAI: https://platform.openai.com/docs/guides/fine-tuning
