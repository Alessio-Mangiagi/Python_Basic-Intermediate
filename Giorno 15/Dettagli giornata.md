### Giorno 15
- **Teoria: Concetti di API REST, metodi HTTP, JSON**

1. Introduzione alle API REST: definizione e scopo.
2. Il concetto di *stateless* nelle API REST.
3. Struttura di un endpoint REST.
4. I principali metodi HTTP: GET.
5. I principali metodi HTTP: POST.
6. I principali metodi HTTP: PUT.
7. I principali metodi HTTP: DELETE.
8. Differenza tra PUT e PATCH.
9. I codici di stato HTTP (status codes): 200, 201, 400, 404, 500.
10. Autenticazione nelle API REST: token, header, OAuth.
11. Sicurezza nelle API REST: HTTPS, CORS.
12. Formato JSON: struttura base (oggetti e array).
13. Serializzazione e deserializzazione JSON.
14. Differenza tra XML e JSON.
15. Perché REST è così diffuso nelle applicazioni moderne.

- **Pratica: Chiamate base con la libreria requests**

1. Installazione della libreria `requests`.
2. Eseguire una semplice chiamata GET.
3. Parsing della risposta JSON.
4. Gestire errori con `response.status_code`.
5. Aggiungere parametri alle richieste GET.
6. Eseguire una chiamata POST con dati JSON.
7. Inviare header personalizzati.
8. Gestire autenticazione base con `requests.auth`.
9. Timeout delle richieste.
10. Retry automatici con `requests.adapters`.
11. Logging delle chiamate HTTP.
12. Scaricare file tramite API.
13. Upload di file con `requests`.
14. Gestire eccezioni di rete.
15. Creare una semplice funzione wrapper per chiamate REST.