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
        ong_atual = Ong(k, listagem[k]['Ong'], listagem[k]['Presidente'])
        cad_ongs.append(ong_atual)
def delete_api(url1):
    requests.delete(url1)
    print('Ong deletada com sucesso!')
def gravar_projeto(ong):
    indice = ong.id
    url1 = "https://teste-pi-senac-default-rtdb.firebaseio.com/"+indice+".json"
    requests.patch(url1, json=ong)