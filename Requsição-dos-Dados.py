import requests

with open("C:\\Users\\roger\\Downloads\\Ficha Rogério.pdf", 'rb') as leitor:
    teste_envio = requests.post("https://estudosflask-default-rtdb.firebaseio.com/.json", files={'file': leitor})

print(teste_envio.json())
