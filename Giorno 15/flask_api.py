from flask import Flask, request, jsonify, make_response
from functools import wraps

app = Flask(__name__)

# --- CONFIGURAZIONE SEMPLICE ---
API_KEY = "supersecretapikey"
BASIC_USER = "utente"
BASIC_PASS = "password123"
BEARER_TOKEN = "abcde12345token"

ITEMS = [
    {"id": 1, "name": "Test", "desc": "Primo item"},
    {"id": 2, "name": "Ciao", "desc": "Secondo item"},
    {"id": 3, "name": "Python", "desc": "Terzo item"},
]


# --- DECORATOR AUTENTICAZIONE API KEY ---
def require_api_key(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        key = request.headers.get("X-API-Key")
        if not key or key != API_KEY:
            return jsonify({"error": "Missing or invalid API Key"}), 401
        return f(*args, **kwargs)

    return decorated


# --- DECORATOR AUTENTICAZIONE BASIC ---
def require_basic_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or auth.username != BASIC_USER or auth.password != BASIC_PASS:
            return make_response(
                jsonify({"error": "Unauthorized"}),
                401,
                {"WWW-Authenticate": 'Basic realm="Login Required"'},
            )
        return f(*args, **kwargs)

    return decorated


# --- DECORATOR AUTENTICAZIONE BEARER TOKEN ---
def require_bearer_token(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get("Authorization")
        if not auth_header or not auth_header.startswith("Bearer "):
            return jsonify({"error": "Missing Bearer token"}), 401
        token = auth_header.split(" ")[1]
        if token != BEARER_TOKEN:
            return jsonify({"error": "Invalid Bearer token"}), 401
        return f(*args, **kwargs)

    return decorated


# --- ENDPOINT CRUD SENZA SICUREZZA ---


@app.route("/items", methods=["GET"])
def get_items():
    name = request.args.get("name")
    if name:
        # Cerca item per nome
        for item in ITEMS:
            if item["name"].lower() == name.lower():
                return jsonify(item), 200
        return jsonify({"error": "Item not found"}), 404
    else:
        # Ritorna tutta la lista
        return jsonify(ITEMS), 200


@app.route("/items", methods=["POST"])
def create_item():
    data = request.get_json()
    if not data or "name" not in data or "desc" not in data:
        return jsonify({"error": "name and desc richiesti"}), 400

    new_id = max((item["id"] for item in ITEMS), default=0) + 1
    nuovo_item = {"id": new_id, "name": data["name"], "desc": data["desc"]}
    ITEMS.append(nuovo_item)
    return jsonify(nuovo_item), 201


@app.route("/items", methods=["PUT"])
def put_item():
    data = request.get_json()
    if not data or "id" not in data or "name" not in data or "desc" not in data:
        return jsonify({"error": "id, name e desc richiesti"}), 400
    for item in ITEMS:
        if item["id"] == data["id"]:
            item["name"] = data["name"]
            item["desc"] = data["desc"]
            return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404


@app.route("/items", methods=["PATCH"])
def patch_item():
    data = request.get_json()
    if not data or "id" not in data:
        return jsonify({"error": "id richiesto"}), 400
    for item in ITEMS:
        if item["id"] == data["id"]:
            if "name" in data:
                item["name"] = data["name"]
            if "desc" in data:
                item["desc"] = data["desc"]
            return jsonify(item), 200
    return jsonify({"error": "Item not found"}), 404


@app.route("/items", methods=["DELETE"])
def delete_item():
    id_str = request.args.get("id")
    if not id_str or not id_str.isdigit():
        return jsonify({"error": "id numerico richiesto nei parametri"}), 400
    item_id = int(id_str)
    for idx, item in enumerate(ITEMS):
        if item["id"] == item_id:
            removed = ITEMS.pop(idx)
            return jsonify({"message": "Item eliminato", "item": removed}), 200
    return jsonify({"error": "Item not found"}), 404


# --- ENDPOINTS PROTETTI ---


@app.route("/protected/apikey", methods=["GET"])
@require_api_key
def protected_apikey():
    return jsonify({"message": "Accesso consentito con API Key!"}), 200


@app.route("/protected/basic", methods=["GET"])
@require_basic_auth
def protected_basic():
    return (
        jsonify(
            {"message": f"Accesso consentito con Basic Auth! Benvenuto {BASIC_USER}"}
        ),
        200,
    )


@app.route("/protected/bearer", methods=["GET"])
@require_bearer_token
def protected_bearer():
    return jsonify({"message": "Accesso consentito con Bearer Token!"}), 200


# --- AVVIO ---
if __name__ == "__main__":
    app.run(debug=True, port=5000)
