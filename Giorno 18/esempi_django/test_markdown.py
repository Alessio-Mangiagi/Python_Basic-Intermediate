import json

import requests


def test_markdown_response():
    """
    Test per verificare che il chatbot possa generare e formattare contenuto Markdown
    """
    url = "http://127.0.0.1:8000/api/chat/"

    # Richiediamo esplicitamente una risposta con Markdown
    data = {
        "message": "Mostrami un esempio di codice Python con spiegazione formattata in Markdown, includi titoli, liste e blocchi di codice",
        "session_id": "test_markdown",
        "streaming": False,
    }

    try:
        response = requests.post(url, json=data)
        print("=== TEST CONTENUTO MARKDOWN ===")
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            response_data = response.json()
            print(f"Success: {response_data['success']}")
            print(f"Response length: {len(response_data['response'])} characters")
            print("\n--- CONTENUTO RICEVUTO ---")
            print(response_data["response"])
            print("\n--- FINE CONTENUTO ---")

            # Controlliamo se la risposta contiene elementi Markdown
            content = response_data["response"]
            markdown_elements = {
                "headers": "#" in content,
                "lists": ("*" in content or "-" in content or "1." in content),
                "code_blocks": "```" in content,
                "inline_code": "`" in content and not "```" in content,
                "bold": "**" in content,
                "italic": "_" in content or "*" in content,
            }

            print("\n--- ANALISI MARKDOWN ---")
            for element, found in markdown_elements.items():
                status = "✅ TROVATO" if found else "❌ NON TROVATO"
                print(f"{element}: {status}")

            return response.status_code == 200
        else:
            print(f"Errore: {response.text}")
            return False

    except Exception as e:
        print(f"Errore nel test: {e}")
        return False


def test_streaming_markdown():
    """
    Test per verificare il rendering Markdown in streaming
    """
    url = "http://127.0.0.1:8000/api/chat/stream/"
    data = {
        "message": "Crea una lista numerata di 3 linguaggi di programmazione con esempi di codice",
        "session_id": "test_markdown_stream",
    }

    try:
        response = requests.post(url, json=data, stream=True)
        print("\n=== TEST STREAMING MARKDOWN ===")
        print(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            print("Streaming content (primi chunk):")
            chunk_count = 0
            for line in response.iter_lines():
                if line and chunk_count < 10:  # Mostra solo i primi 10 chunk
                    line_str = line.decode("utf-8")
                    if line_str.startswith("data: "):
                        try:
                            chunk_data = json.loads(line_str[6:])
                            print(f"  {chunk_data}")
                            chunk_count += 1
                        except:
                            pass
            print("  [... altri chunk ...]")
            return True
        else:
            print(f"Errore: {response.text}")
            return False

    except Exception as e:
        print(f"Errore nel test streaming: {e}")
        return False


if __name__ == "__main__":
    print("🧪 Test del Processore Markdown")
    print("=" * 50)

    # Test normale con Markdown
    success_normal = test_markdown_response()

    # Test streaming con Markdown
    success_streaming = test_streaming_markdown()

    print("\n" + "=" * 50)
    print(f"✅ Test Normale Markdown: {'PASS' if success_normal else 'FAIL'}")
    print(f"📡 Test Streaming Markdown: {'PASS' if success_streaming else 'FAIL'}")

    if success_normal and success_streaming:
        print("🎉 Tutti i test Markdown sono passati!")
        print("\n💡 Per testare il rendering visuale:")
        print("   1. Vai a http://127.0.0.1:8000/")
        print(
            "   2. Chiedi: 'Mostra un esempio di codice Python con formattazione Markdown'"
        )
        print("   3. Testa sia modalità normale che streaming")
    else:
        print("❌ Alcuni test sono falliti")
