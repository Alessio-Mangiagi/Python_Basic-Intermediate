# I principali metodi HTTP: 


# GET
# GET serve per ottenere dati da una risorsa.
# _________________________
# import requests

# # Effettuare una richiesta GET
# response = requests.get(
#     'https://api.esempio.com/utenti',
#     params={'attivi': 'true'}
# )

# # Verificare lo stato della risposta
# if response.status_code == 200:
#     utenti = response.json()
#     print(utenti)
# _________________________


# POST
# POST serve per creare una nuova risorsa.
# _________________________
# import requests

# Effettuare una richiesta POST
# nuovo_utente = {
#     'nome': 'Luca',
#     'email': 'luca@example.com'
# }
# response = requests.post(
#     'https://api.esempio.com/utenti',
#     json=nuovo_utente
# )

# # Verificare lo stato della risposta
# if response.status_code == 201:
#     utente_creato = response.json()
#     print(utente_creato)
# _________________________


# PUT
# PUT serve per aggiornare una risorsa esistente (sostituzione completa).
# _________________________
# import requests

# # Aggiornare completamente un utente esistente
# utente_aggiornato = {
#     'nome': 'Luca Modificato',
#     'email': 'luca.modificato@example.com'
# }
# response = requests.put(
#     'https://api.esempio.com/utenti/1',
#     json=utente_aggiornato
# )

# # Verificare lo stato della risposta
# if response.status_code == 200:
#     utente = response.json()
#     print(utente)
# _________________________


# DELETE
# DELETE serve per eliminare una risorsa.
# _________________________
# import requests

# # Eliminare un utente esistente
# response = requests.delete('https://api.esempio.com/utenti/1')

# # Verificare lo stato della risposta
# if response.status_code == 204:
#     print('Utente eliminato con successo')
# else:
#     print('Errore nell\'eliminazione')
# _________________________


# _-_-_-_-_-_-_-_-_-_-_-_-_
# I codici di stato HTTP (status codes): 200, 201, 400, 404, 500

# 200 OK: richiesta riuscita
# 201 Created: risorsa creata
# 400 Bad Request: richiesta errata
# 404 Not Found: risorsa non trovata
# 429 Too Many Requests: troppe richieste inviate in un breve periodo
# 500 Internal Server Error: errore del server

# _-_-_-_-_-_-_-_-_-_-_-_-_
# Autenticazione nelle API REST: API Key, Basic Auth, OAuth 2.0

# _________________________
# # --- API Key ---
# # Un token semplice inviato come parametro URL o header. È il metodo più basilare ma anche meno sicuro.
# import requests
# response = requests.get(
#     'https://api.esempio.com/dati',
#     headers={'X-API-Key': 'chiave_segreta'}
# )

# # --- Basic Auth ---
# # Credenziali username:password codificate in Base64. Semplice ma deve essere usato sempre con HTTPS.
# from requests.auth import HTTPBasicAuth
# response = requests.get(
#     'https://api.esempio.com/dati',
#     auth=HTTPBasicAuth('utente', 'password')
# )

# # --- OAuth 2.0 ---
# # Standard avanzato che permette autorizzazioni granulari e token temporanei. Più complesso ma molto più sicuro.
# headers = {
#     'Authorization': 'Bearer token_accesso'
# }
# response = requests.get(
#     'https://api.esempio.com/dati',
#     headers=headers
# )
# _________________________

# _-_-_-_-_-_-_-_-_-_-_-_-_
# Serializzazione e deserializzazione JSON
# Serializzazione: trasformare oggetti Python in stringhe JSON.
# Deserializzazione: convertire stringhe JSON in oggetti Python.
# _________________________
# import json
# utente = {"nome": "Anna", "eta": 25}
# json_str = json.dumps(utente)  # Serializzazione
# utente2 = json.loads(json_str)  # Deserializzazione
# # "utente" è un dizionario Python, "json_str" è una stringa JSON, "utente2" è di nuovo un dizionario Python.
# _________________________


# API per testing e learning
# https://jsonplaceholder.typicode.com/ # Esempio: https://jsonplaceholder.typicode.com/posts
# https://reqres.in/ # (RICHIEDE API KEY) Esempio: https://reqres.in/api/users
# https://bored-api.appbrewery.com/ # Esempio: https://bored-api.appbrewery.com/random 
# https://dog.ceo/dog-api/ #Esempio: https://dog.ceo/api/breeds/image/random
# https://docs.spacexdata.com/ #Esempio: https://api.spacexdata.com/v4/launches/latest
# https://restcountries.com/ #Esempio: https://restcountries.com/v3.1/name/italy
# https://openweathermap.org/api # (RICHIEDE API KEY) Esempio: https://api.openweathermap.org/data/2.5/weather?q=London
