# Importiamo i moduli necessari da Django REST Framework
# Importiamo uuid per generare ID unici per le sessioni
import json
import uuid

from django.http import StreamingHttpResponse  # Per Server-Sent Events
from rest_framework import status  # Codici di stato HTTP (200, 400, 500, etc.)
from rest_framework.decorators import api_view  # Decoratore per creare API views
from rest_framework.response import Response  # Classe per le risposte HTTP

# Importiamo i nostri serializers per validare e formattare i dati
from .serializers import ChatRequestSerializer, ChatResponseSerializer

# Importiamo il nostro servizio chatbot che contiene la logica principale
from .services import ChatbotService


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

    # Estraiamo il flag streaming (default: False se non specificato)
    streaming = serializer.validated_data.get("streaming", False)

    # Creiamo un'istanza del servizio chatbot
    chatbot_service = ChatbotService()

    # Chiamiamo il metodo chat passando anche il parametro streaming
    result = chatbot_service.chat(user_message, session_id, streaming)

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


@api_view(["POST"])
def chat_stream_endpoint(request):
    """
    Endpoint per streaming in tempo reale con Server-Sent Events (SSE)
    Questo endpoint restituisce la risposta del chatbot pezzo per pezzo
    mentre viene generata da OpenAI
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

    # Funzione generatore per lo streaming
    def stream_response():
        """
        Funzione generatore che produce i chunk di risposta uno per volta
        Questa funzione viene chiamata da StreamingHttpResponse
        """
        try:
            # Recuperiamo i messaggi della sessione
            messages = (
                chatbot_service.get_session_messages(session_id)
                if session_id
                else list(chatbot_service.default_messages)
            )

            # Aggiungiamo il nuovo messaggio dell'utente
            messages.append({"role": "user", "content": user_message})

            # Chiamiamo l'API OpenAI con streaming
            import openai
            from django.conf import settings

            # Configura la chiave API
            openai.api_key = settings.OPENAI_API_KEY

            response_stream = openai.chat.completions.create(
                model="gpt-4.1-nano",
                messages=messages,
                max_tokens=1000,
                stream=True,
            )

            complete_response = ""

            # Mandiamo l'inizio dello stream
            yield f"data: {json.dumps({'type': 'start', 'session_id': session_id})}\n\n".encode(
                "utf-8"
            )

            # Iteriamo attraverso tutti i chunk che arrivano da OpenAI
            for chunk in response_stream:
                if chunk.choices[0].delta.content is not None:
                    chunk_content = chunk.choices[0].delta.content
                    complete_response += chunk_content

                    # Mandiamo ogni chunk al frontend
                    yield f"data: {json.dumps({'type': 'chunk', 'content': chunk_content})}\n\n".encode(
                        "utf-8"
                    )

            # Mandiamo la fine dello stream
            yield f"data: {json.dumps({'type': 'end', 'complete_response': complete_response})}\n\n".encode(
                "utf-8"
            )

            # Salviamo la conversazione completa nel database
            chatbot_service._save_chat_message(
                user_message, complete_response, session_id
            )

        except Exception as e:
            # In caso di errore, mandiamo l'errore come ultimo messaggio
            yield f"data: {json.dumps({'type': 'error', 'error': str(e)})}\n\n".encode(
                "utf-8"
            )

    # Ritorniamo una StreamingHttpResponse con i giusti headers per SSE
    response = StreamingHttpResponse(
        stream_response(), content_type="text/event-stream"
    )
    response["Cache-Control"] = "no-cache"
    response["Access-Control-Allow-Origin"] = "*"  # Per CORS
    return response
