import json

import requests


# Test dell'endpoint normale
def test_normal_chat():
    url = "http://127.0.0.1:8000/api/chat/"
    data = {
        "message": "Ciao, come stai?",
        "session_id": "test_session",
        "streaming": False,
    }

    try:
        response = requests.post(url, json=data)
        print("=== TEST MODALITÀ NORMALE ===")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        print()
        return response.status_code == 200
    except Exception as e:
        print(f"Errore nel test normale: {e}")
        return False


# Test dell'endpoint streaming
def test_streaming_chat():
    url = "http://127.0.0.1:8000/api/chat/stream/"
    data = {
        "message": "Raccontami una breve storia",
        "session_id": "test_session_stream",
    }

    try:
        response = requests.post(url, json=data, stream=True)
        print("=== TEST MODALITÀ STREAMING ===")
        print(f"Status Code: {response.status_code}")
        print(f"Headers: {dict(response.headers)}")

        if response.status_code == 200:
            print("Chunk ricevuti:")
            for line in response.iter_lines():
                if line:
                    line_str = line.decode("utf-8")
                    if line_str.startswith("data: "):
                        try:
                            chunk_data = json.loads(line_str[6:])
                            print(f"  {chunk_data}")
                        except:
                            print(f"  Raw: {line_str}")
        print()
        return response.status_code == 200
    except Exception as e:
        print(f"Errore nel test streaming: {e}")
        return False


if __name__ == "__main__":
    print("🧪 Test delle API del Chatbot")
    print("=" * 40)

    # Testa modalità normale
    success_normal = test_normal_chat()

    # Testa modalità streaming
    success_streaming = test_streaming_chat()

    print("=" * 40)
    print(f"✅ Test Normale: {'PASS' if success_normal else 'FAIL'}")
    print(f"📡 Test Streaming: {'PASS' if success_streaming else 'FAIL'}")

    if success_normal and success_streaming:
        print("🎉 Tutti i test sono passati!")
    else:
        print("❌ Alcuni test sono falliti")
