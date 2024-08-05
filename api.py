from classes import *
import os
import requests
import json
url = "https://teste-pi-senac-default-rtdb.firebaseio.com/.json"
def busca_api():
    listagem = requests.get(url)
    listagem = listagem.json()
    for k in listagem.keys():
        print(f'Ong: {listagem[k]['Ong']}   -   Presidente: {listagem[k]['Presidente']}')
    # print(listagem)
print("Teste de GitHub")