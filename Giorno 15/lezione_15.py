import json

# Serializzazione (Python -> JSON)
dati_python = {"nome": "Anna", "età": 28, "corsi": ["Python", "SQL"]}
json_string = json.dumps(dati_python, indent=2)

print("Dati serializzati in JSON:")
print(json_string)

# Deserializzazione (JSON -> Python)
json_ricevuto = '{"prodotto": "Laptop", "prezzo": 999.99}'
dati_python = json.loads(json_ricevuto)

print("\nDati deserializzati da JSON:")
print(dati_python)
