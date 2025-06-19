import openai
import numpy as np
import os

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=["Questa è una frase.", "Questa è un'altra frase."]
)
embeddings = [e.embedding for e in response.data]
print(np.array(embeddings))