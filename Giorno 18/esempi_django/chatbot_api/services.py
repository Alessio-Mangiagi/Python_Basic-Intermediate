# Importiamo la libreria openai per comunicare con l'API di OpenAI
# Importiamo il sistema di logging per registrare errori e informazioni
import logging

# Importiamo os per accedere alle variabili d'ambiente (non utilizzato direttamente qui)
import os

# Importiamo le tipizzazioni per rendere il codice più leggibile e sicuro
from typing import Any, Dict, List

import openai

# Importiamo le impostazioni di Django per accedere alle configurazioni del progetto
from django.conf import settings

# Creiamo un logger specifico per questo modulo
logger = logging.getLogger(__name__)


# Classe principale che gestisce tutta la logica del chatbot
class ChatbotService:
    def __init__(self):
        # Configuriamo la chiave API di OpenAI dalle impostazioni Django
        openai.api_key = settings.OPENAI_API_KEY

        # Definiamo i messaggi di sistema di default che impostano il comportamento del chatbot
        self.default_messages = [
            {"role": "system", "content": "Sei un assistente gentile."}
        ]

    def get_session_messages(self, session_id: str) -> List[Dict[str, str]]:
        """
        Recupera i messaggi della sessione dal database
        Questa funzione prende tutti i messaggi precedenti di una conversazione
        """
        # Importiamo il modello qui per evitare importazioni circolari
        from .models import ChatMessage

        # Iniziamo con i messaggi di default (messaggio di sistema)
        messages = list(self.default_messages)

        # Recuperiamo i messaggi precedenti della sessione dal database
        chat_messages = ChatMessage.objects.filter(
            id__in=self._get_session_message_ids(session_id)
        ).order_by("created_at")

        # Per ogni messaggio nel database, aggiungiamo sia la domanda dell'utente che la risposta
        for chat_msg in chat_messages:
            # Aggiungiamo il messaggio dell'utente
            messages.append({"role": "user", "content": chat_msg.user_message})
            # Aggiungiamo la risposta dell'assistente
            messages.append(
                {"role": "assistant", "content": chat_msg.assistant_response}
            )

        return messages

    def _get_session_message_ids(self, session_id: str) -> List[int]:
        """
        Helper per recuperare gli ID dei messaggi di una sessione
        Implementazione semplificata - in produzione potresti voler limitare il numero
        """
        from .models import ChatMessage

        # Prendiamo solo gli ultimi 20 messaggi per evitare di sovraccaricare l'API
        return list(ChatMessage.objects.values_list("id", flat=True)[:20])

    def chat(
        self, user_message: str, session_id: str = None, streaming: bool = False
    ) -> Dict[str, Any]:
        """
        Elabora un messaggio dell'utente e restituisce la risposta del chatbot
        Questo è il metodo principale che:
        1. Recupera la cronologia della conversazione
        2. Aggiunge il nuovo messaggio
        3. Chiama l'API OpenAI (normale o streaming)
        4. Salva tutto nel database

        Args:
            user_message: Il messaggio dell'utente
            session_id: ID della sessione di chat (opzionale)
            streaming: Se True, attiva lo streaming delle risposte
        """
        try:
            # Recuperiamo i messaggi della sessione se esiste un session_id,
            # altrimenti usiamo solo i messaggi di default
            messages = (
                self.get_session_messages(session_id)
                if session_id
                else list(self.default_messages)
            )

            # Aggiungiamo il nuovo messaggio dell'utente alla conversazione
            messages.append({"role": "user", "content": user_message})

            # Se è richiesto lo streaming, usiamo una logica diversa
            if streaming:
                return self._chat_with_streaming(messages, user_message, session_id)
            else:
                return self._chat_normal(messages, user_message, session_id)

        # Gestiamo gli errori specifici dell'API OpenAI
        except openai.OpenAIError as e:
            # Registriamo l'errore nel log per il debugging
            logger.error(f"OpenAI API Error: {e}")
            return {
                "response": "Mi dispiace, si è verificato un errore. Riprova più tardi.",
                "session_id": session_id or "default",
                "success": False,
                "is_streaming": streaming,  # Manteniamo l'informazione sul tipo di richiesta
                "is_final": True,  # Gli errori sono sempre "finali"
                "error": str(e),  # Includiamo il messaggio di errore
            }

        # Gestiamo tutti gli altri errori imprevisti
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return {
                "response": "Si è verificato un errore inaspettato.",
                "session_id": session_id or "default",
                "success": False,
                "is_streaming": streaming,  # Manteniamo l'informazione sul tipo di richiesta
                "is_final": True,  # Gli errori sono sempre "finali"
                "error": str(e),
            }

    def _save_chat_message(
        self, user_message: str, assistant_response: str, session_id: str = None
    ):
        """
        Salva il messaggio nel database
        Questo metodo privato (inizia con _) viene chiamato internamente
        per salvare ogni conversazione nel database
        """
        # Importiamo il modello qui per evitare problemi di importazione circolare
        from .models import ChatMessage

        # Creiamo un nuovo record nel database con la domanda e la risposta
        ChatMessage.objects.create(
            user_message=user_message,  # Il messaggio dell'utente
            assistant_response=assistant_response,  # La risposta del chatbot
            # Nota: created_at si riempie automaticamente grazie ad auto_now_add=True
            # session_id non è utilizzato in questa implementazione semplificata
        )

    def _chat_normal(
        self, messages: List[Dict[str, str]], user_message: str, session_id: str = None
    ) -> Dict[str, Any]:
        """
        Gestisce la chat normale (senza streaming)
        Questa è la logica originale che abbiamo sempre usato
        """
        # Chiamiamo l'API di OpenAI per ottenere la risposta completa
        response = openai.chat.completions.create(
            model="gpt-4.1-nano",  # Il modello AI da utilizzare
            messages=messages,  # Tutta la cronologia della conversazione
            max_tokens=1000,  # Massimo numero di token (parole) nella risposta
            stream=False,  # Streaming disabilitato = risposta completa in una volta
        )

        # Estraiamo la risposta del chatbot dalla risposta dell'API
        assistant_response = response.choices[0].message.content

        # Salviamo sia la domanda che la risposta nel database
        self._save_chat_message(user_message, assistant_response, session_id)

        # Ritorniamo un dizionario con il successo dell'operazione
        return {
            "response": assistant_response,  # La risposta completa del chatbot
            "session_id": session_id or "default",  # L'ID della sessione
            "success": True,  # Operazione riuscita
            "is_streaming": False,  # Non è streaming
            "is_final": True,  # È la risposta finale
        }

    def _chat_with_streaming(
        self, messages: List[Dict[str, str]], user_message: str, session_id: str = None
    ) -> Dict[str, Any]:
        """
        Gestisce la chat con streaming
        In modalità streaming, la risposta arriva pezzo per pezzo in tempo reale
        Questo metodo raccoglie tutti i pezzi e li concatena per salvare nel database
        """
        # Chiamiamo l'API OpenAI con streaming abilitato
        response_stream = openai.chat.completions.create(
            model="gpt-4.1-nano",  # Il modello AI da utilizzare
            messages=messages,  # Tutta la cronologia della conversazione
            max_tokens=1000,  # Massimo numero di token (parole) nella risposta
            stream=True,  # Streaming abilitato = risposta arriva pezzo per pezzo
        )

        # Inizializziamo una stringa vuota per raccogliere tutti i pezzi
        complete_response = ""

        # Iteriamo attraverso tutti i chunk (pezzi) che arrivano
        for chunk in response_stream:
            # Ogni chunk contiene un pezzo della risposta
            if chunk.choices[0].delta.content is not None:
                # Aggiungiamo il pezzo alla risposta completa
                chunk_content = chunk.choices[0].delta.content
                complete_response += chunk_content

        # Ora che abbiamo la risposta completa, la salviamo nel database
        # (In una implementazione più avanzata, potresti voler salvare i chunk uno per uno)
        self._save_chat_message(user_message, complete_response, session_id)

        # Ritorniamo la risposta completa
        # Nota: In questa implementazione semplificata ritorniamo la risposta completa
        # In un'implementazione più avanzata, dovresti ritornare ogni chunk separatamente
        return {
            "response": complete_response,  # La risposta completa assemblata
            "session_id": session_id or "default",  # L'ID della sessione
            "success": True,  # Operazione riuscita
            "is_streaming": True,  # Era in modalità streaming
            "is_final": True,  # Questo è l'ultimo (e unico) chunk che ritorniamo
        }
