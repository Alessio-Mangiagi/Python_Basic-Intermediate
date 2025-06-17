'''Fai una richiesta GET a https://httpbin.org/get passando i parametri nome e corso.

Fai una richiesta POST a https://httpbin.org/post passando gli stessi parametri come dati del form.

Fai una richiesta PUT a https://httpbin.org/put passando gli stessi parametri come JSON.

Fai una richiesta PATCH a https://httpbin.org/patch passando solo il parametro corso come JSON.

Fai una richiesta DELETE a https://httpbin.org/delete passando il parametro nome come parametro nella URL.

Per ogni chiamata, stampa:

Lo status code

La URL (se visibile)

I dati ricevuti dal server'''



import requests

# respons = requests.get("https://httpbin.org/get",params = {'nome': 'Alessio', 'corso': 'Informatica'})
# print(respons.status_code)
# print(respons.url)
# print(respons.json())

# nuovo_utente = {"nome": "lucia", "email" :"@gmail.com"}
# respons = requests.post("https://httpbin.org/post",data = nuovo_utente)
# print(respons.status_code)
# print(respons.url)
# print(respons.json())

# utente_aggiornato = { "nome":"lucia", "email":"paperella@gmail.com"}
# respons = requests.put("https://httpbin.org/put",json = utente_aggiornato)
# print(respons.status_code)
# print(respons.url)
# print(respons.json())

# url = "https://httpbin.org/patch"#nelle api fattte bene cambia in questa non funziona
# utente= {"nome":"Paola"}
# respons = requests.patch(url, json = utente)
# print(respons.status_code)
# print(respons.url)
# print(respons.json())

# url = "https://httpbin.org/delete"
# utente = {"nome":"Paola"}
# respons = requests.delete(url, json = utente)
# print(respons.status_code)
# print(respons.url)
# print(respons.json())


#  API di prova per capire le risposte dal server. controllare con api pubbliche!!!