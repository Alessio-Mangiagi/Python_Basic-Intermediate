# Chatbot Django App

Un'applicazione Django completa con interfaccia web e API REST per un chatbot basato su OpenAI.

## Struttura del Progetto

```
esempi_django/
├── chatbot_project/          # Configurazione principale Django
├── chatbot_api/             # App per le API REST
├── chatbot_web/             # App per l'interfaccia web
├── .env                     # Variabili d'ambiente
├── requirements.txt         # Dipendenze Python
└── manage.py               # Script di gestione Django
```

## Caratteristiche

### API Backend (chatbot_api)

-   **POST /api/chat/**: Endpoint per inviare messaggi al chatbot
-   **GET /api/health/**: Health check dell'API
-   **GET /api/history/**: Cronologia delle chat
-   Integrazione con OpenAI GPT-4.1-nano (aggiornato dal CLI originale)
-   Gestione delle sessioni di chat
-   Salvataggio messaggi nel database
-   **Codice completamente commentato per scopi didattici**

### Interfaccia Web (chatbot_web)

-   Interfaccia grafica moderna e responsive
-   Chat in tempo reale
-   Gestione degli errori
-   Design moderno con gradients e animazioni

## Setup e Installazione

### 1. Configurazione dell'ambiente

```bash
# Installa le dipendenze
pip install -r requirements.txt
```

### 2. Configurazione delle variabili d'ambiente

Modifica il file `.env`:

```env
OPENAI_API_KEY=your_actual_openai_api_key_here
DEBUG=True
SECRET_KEY=your-secret-key-here
```

### 3. Setup del database

```bash
# Applica le migrazioni
python manage.py migrate

# (Opzionale) Crea un superuser per l'admin
python manage.py createsuperuser
```

### 4. Avvio del server

```bash
python manage.py runserver
```

## Utilizzo

### Interfaccia Web

-   Vai su `http://localhost:8000/` per accedere all'interfaccia chat
-   Digita un messaggio e premi Invio o clicca "Invia"
-   Il chatbot risponderà utilizzando l'API OpenAI

### API Endpoints

#### Chat Endpoint

```bash
POST /api/chat/
Content-Type: application/json

{
    "message": "Ciao, come stai?",
    "session_id": "optional_session_id"
}
```

Risposta:

```json
{
    "response": "Ciao! Sto bene, grazie. Come posso aiutarti?",
    "session_id": "session_123",
    "success": true
}
```

#### Health Check

```bash
GET /api/health/
```

#### Cronologia Chat

```bash
GET /api/history/
```

## Struttura del Codice

### Models (chatbot_api/models.py)

-   `ChatMessage`: Memorizza i messaggi di chat
-   `ChatSession`: Gestisce le sessioni di chat

### Services (chatbot_api/services.py)

-   `ChatbotService`: Gestisce l'integrazione con OpenAI
-   Ispirato al codice CLI originale
-   Gestione degli errori e logging

### Views (chatbot_api/views.py)

-   API endpoints utilizzando Django REST Framework
-   Validazione dei dati con serializers
-   Gestione degli errori

### Frontend (chatbot_web/templates/)

-   Interfaccia chat responsive
-   JavaScript per comunicazione con l'API
-   Design moderno con CSS

## Personalizzazione

### Modifica del modello AI

Nel file `chatbot_api/services.py`, cambia il modello:

```python
model="gpt-4"  # invece di gpt-4.1-nano
```

### Personalizza il prompt di sistema

Nel file `chatbot_api/services.py`:

```python
self.default_messages = [
    {"role": "system", "content": "Il tuo prompt personalizzato qui"}
]
```

### Styling dell'interfaccia

Modifica il CSS nel template `chatbot_web/templates/chatbot_web/chat.html`

## Note Tecniche

-   Basato su Django 5.2.3
-   Utilizza Django REST Framework per le API
-   CORS abilitato per lo sviluppo
-   Database SQLite (di default)
-   Supporto per sessioni di chat multiple
-   Gestione degli errori dell'API OpenAI

## Sicurezza

-   Non committare mai il file `.env` con le chiavi API reali
-   In produzione, usa un database più robusto (PostgreSQL)
-   Configura `ALLOWED_HOSTS` per la produzione
-   Usa HTTPS in produzione

## 📚 Documentazione Didattica

### Per Studenti

Questo progetto include **codice completamente commentato** per scopi didattici:

-   **`GUIDA_COMPLETA_STUDENTI.md`**: Spiegazione dettagliata di tutta l'architettura
-   **Commenti riga per riga** in tutti i file Python
-   **Flusso di dati documentato** step-by-step
-   **Configurazione debug** per VS Code
-   **Best practices** e concetti Django spiegati

### File Commentati

-   `chatbot_api/models.py`: Modelli database con spiegazioni dettagliate
-   `chatbot_api/serializers.py`: Conversione dati JSON ↔ Python
-   `chatbot_api/services.py`: Logica business e integrazione OpenAI
-   `chatbot_api/views.py`: Endpoint API REST
-   `chatbot_web/templates/chat.html`: Frontend JavaScript e CSS

### Come Studiare il Codice

1. **Inizia dalla guida**: Leggi `GUIDA_COMPLETA_STUDENTI.md`
2. **Segui il flusso**: Utente → Frontend → API → OpenAI → Database
3. **Usa il debugger**: Metti breakpoint e osserva l'esecuzione
4. **Sperimenta**: Modifica il codice e osserva i risultati
