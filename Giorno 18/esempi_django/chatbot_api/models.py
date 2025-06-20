# Importiamo il modulo models di Django che contiene tutte le classi per creare tabelle nel database
from django.db import models


# Creiamo il modello ChatMessage che rappresenta una tabella nel database
class ChatMessage(models.Model):
    # Campo di testo per salvare il messaggio dell'utente (può essere molto lungo)
    user_message = models.TextField()

    # Campo di testo per salvare la risposta dell'assistente AI
    assistant_response = models.TextField()

    # Campo data/ora che si riempie automaticamente quando creiamo un nuovo record
    created_at = models.DateTimeField(auto_now_add=True)

    # Classe Meta: configurazioni aggiuntive per il modello
    class Meta:
        # Ordiniamo i messaggi dal più recente al più vecchio (- significa decrescente)
        ordering = ["-created_at"]

    # Metodo __str__: definisce come viene mostrato l'oggetto quando lo stampiamo
    def __str__(self):
        return (
            f"Chat {self.id} - {self.created_at}"  # id è la chiave primaria automatica
        )


# Modello per gestire le sessioni di chat (conversazioni separate)
class ChatSession(models.Model):
    # ID univoco della sessione (stringa di massimo 100 caratteri)
    session_id = models.CharField(max_length=100, unique=True)

    # Data di creazione della sessione (si riempie automaticamente)
    created_at = models.DateTimeField(auto_now_add=True)

    # Data di ultimo aggiornamento (si aggiorna automaticamente ad ogni modifica)
    updated_at = models.DateTimeField(auto_now=True)

    # Metodo per rappresentare l'oggetto come stringa
    def __str__(self):
        return f"Session {self.session_id}"
