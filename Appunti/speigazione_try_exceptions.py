try:
    with open(
        "file.txt", "r", encoding="utf-8"
    ) as f:  # Apriamo il file in modalità di lettura ("r")
        contenuto = f.read()  # Leggiamo tutto il contenuto del file
        print(contenuto)  # Stampiamo il contenuto del file
        f.close()  # Chiudiamo il file
except FileNotFoundError:
    print("Il file non esiste.")
except Exception as e:
    print(f"Si è verificato un errore: {e}")
finally:
    print("")
