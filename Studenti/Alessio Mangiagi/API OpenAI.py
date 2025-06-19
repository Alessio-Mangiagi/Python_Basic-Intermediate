from openai import OpenAI
from dotenv import load_dotenv
import os
import logging

load_dotenv()

logging.basicConfig(filename='openai_responses.log', level=logging.INFO, format='%(asctime)s %(message)s')


key = os.getenv("OPENAI_API_KEY")
print(key)
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
)
def genera_testo(promt,max_completion_tokens = 100, temperature=0.7 )  :    
    completion = client.chat.completions.create(
        model="gpt-4.1-nano",
        messages=[
            {"role": "user", "content": "scrivi una poesia con tono ottocentesco, non troncare e rimani nei token"}
        ],  # role può essere "system", "user" o "assistant"
        #limote di token
        #determina la creatività
    )


print(completion.choices[0].message)
print(completion.choices[0].message.content)#risultatostampato aschermo





#sistem = ruolo predetermnato es: pirata
#user = quando poniamo la domanda noi
#assistant = la risposta che ci viene data da lui 

# ChatCompletionMessage(content='Le paperelle sono oggetti simbolo di divertimento e spensieratezza,
# spesso associati ai giochi acquatici e alle decorazioni per bagni o piscine. 
# Sono iconiche per il loro design semplice e colorato, e portano un senso di allegria e nostalgia.
# Molte persone apprezzano le paperelle sia per il loro ruolo ludico che come oggetti decorativi, 
# e sono spesso presenti in scene di relax e momenti di svago. Tu hai una particolare opinione o esperienza con le paperelle?', 
# refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None)
# Le paperelle sono oggetti simbolo di divertimento e spensieratezza, spesso associati ai giochi acquatici 
# e alle decorazioni per bagni o piscine. Sono iconiche per il loro design semplice e colorato, e portano un senso di allegria e nostalgia.
# Molte persone apprezzano le paperelle sia per il loro ruolo ludico che come oggetti decorativi, e sono spesso presenti in scene di relax e momenti di svago. 
# Tu hai una particolare opinione o esperienza con le paperelle?

#risultato 2
# O tu, che tra le ombre del mattino pallido
# sdraiato giaces, tra sogni e memorie sbiadite,
# ascolta il mormorio dolce della brezza leggera,
# che accarezza i fioriti campi della tua dimora.

# Nel silenzio ovattato dell’alba s’innalza il pensiero,
# come farfalla svanente in un cielo ammantar di brina,

#scaricare deepseek r1 7b con oolama

