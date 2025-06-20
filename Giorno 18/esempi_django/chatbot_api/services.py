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

    def chat(self, user_message: str, session_id: str = None) -> Dict[str, Any]:
        """
        Elabora un messaggio dell'utente e restituisce la risposta del chatbot
        Questo è il metodo principale che:
        1. Recupera la cronologia della conversazione
        2. Aggiunge il nuovo messaggio
        3. Chiama l'API OpenAI
        4. Salva tutto nel database
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

            # Chiamiamo l'API di OpenAI per ottenere la risposta
            response = openai.chat.completions.create(
                model="gpt-4.1-nano",  # Il modello AI da utilizzare
                messages=messages,  # Tutta la cronologia della conversazione
                max_tokens=150,  # Massimo numero di token (parole) nella risposta
            )

            # Estraiamo la risposta del chatbot dalla risposta dell'API
            assistant_response = response.choices[0].message.content

            # Salviamo sia la domanda che la risposta nel database
            self._save_chat_message(user_message, assistant_response, session_id)

            # Ritorniamo un dizionario con il successo dell'operazione
            return {
                "response": assistant_response,  # La risposta del chatbot
                "session_id": session_id or "default",  # L'ID della sessione
                "success": True,  # Operazione riuscita
            }

        # Gestiamo gli errori specifici dell'API OpenAI
        except openai.OpenAIError as e:
            # Registriamo l'errore nel log per il debugging
            logger.error(f"OpenAI API Error: {e}")
            return {
                "response": "Mi dispiace, si è verificato un errore. Riprova più tardi.",
                "session_id": session_id or "default",
                "success": False,
                "error": str(e),  # Includiamo il messaggio di errore
            }

        # Gestiamo tutti gli altri errori imprevisti
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return {
                "response": "Si è verificato un errore inaspettato.",
                "session_id": session_id or "default",
                "success": False,
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
