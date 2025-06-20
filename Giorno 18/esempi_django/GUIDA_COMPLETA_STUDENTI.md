# 📚 GUIDA COMPLETA AL CHATBOT DJANGO - COMMENTATA PER STUDENTI

## 🎯 Panoramica del Progetto

Questo progetto è un **chatbot completo** costruito con Django che include:

-   **Backend API** per comunicare con OpenAI
-   **Frontend Web** con interfaccia chat moderna
-   **Database** per salvare le conversazioni
-   **Sistema di debug** integrato con VS Code

---

## 🏗️ ARCHITETTURA DEL PROGETTO

```
esempi_django/
├── chatbot_project/     # ⚙️ CONFIGURAZIONE PRINCIPALE
│   ├── settings.py      # Impostazioni Django (database, API keys, etc.)
│   ├── urls.py          # Router URL principale
│   └── wsgi.py          # Server web
│
├── chatbot_api/         # 🔌 APP API REST
│   ├── models.py        # Modelli database (ChatMessage, ChatSession)
│   ├── serializers.py   # Convertitori JSON ↔ Python
│   ├── services.py      # Logica business + OpenAI
│   ├── views.py         # Endpoint API (/api/chat/, /api/health/)
│   └── urls.py          # Router URL API
│
├── chatbot_web/         # 🌐 APP INTERFACCIA WEB
│   ├── views.py         # View per pagina web
│   ├── urls.py          # Router URL web
│   └── templates/       # File HTML
│       └── chat.html    # Interfaccia chat
│
├── .env                 # 🔐 VARIABILI SEGRETE
├── requirements.txt     # 📦 DIPENDENZE PYTHON
└── manage.py           # 🚀 SCRIPT GESTIONE DJANGO
```

---

## 📊 FLUSSO DEI DATI

```
1. UTENTE scrive messaggio nell'interfaccia web (chat.html)
   ↓
2. JAVASCRIPT invia richiesta POST a /api/chat/
   ↓
3. DJANGO views.py riceve la richiesta
   ↓
4. SERIALIZER valida i dati (message, session_id)
   ↓
5. CHATBOT SERVICE chiama API OpenAI
   ↓
6. OPENAI restituisce la risposta
   ↓
7. DATABASE salva conversazione (models.py)
   ↓
8. RISPOSTA torna al frontend come JSON
   ↓
9. JAVASCRIPT mostra la risposta nella chat
```

---

## 🧩 SPIEGAZIONE DEI COMPONENTI

### 📋 **models.py** - STRUTTURA DATABASE

```python
# TABELLA: chatbot_api_chatmessage
class ChatMessage(models.Model):
    id = AutoField()                    # 🔑 Chiave primaria automatica
    user_message = TextField()          # 💬 Messaggio dell'utente
    assistant_response = TextField()    # 🤖 Risposta del chatbot
    created_at = DateTimeField()        # 📅 Quando è stata creata

# TABELLA: chatbot_api_chatsession
class ChatSession(models.Model):
    id = AutoField()                    # 🔑 Chiave primaria automatica
    session_id = CharField()            # 🏷️ ID univoco della sessione
    created_at = DateTimeField()        # 📅 Quando è stata creata
    updated_at = DateTimeField()        # 🔄 Ultimo aggiornamento
```

### 🔄 **serializers.py** - CONVERSIONE DATI

```python
# INPUT: Valida dati in arrivo dal frontend
ChatRequestSerializer:
  - message: str (max 1000 caratteri)     # Il messaggio dell'utente
  - session_id: str (opzionale)          # ID della conversazione

# OUTPUT: Formatta risposte per il frontend
ChatResponseSerializer:
  - response: str                         # Risposta del chatbot
  - session_id: str                       # ID della sessione
  - success: bool                         # true/false se è andata bene
  - error: str (opzionale)                # Messaggio di errore
```

### 🧠 **services.py** - LOGICA PRINCIPALE

```python
class ChatbotService:
    def __init__():
        # Configura OpenAI API key
        # Imposta messaggio di sistema ("Sei un assistente gentile")

    def chat(user_message, session_id):
        # 1. Recupera cronologia conversazione
        # 2. Aggiunge nuovo messaggio utente
        # 3. Chiama OpenAI API (gpt-4.1-nano)
        # 4. Salva tutto nel database
        # 5. Restituisce risposta formattata

    def get_session_messages(session_id):
        # Recupera messaggi precedenti dal database
        # Li formatta per OpenAI: [{"role": "user", "content": "..."}]

    def _save_chat_message(user_msg, ai_response):
        # Salva nel database: ChatMessage.objects.create(...)
```

### 🌐 **views.py** - ENDPOINT API

```python
@api_view(['POST'])
def chat_endpoint(request):
    # 1. Valida dati con ChatRequestSerializer
    # 2. Estrae message e session_id
    # 3. Chiama ChatbotService.chat()
    # 4. Restituisce risposta JSON

@api_view(['GET'])
def health_check(request):
    # Semplice endpoint per verificare che l'API funzioni

@api_view(['GET'])
def chat_history(request):
    # Restituisce ultimi 20 messaggi dal database
```

### 🎨 **chat.html** - INTERFACCIA UTENTE

```html
<div class="chat-container">
    <div class="chat-header">🤖 Assistente AI</div>

    <div class="chat-messages" id="chatMessages">
        <!-- I messaggi appaiono qui dinamicamente -->
    </div>

    <div class="chat-input-container">
        <input id="messageInput" placeholder="Scrivi..." />
        <button onclick="sendMessage()">Invia</button>
    </div>
</div>

<script>
    function sendMessage() {
        // 1. Prende il messaggio dall'input
        // 2. Lo mostra nella chat come messaggio utente
        // 3. Invia richiesta POST a /api/chat/
        // 4. Mostra la risposta come messaggio assistente
    }
</script>
```

---

## 🔧 CONFIGURAZIONE TECNICA

### **settings.py** - Impostazioni Principali

```python
INSTALLED_APPS = [
    'django.contrib.admin',        # Admin panel Django
    'django.contrib.auth',         # Sistema autenticazione
    'rest_framework',              # API REST
    'corsheaders',                 # CORS per chiamate AJAX
    'chatbot_api',                 # La nostra app API
    'chatbot_web',                 # La nostra app web
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # CORS per AJAX
    'django.middleware.csrf.CsrfViewMiddleware',  # Sicurezza CSRF
    # ... altri middleware
]

# Configurazione Django REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.AllowAny'],
    'DEFAULT_RENDERER_CLASSES': ['rest_framework.renderers.JSONRenderer'],
}

# Configurazione CORS (per chiamate AJAX)
CORS_ALLOWED_ORIGINS = ["http://localhost:8000", "http://127.0.0.1:8000"]

# Chiave API OpenAI dalle variabili d'ambiente
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
```

### **urls.py** - Routing URL

```python
# chatbot_project/urls.py (PRINCIPALE)
urlpatterns = [
    path('admin/', admin.site.urls),        # /admin/ → Admin Django
    path('api/', include('chatbot_api.urls')),  # /api/* → API endpoints
    path('', include('chatbot_web.urls')),      # /* → Interfaccia web
]

# chatbot_api/urls.py (API)
urlpatterns = [
    path('chat/', views.chat_endpoint),     # POST /api/chat/
    path('health/', views.health_check),    # GET /api/health/
    path('history/', views.chat_history),   # GET /api/history/
]

# chatbot_web/urls.py (WEB)
urlpatterns = [
    path('', views.chat_interface),         # GET / → Pagina chat
]
```

---

## 🐛 DEBUG E SVILUPPO

### **VS Code Launch Configuration**

```json
{
    "name": "Django Chatbot - Debug Server",
    "type": "debugpy",
    "program": "${workspaceFolder}/Giorno 18/esempi_django/manage.py",
    "args": ["runserver", "127.0.0.1:8000", "--noreload"],
    "cwd": "${workspaceFolder}/Giorno 18/esempi_django",
    "env": { "DJANGO_SETTINGS_MODULE": "chatbot_project.settings" }
}
```

### **Come Debuggare:**

1. **Metti breakpoint** nei file Python (clicca sul numero di riga)
2. **Avvia debug** con "Django Chatbot - Debug Server"
3. **Interagisci** con l'interfaccia web su http://127.0.0.1:8000
4. **Il debugger si ferma** sui breakpoint, puoi:
    - Ispezionare variabili
    - Eseguire codice step-by-step
    - Vedere lo stack delle chiamate

### **Punti di Debug Utili:**

-   `chatbot_api/views.py:42` → Quando arriva una richiesta chat
-   `chatbot_api/services.py:90` → Prima di chiamare OpenAI
-   `chatbot_api/services.py:96` → Dopo aver ricevuto risposta OpenAI
-   `chatbot_api/models.py` → Quando si salvano dati nel database

---

## 🚀 COMANDI UTILI

```bash
# Avviare il server di sviluppo
python manage.py runserver

# Creare migrazioni dopo modifiche ai models
python manage.py makemigrations

# Applicare migrazioni al database
python manage.py migrate

# Aprire shell Django per test
python manage.py shell

# Creare superuser per admin
python manage.py createsuperuser

# Vedere log in tempo reale (Windows)
Get-Content -Path "django.log" -Wait
```

---

## 🎓 CONCETTI DIDATTICI IMPORTANTI

### **1. Separazione delle Responsabilità**

-   **Models**: Gestiscono i dati (database)
-   **Views**: Gestiscono le richieste HTTP
-   **Services**: Contengono la logica business
-   **Serializers**: Gestiscono la conversione dati
-   **Templates**: Gestiscono la presentazione

### **2. API REST**

-   **GET**: Recuperare dati (es. /api/health/)
-   **POST**: Inviare dati (es. /api/chat/)
-   **Status Codes**: 200 (OK), 400 (Bad Request), 500 (Server Error)
-   **JSON**: Formato standard per scambio dati

### **3. Frontend-Backend Communication**

-   **AJAX**: Chiamate asincrone JavaScript → Django
-   **CSRF Token**: Sicurezza contro attacchi Cross-Site
-   **CORS**: Permessi per chiamate cross-origin

### **4. Gestione Errori**

-   **Try-Catch**: Catturare errori Python
-   **Logging**: Registrare errori per debug
-   **Validation**: Validare input utente
-   **Graceful Degradation**: Messaggi d'errore user-friendly

### **5. Environment Variables**

-   **API Keys**: Mai committare in Git
-   **Configuration**: Separare config da codice
-   **Security**: Proteggere informazioni sensibili

---

## 🔐 SICUREZZA

### **Cosa FARE:**

✅ Usare `.env` per API keys  
✅ Validare tutti gli input  
✅ Limitare rate delle richieste  
✅ Usare HTTPS in produzione  
✅ Configurare `ALLOWED_HOSTS` correttamente

### **Cosa NON fare:**

❌ Non committare `.env` in Git  
❌ Non disabilitare CSRF in produzione  
❌ Non loggare informazioni sensibili  
❌ Non fidarsi mai dell'input utente

---

## 📈 POSSIBILI MIGLIORAMENTI

1. **Autenticazione Utenti**: Login/logout per sessioni personali
2. **Rate Limiting**: Limitare richieste per IP
3. **Caching**: Cache Redis per risposte frequenti
4. **WebSockets**: Chat real-time invece di polling
5. **Database Avanzato**: PostgreSQL invece di SQLite
6. **Deployment**: Docker, AWS, Heroku
7. **Testing**: Unit test e integration test
8. **Monitoring**: Logs strutturati, metriche performance

---

## 🎯 OBIETTIVI DIDATTICI RAGGIUNTI

✅ **Django Framework**: Creazione progetto completo  
✅ **Django REST Framework**: API moderne  
✅ **Database ORM**: Modelli e migrazioni  
✅ **Frontend Integration**: JavaScript + Django  
✅ **External APIs**: Integrazione OpenAI  
✅ **Error Handling**: Gestione robusta errori  
✅ **Debugging**: Setup environment sviluppo  
✅ **Best Practices**: Struttura progetto pulita  
✅ **Security**: Protezione base applicazione

---

**💡 Suggerimento per Studenti:**  
Esperimenta modificando piccole parti del codice e osserva i risultati. Il modo migliore per imparare è provare, sbagliare, e correggere! 🚀
