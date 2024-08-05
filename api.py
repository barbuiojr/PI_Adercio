from classes import *
import os
import requests
import json
cad_ongs = []
url = "https://teste-pi-senac-default-rtdb.firebaseio.com/.json"
def busca_api():
    listagem = requests.get(url)
    listagem = listagem.json()
    for k in listagem.keys():
        print(f'Ong: {listagem[k]['Ong']}\nPresidente: {listagem[k]['Presidente']}')
        ong_atual = Ong(k, listagem[k]['Ong'], listagem[k]['Presidente'])
        cad_ongs.append(ong_atual)
    