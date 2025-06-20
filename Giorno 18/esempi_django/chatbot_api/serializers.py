# Importiamo il modulo serializers da Django REST Framework
# I serializers convertono i dati da Python a JSON e viceversa
from rest_framework import serializers

# Importiamo i nostri modelli dal file models.py
from .models import ChatMessage, ChatSession


# Serializer per il modello ChatMessage - converte gli oggetti del database in JSON
class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        # Specifichiamo quale modello usare
        model = ChatMessage
        # Specifichiamo quali campi includere nella serializzazione JSON
        fields = ["id", "user_message", "assistant_response", "created_at"]


# Serializer per validare i dati in arrivo dalle richieste HTTP
class ChatRequestSerializer(serializers.Serializer):
    # Campo obbligatorio per il messaggio dell'utente (massimo 1000 caratteri)
    message = serializers.CharField(max_length=1000)

    # Campo opzionale per l'ID della sessione (required=False significa che non è obbligatorio)
    session_id = serializers.CharField(max_length=100, required=False)

    # Campo opzionale per attivare lo streaming delle risposte (default: False)
    # Se True, la risposta arriverà pezzo per pezzo in tempo reale
    streaming = serializers.BooleanField(required=False, default=False)


# Serializer per formattare le risposte che inviamo al client
class ChatResponseSerializer(serializers.Serializer):
    # La risposta del chatbot (può essere completa o parziale se streaming=True)
    response = serializers.CharField()

    # L'ID della sessione utilizzata
    session_id = serializers.CharField()

    # Indica se l'operazione è andata a buon fine
    success = serializers.BooleanField()

    # Indica se la risposta è in modalità streaming
    is_streaming = serializers.BooleanField(default=False)

    # Se streaming=True, indica se questo è l'ultimo chunk della risposta
    is_final = serializers.BooleanField(default=True)

    # Messaggio di errore (opzionale, solo se success=False)
    error = serializers.CharField(required=False)
