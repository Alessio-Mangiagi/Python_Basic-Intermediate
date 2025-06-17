import requests
from requests.auth import HTTPBasicAuth

# URL base del server Flask API
BASE_URL = "http://localhost:5000"

# API_KEY = "supersecretapikey"
# BASIC_USER = "utente"
# BASIC_PASS = "password123"
# BEARER_TOKEN = "abcde12345token"


def test_get(name=None):
    """Testa l'endpoint GET /items con filtro opzionale per nome."""
    print("\n--- GET /items ---")
    if not name is None:
        # Richiesta GET con parametro di query per filtrare per nome
        params = {"name": name}
        response = requests.get(f"{BASE_URL}/items", params=params)
    else:
        # Richiesta GET per ottenere tutti gli items
        response = requests.get(f"{BASE_URL}/items")

    print("Status:", response.status_code)
    print("Risposta:", response.json())


def test_post(name="Test", desc="Nuovo item"):
    """Testa l'endpoint POST /items per creare un nuovo item."""
    print("\n--- POST /items ---")
    data = {"name": name, "desc": desc}
    response = requests.post(f"{BASE_URL}/items", json=data)
    print("Status:", response.status_code)
    print("Risposta:", response.json())


def test_put(item_id, new_name, new_desc):
    """Testa l'endpoint PUT /items per aggiornare completamente un item."""
    print("\n--- PUT /items ---")
    data = {"id": item_id, "name": new_name, "desc": new_desc}
    response = requests.put(f"{BASE_URL}/items", json=data)
    print("Status:", response.status_code)
    print("Risposta:", response.json())


def test_patch(item_id, new_name=None, new_desc=None):
    """Testa l'endpoint PATCH /items per aggiornare parzialmente un item."""
    print("\n--- PATCH /items ---")
    data = {"id": item_id}
    # Aggiunge solo i campi specificati per l'aggiornamento parziale
    if new_name is not None:
        data["name"] = new_name
    if new_desc is not None:
        data["desc"] = new_desc
    response = requests.patch(f"{BASE_URL}/items", json=data)
    print("Status:", response.status_code)
    print("Risposta:", response.json())


def test_delete(id):
    """Testa l'endpoint DELETE /items per eliminare un item."""
    print("\n--- DELETE /items ---")
    params = {"id": id}
    response = requests.delete(f"{BASE_URL}/items", params=params)
    print("Status:", response.status_code)
    print("Risposta:", response.json())


def test_apikey(key):
    """Testa l'endpoint protetto con autenticazione tramite API key."""
    print("\n--- GET /protected/apikey ---")
    headers = {"X-API-Key": key}
    response = requests.get(f"{BASE_URL}/protected/apikey", headers=headers)
    print("Status:", response.status_code)
    print("Risposta:", response.json())


def test_basic_auth(username, password):
    """Testa l'endpoint protetto con autenticazione HTTP Basic."""
    print("\n--- GET /protected/basic ---")
    auth = HTTPBasicAuth(username, password)
    response = requests.get(f"{BASE_URL}/protected/basic", auth=auth)
    print("Status:", response.status_code)
    print("Risposta:", response.json())


def test_bearer(token):
    """Testa l'endpoint protetto con autenticazione Bearer token."""
    print("\n--- GET /protected/bearer ---")
    headers = {"Authorization": "Bearer" + f" {token}"}
    response = requests.get(f"{BASE_URL}/protected/bearer", headers=headers)
    print("Status:", response.status_code)
    print("Risposta:", response.json())


# Dati di esempio per i test (commentati)
# ITEMS = [
#     {"id": 1, "name": "Test", "desc": "Primo item"},
#     {"id": 2, "name": "Ciao", "desc": "Secondo item"},
#     {"id": 3, "name": "Python", "desc": "Terzo item"},
# ]

# Test delle operazioni CRUD (commentati)
# test_get()
# test_post("Alessio", " Nuovo item Alessio")
# test_get("Alessio")
# test_put(4, "Tony", "Aggiornato")
# test_get()
# test_patch(4, new_name="Giada")
# test_get()
# test_delete(2)
# test_get()
