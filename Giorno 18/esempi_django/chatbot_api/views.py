# Importiamo i moduli necessari da Django REST Framework
from rest_framework import status  # Codici di stato HTTP (200, 400, 500, etc.)
from rest_framework.decorators import api_view  # Decoratore per creare API views
from rest_framework.response import Response  # Classe per le risposte HTTP

# Importiamo i nostri serializers per validare e formattare i dati
from .serializers import ChatRequestSerializer, ChatResponseSerializer

# Importiamo il nostro servizio chatbot che contiene la logica principale
from .services import ChatbotService

# Importiamo uuid per generare ID unici per le sessioni
import uuid


# Decoratore che specifica che questa funzione accetta solo richieste POST
@api_view(["POST"])
def chat_endpoint(request):
    """
    Endpoint per inviare messaggi al chatbot
    Questo è l'endpoint principale che riceve i messaggi dall'interfaccia web
    e restituisce le risposte del chatbot
    """
    # Creiamo un serializer per validare i dati ricevuti nella richiesta
    serializer = ChatRequestSerializer(data=request.data)

    # Controlliamo se i dati sono validi secondo le regole del serializer
    if not serializer.is_valid():
        # Se i dati non sono validi, ritorniamo un errore 400 (Bad Request)
        return Response(
            {"error": "Dati non validi", "details": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    # Estraiamo il messaggio dell'utente dai dati validati
    user_message = serializer.validated_data["message"]
    
    # Estraiamo l'ID della sessione, se non c'è ne generiamo uno nuovo
    session_id = serializer.validated_data.get("session_id", str(uuid.uuid4()))

    # Creiamo un'istanza del servizio chatbot
    chatbot_service = ChatbotService()
    
    # Chiamiamo il metodo chat per ottenere la risposta
    result = chatbot_service.chat(user_message, session_id)

    # Creiamo un serializer per formattare la risposta
    response_serializer = ChatResponseSerializer(data=result)
    
    # Controlliamo se la serializzazione è andata a buon fine
    if response_serializer.is_valid():
        # Ritorniamo la risposta con status 200 (OK)
        return Response(response_serializer.data, status=status.HTTP_200_OK)
    else:
        # Se c'è un errore nella serializzazione, ritorniamo errore 500
        return Response(
            {"error": "Errore nella serializzazione della risposta"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


# Endpoint che accetta solo richieste GET per verificare lo stato dell'API
@api_view(["GET"])
def health_check(request):
    """
    Endpoint di health check
    Questo endpoint serve per verificare che l'API sia funzionante
    """
    return Response({"status": "ok", "message": "API is running"})


# Endpoint GET per recuperare la cronologia delle conversazioni
@api_view(["GET"])
def chat_history(request):
    """
    Endpoint per recuperare la cronologia delle chat
    Questo endpoint restituisce gli ultimi messaggi salvati nel database
    """
    # Importiamo i modelli e serializers necessari
    from .models import ChatMessage
    from .serializers import ChatMessageSerializer

    # Prendiamo gli ultimi 20 messaggi dal database
    messages = ChatMessage.objects.all()[:20]  # Ultimi 20 messaggi
    
    # Serializziamo i messaggi in formato JSON (many=True per liste)
    serializer = ChatMessageSerializer(messages, many=True)

    # Ritorniamo la lista dei messaggi
    return Response({"messages": serializer.data})
