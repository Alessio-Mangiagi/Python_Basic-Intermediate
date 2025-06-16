'''Fai una richiesta GET a https://httpbin.org/get inviando una API key nell’header X-API-Key (scegli tu il valore).

Fai una richiesta GET a https://httpbin.org/basic-auth/utente/password123 usando utente come user e password123 come password con HTTPBasicAuth.
(Prova anche a cambiare password e osserva lo status code!)

Fai una richiesta GET a https://httpbin.org/bearer inviando nell’header Authorization: Bearer 12345abcde.

Per ogni chiamata, stampa:

Lo status code

La parte della risposta che conferma l’autenticazione (ad esempio "authenticated": true)'''


import requests
from dotenv import load_dotenv
import os
from requests.auth import HTTPBasicAuth
load_dotenv()

# url = "https://httpbin.org/get"
# x_key = {'X-API-Key': os.getenv('x_key')}

# response = requests.get(url,headers=x_key)
# print(response.status_code)
# print(response.json())

# url = "https://httpbin.org/basic-auth/Alessio/password123"
# Alessio = (os.getenv('utente'), os.getenv('password'))
# response = requests.get(url, auth=Alessio)
# print(response.status_code)
# print(response.json())
#password modificata per dare errore 401

# url = "https://httpbin.org/bearer"
# headers = {"Authorization": f"Bearer {os.getenv('token')}"}

# response = requests.get(url,headers=headers)
# print(response.status_code)
# print(response.json())

#non perdere il file .env con le chiavi di autenticazione