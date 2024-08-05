from classes import *
import os
import requests
import json
url = "https://teste-pi-senac-default-rtdb.firebaseio.com/.json"
def criar_ong():
    id = 25
    ong = input('Digite o nome da ONG: ')
    pres = input('Digite o nome do presidente da ONG: ')
    ong_atual = Ong(id, ong, pres)
    ong_post = {'Ong':ong, 'Presidente':pres}
    print(ong_post)
    requests.post(url, json=ong_post)
    resultado = requests.get(url)
    print(resultado)
    return ong_atual
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
     print(f'Projeto criado com sucesso para a ONG {cad_ongs[on-1].ong}')
     print(f'Nome do projeto: {cad_ongs[on-1].projetos[0].projeto}')
def deletar_ong(url_1):
     urld = "https://teste-pi-senac-default-rtdb.firebaseio.com/"+url_1+".json"
     print(urld)
     requests.delete(urld)
     print('Ong deletada com sucesso!')