# Implementazione del Streaming OpenAI - Documentazione Tecnica

## 🚀 Cosa è stato implementato

### 1. Vero Streaming OpenAI

-   **Backend**: Implementato il vero streaming con `stream=True` nell'API OpenAI
-   **Frontend**: Aggiunta gestione del streaming progressivo con Server-Sent Events (SSE)
-   **Aumento Token**: Incrementato `max_tokens` da 150 a 1000 per risposte più complete

### 2. Due modalità di funzionamento

#### Modalità Normale (Default)

-   Checkbox "Streaming" **NON** selezionata
-   Una singola richiesta HTTP che aspetta la risposta completa
-   Endpoint: `/api/chat/`
-   L'utente vede l'indicatore di caricamento finché la risposta non è pronta

#### Modalità Streaming

-   Checkbox "Streaming" **selezionata**
-   La risposta arriva in tempo reale, parola dopo parola
-   Endpoint: `/api/chat/stream/`
-   L'utente vede la risposta mentre viene generata

## 🔧 Dettagli Tecnici

### Backend (Django + DRF)

#### Nuovo Endpoint: `/api/chat/stream/`

```python
@api_view(["POST"])
def chat_stream_endpoint(request):
    # Valida i dati in input
    # Configura OpenAI con stream=True
    # Utilizza StreamingHttpResponse per Server-Sent Events
    # Invia chunk in tempo reale al frontend
```

#### Formato dei messaggi SSE:

```javascript
// Inizio streaming
data: {"type": "start", "session_id": "session_123"}

// Chunk di testo
data: {"type": "chunk", "content": "Ciao"}
data: {"type": "chunk", "content": " come"}
data: {"type": "chunk", "content": " stai"}

// Fine streaming
data: {"type": "end", "complete_response": "Ciao come stai?"}

// In caso di errore
data: {"type": "error", "error": "Messaggio di errore"}
```

### Frontend (HTML + JavaScript)

#### Gestione dello Streaming

```javascript
function handleStreamingResponse(message) {
    // Usa fetch() per inviare la richiesta
    // Legge lo stream con response.body.getReader()
    // Aggiorna il messaggio in tempo reale
    // Gestisce start, chunk, end, error
}
```

#### Gestione Normale

```javascript
function handleNormalResponse(message) {
    // Usa fetch() standard
    // Aspetta la risposta completa
    // Mostra tutto il messaggio in una volta
}
```

## 📁 File Modificati

### 1. `chatbot_api/services.py`

-   ✅ Aumentato `max_tokens` da 150 a 1000 (normale e streaming)
-   ✅ Metodi `_chat_normal()` e `_chat_with_streaming()` funzionanti

### 2. `chatbot_api/views.py`

-   ✅ Aggiunto `chat_stream_endpoint()` per Server-Sent Events
-   ✅ Gestione proper dei chunk OpenAI
-   ✅ Headers corretti per SSE

### 3. `chatbot_api/urls.py`

-   ✅ Aggiunto `path("chat/stream/", views.chat_stream_endpoint)`

### 4. `chatbot_web/templates/chatbot_web/chat.html`

-   ✅ Rimossa emoji 🔄 durante lo streaming
-   ✅ Aggiunta `handleStreamingResponse()` per SSE
-   ✅ Aggiunta `handleNormalResponse()` per chiamate normali
-   ✅ Selezione automatica modalità basata su checkbox

## 🎯 Come Funziona per l'Utente

### Modalità Normale

1. L'utente scrive un messaggio
2. Clicca "Invia" (checkbox streaming vuota)
3. Vede "L'assistente sta pensando..."
4. Dopo qualche secondo appare la risposta completa

### Modalità Streaming

1. L'utente seleziona la checkbox "📡 Streaming"
2. Scrive un messaggio e clicca "Invia"
3. Vede "📡 Streaming in corso..."
4. La risposta appare progressivamente, parola dopo parola
5. Come se l'assistente stesse scrivendo in tempo reale

## 🔍 Differenze Tecniche

| Aspetto        | Normale               | Streaming            |
| -------------- | --------------------- | -------------------- |
| **API OpenAI** | `stream=False`        | `stream=True`        |
| **Endpoint**   | `/api/chat/`          | `/api/chat/stream/`  |
| **Protocollo** | HTTP Request/Response | Server-Sent Events   |
| **Frontend**   | `fetch().then()`      | `ReadableStream`     |
| **UX**         | Risposta istantanea   | Risposta progressiva |
| **Token Max**  | 1000                  | 1000                 |

## 🧪 Test e Debug

### Test Manuale

1. Apri http://127.0.0.1:8000/
2. Prova entrambe le modalità (checkbox on/off)
3. Verifica che lo streaming mostri il testo progressivamente
4. Verifica che la modalità normale mostri tutto insieme

### Debug Backend

```python
# In views.py - aggiungi logging
import logging
logger = logging.getLogger(__name__)

# Per vedere i chunk in arrivo:
logger.info(f"Chunk ricevuto: {chunk_content}")
```

### Debug Frontend

```javascript
// Nel browser, F12 -> Console
console.log("Chunk ricevuto:", data);
```

## 📚 Concetti Didattici Spiegati

### Server-Sent Events (SSE)

-   **Cosa sono**: Tecnologia HTML5 per streaming unidirezionale dal server
-   **Vantaggi**: Più semplice di WebSocket, perfetto per streaming di testo
-   **Headers necessari**: `text/event-stream`, `Cache-Control: no-cache`

### ReadableStream API

-   **Cosa fa**: Legge dati in streaming dal browser
-   **Metodi**: `getReader()`, `read()`, `decode()`
-   **Asincrono**: Perfetto per dati che arrivano in tempo reale

### OpenAI Streaming

-   **stream=True**: Attiva la modalità streaming
-   **Chunks**: Piccoli pezzi di risposta che arrivano uno per volta
-   **Delta**: Contiene solo il nuovo testo aggiunto

## 🎓 Per gli Studenti

Questo progetto dimostra:

1. **Architettura RESTful**: Due endpoint per due funzionalità diverse
2. **Real-time Communication**: Streaming di dati server-to-client
3. **Progressive Enhancement**: Funzionalità che si attiva/disattiva
4. **Error Handling**: Gestione errori sia backend che frontend
5. **User Experience**: Due modalità d'uso per esigenze diverse

## 🛠 Prossimi Miglioramenti Possibili

1. **WebSocket**: Per comunicazione bidirezionale
2. **Typing Indicator**: Indicatore che mostra quando l'AI sta "scrivendo"
3. **Pause/Resume**: Possibilità di fermare/riprendere lo streaming
4. **Caratteri speciali**: Gestione di markdown, emoji, ecc.
5. **Chunking intelligente**: Interrompere solo a fine parola/frase
