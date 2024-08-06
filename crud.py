from classes import *
import os
import requests
import json
from api import *
url = "https://teste-pi-senac-default-rtdb.firebaseio.com/.json"
def criar_ong():
    ong = input('Digite o nome da ONG: ')
    pres = input('Digite o nome do presidente da ONG: ')
    ong_post = {'Tipo':'ONG','Ong':ong, 'Presidente':pres}
    requests.post(url, json=ong_post)
    cad_ongs.clear()
    busca_api()
def listar_ongs(cad_ongs):
     c = 0
     os.system("cls")
     print(30*'-')
     print('Ongs Cadastradas')
     print(30*'_')
     for entidade in cad_ongs:
          c +=1
          print(f'{c} - {entidade.ong}')
     print(30*'_')
def criar_projeto(on, cad_ongs):
     os.system("cls")
     tit = input('Digite o nome do projeto: ')
     d = input('Descreva o projeto: ')
     r = input('Digite o nome do responsável pelo projeto: ')
     s = input('Informe a situação do projeto: ')
     proj_atual = Projeto(tit, d, r, s)
     cad_ongs[on-1].projetos.append(proj_atual)
     print(cad_ongs[on-1].id)
     a = input('Tecle algo para continuar')
     print(f'Projeto criado com sucesso para a ONG {cad_ongs[on-1].ong}')
     print(f'Nome do projeto: {cad_ongs[on-1].projetos[0].projeto}')
     gravar_projeto(on-1, proj_atual)
def deletar_ong(url_1):
     urld = "https://teste-pi-senac-default-rtdb.firebaseio.com/"+url_1+".json"
     delete_api(urld)
     cad_ongs.clear()
     busca_api()
     