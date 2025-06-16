"""Fai una richiesta GET a https://httpbin.org/get inviando una API key nell'header X-API-Key (scegli tu il valore).

Fai una richiesta GET a https://httpbin.org/basic-auth/utente/password123 usando utente come user e password123 come password con HTTPBasicAuth.
(Prova anche a cambiare password e osserva lo status code!)

Fai una richiesta GET a https://httpbin.org/bearer inviando nell'header Authorization: Bearer 12345abcde.

Per ogni chiamata, stampa:

Lo status code

La parte della risposta che conferma l'autenticazione (ad esempio "authenticated": true)
"""

import requests
from dotenv import load_dotenv
import os
from requests.auth import HTTPBasicAuth

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Prima richiesta: autenticazione con API key nell'header
url = "https://httpbin.org/get"
# Crea header con la chiave API dal file .env
x_key = {"X-API-Key": os.getenv("x_key")}

# Effettua la richiesta GET con l'header X-API-Key
response = requests.get(url, headers=x_key)
print(response.status_code)
print(response.json())

# Seconda richiesta: autenticazione HTTP Basic Auth
url = "https://httpbin.org/basic-auth/Alessio/password123"

# Crea oggetto HTTPBasicAuth con credenziali dal file .env
Alessio = HTTPBasicAuth(str(os.getenv("utente")), str(os.getenv("password")))
# Effettua la richiesta GET con autenticazione basic
response = requests.get(url, auth=Alessio)
print(response.status_code)
print(response.json())
# password modificata per dare errore 401

# Terza richiesta: autenticazione Bearer token
url = "https://httpbin.org/bearer"
# Crea header Authorization con Bearer token dal file .env
headers = {"Authorization": f"Bearer {os.getenv('token')}"}

# Effettua la richiesta GET con Bearer token
response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())

# non perdere il file .env con le chiavi di autenticazione
