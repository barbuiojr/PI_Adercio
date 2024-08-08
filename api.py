from classes import *
import requests
#import json
cad_ongs = []
url = "https://teste-pi-senac-default-rtdb.firebaseio.com/.json"
def busca_api():
    listagem = requests.get(url)
    listagem = listagem.json()
    for k in listagem.keys():
        if listagem[k]['Tipo'] == 'ONG':
            ong_atual = Ong(k, listagem[k]['Ong'], listagem[k]['Presidente'])
            cad_ongs.append(ong_atual)
    for k in listagem.keys():
        if listagem[k]['Tipo'] == 'projeto':
            p = listagem[k]['Título']
            id = listagem[k]['ID']
            d = listagem[k]['Descrição']
            r = listagem[k]['Responsável']
            s = listagem[k]['Status']
            proj_atual = Projeto(k, p, d, r, s)
            for o in cad_ongs:
                if o.id == id:
                    o.projetos.append(proj_atual)
def delete_api(url1):
    requests.delete(url1)
    print('Registro deletado com sucesso!')

def gravar_projeto(cod, tit, d, r, s):
    proj_atual = {"Tipo":"projeto", "ID":cod, "Título":tit, "Descrição":d, "Responsável":r, "Status":s}
    requests.post(url, json=proj_atual)
    cad_ongs.clear()
    busca_api()

def edit_api(url1, n, p):
    urledit = "https://teste-pi-senac-default-rtdb.firebaseio.com/"+url1+".json"
    ong_edit = {"Ong":n, "Presidente":p}
    requests.patch(urledit, json=ong_edit)
    cad_ongs.clear()
    busca_api()