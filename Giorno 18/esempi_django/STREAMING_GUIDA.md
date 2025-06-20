# 📡 STREAMING CHAT - GUIDA TECNICA

## 🎯 Cos'è lo Streaming

Lo **streaming** permette di ricevere la risposta del chatbot **pezzo per pezzo** in tempo reale, invece di aspettare la risposta completa. È simile a come ChatGPT mostra le risposte mentre vengono generate.

---

## 🔧 Come Funziona il Codice

### 1. **Frontend - Interfaccia Utente**

Nel file `chatbot_web/templates/chatbot_web/chat.html`:

```html
<!-- Checkbox per attivare lo streaming -->
<label class="streaming-toggle">
    <input type="checkbox" id="streamingCheckbox" />
    <span class="streaming-label">📡 Streaming</span>
</label>
```

**JavaScript aggiornato:**

```javascript
// Controlla se lo streaming è attivato
const isStreaming = streamingCheckbox.checked;

// Invia il parametro streaming nella richiesta
body: JSON.stringify({
    message: message,
    session_id: sessionId,
    streaming: isStreaming,  // ← Nuovo parametro
}),
```

### 2. **Serializer - Validazione Dati**

Nel file `chatbot_api/serializers.py`:

```python
class ChatRequestSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=1000)
    session_id = serializers.CharField(max_length=100, required=False)

    # ← NUOVO: Campo per attivare streaming
    streaming = serializers.BooleanField(required=False, default=False)

class ChatResponseSerializer(serializers.Serializer):
    response = serializers.CharField()
    session_id = serializers.CharField()
    success = serializers.BooleanField()

    # ← NUOVI: Campi per gestire streaming
    is_streaming = serializers.BooleanField(default=False)
    is_final = serializers.BooleanField(default=True)
    error = serializers.CharField(required=False)
```

### 3. **Views - Endpoint API**

Nel file `chatbot_api/views.py`:

```python
def chat_endpoint(request):
    # Estrae il parametro streaming dalla richiesta
    streaming = serializer.validated_data.get("streaming", False)

    # Passa il parametro al servizio chatbot
    result = chatbot_service.chat(user_message, session_id, streaming)
```

### 4. **Service - Logica Business**

Nel file `chatbot_api/services.py`:

```python
def chat(self, user_message: str, session_id: str = None, streaming: bool = False):
    """
    Metodo principale che decide tra streaming e normale
    """
    # Prepara i messaggi per OpenAI
    messages.append({"role": "user", "content": user_message})

    # Decide quale metodo usare
    if streaming:
        return self._chat_with_streaming(messages, user_message, session_id)
    else:
        return self._chat_normal(messages, user_message, session_id)

def _chat_normal(self, messages, user_message, session_id):
    """
    Chat normale - risposta completa in una volta
    """
    response = openai.chat.completions.create(
        model="gpt-4.1-nano",
        messages=messages,
        max_tokens=150,
        stream=False,  # ← NO streaming
    )

    return {
        "response": response.choices[0].message.content,
        "is_streaming": False,
        "is_final": True,
    }

def _chat_with_streaming(self, messages, user_message, session_id):
    """
    Chat con streaming - risposta pezzo per pezzo
    """
    response_stream = openai.chat.completions.create(
        model="gpt-4.1-nano",
        messages=messages,
        max_tokens=150,
        stream=True,  # ← SÌ streaming
    )

    # Raccoglie tutti i pezzi
    complete_response = ""
    for chunk in response_stream:
        if chunk.choices[0].delta.content is not None:
            complete_response += chunk.choices[0].delta.content

    return {
        "response": complete_response,
        "is_streaming": True,
        "is_final": True,
    }
```

---

## 🚀 Implementazione Attuale vs Avanzata

### **Implementazione Attuale (Semplificata)**

-   ✅ **Funziona**: OpenAI streaming è attivato
-   ✅ **Raccoglie**: Tutti i chunk vengono assemblati
-   ✅ **Salva**: Risposta completa nel database
-   ❓ **Limitazione**: Ritorna solo la risposta finale

### **Implementazione Avanzata (Futura)**

Per un vero streaming real-time, dovresti:

1. **WebSockets** invece di HTTP normale
2. **Server-Sent Events (SSE)** per streaming HTTP
3. **Chunked Response** per inviare pezzi uno per volta

---

## 🔍 Come Testare

### **Test 1: Modalità Normale**

1. Lascia il checkbox "Streaming" **NON** selezionato
2. Invia un messaggio
3. Vedi: "L'assistente sta pensando..."
4. Ricevi: Risposta completa

### **Test 2: Modalità Streaming**

1. Seleziona il checkbox "📡 Streaming"
2. Invia un messaggio
3. Vedi: "📡 Streaming in corso..."
4. Ricevi: Risposta con icona 🔄

### **Debug Points:**

-   `chatbot_api/views.py:42` → Controlla valore `streaming`
-   `chatbot_api/services.py:95` → Vedi quale metodo viene chiamato
-   `chatbot_api/services.py:175` → Debug del loop streaming

---

## 📊 Flusso Dati Streaming

```
1. UTENTE seleziona checkbox streaming ✅
   ↓
2. FRONTEND invia streaming=true
   ↓
3. VIEWS estrae parametro streaming
   ↓
4. SERVICE sceglie _chat_with_streaming()
   ↓
5. OPENAI API chiamata con stream=True
   ↓
6. CHUNK loop assembla risposta completa
   ↓
7. DATABASE salva risposta completa
   ↓
8. FRONTEND riceve risposta con is_streaming=true
   ↓
9. UI mostra risposta con icona 🔄
```

---

## 💡 Miglioramenti Futuri

### **1. Real-time Streaming**

```python
# views.py - con Django Channels (WebSockets)
async def stream_chat(websocket):
    async for chunk in openai_stream:
        await websocket.send_text(chunk)
```

### **2. Server-Sent Events**

```python
# views.py - con SSE
def chat_stream(request):
    def event_stream():
        for chunk in openai_stream:
            yield f"data: {chunk}\n\n"

    return StreamingHttpResponse(event_stream(),
                                content_type='text/event-stream')
```

### **3. Progress Indicator**

```javascript
// Frontend con progress bar
let currentMessage = "";
eventSource.onmessage = function (event) {
    currentMessage += event.data;
    updateMessageInRealTime(currentMessage);
};
```

---

## 🎓 Concetti Appresi

### **Backend:**

-   ✅ **Parameter Validation**: Aggiungere nuovi campi ai serializers
-   ✅ **Method Routing**: Decisioni condizionali nei services
-   ✅ **OpenAI Streaming**: Usare `stream=True` e iterare chunks
-   ✅ **Error Handling**: Gestire errori in modalità diverse

### **Frontend:**

-   ✅ **Form Controls**: Checkbox e gestione stato
-   ✅ **Conditional UI**: Cambiare testo loading basato su modalità
-   ✅ **API Communication**: Inviare parametri aggiuntivi

### **Architecture:**

-   ✅ **Feature Flags**: Attivare/disattivare funzionalità
-   ✅ **Backwards Compatibility**: Nuove feature senza rompere esistenti
-   ✅ **Code Organization**: Separare logiche diverse in metodi separati

---

## 🔐 Note di Sicurezza

⚠️ **Streaming e Rate Limiting:**

-   Lo streaming può consumare più risorse
-   Considera limitazioni per utente
-   Monitora uso token OpenAI

⚠️ **Timeout Handling:**

-   Stream possono essere più lunghi
-   Configura timeout appropriati
-   Gestisci disconnessioni client

---

**🎯 Obiettivo Didattico:**  
Capire come aggiungere nuove funzionalità a un'applicazione esistente mantenendo la compatibilità e seguendo le best practices! 🚀
