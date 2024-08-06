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
def gravar_projeto(indc, proj):
    indice = cad_ongs[indc].id
    url1 = "https://teste-pi-senac-default-rtdb.firebaseio.com/"+indice+".json"
    print(url1)
    p = proj.projeto
    d = proj.descricao
    r = proj.responsavel
    s = proj.status
    prjt = {"Projeto":[p,d,r,s]}
    input('Tecle algo para continuar: ')
    requests.patch(url1, json=prjt)