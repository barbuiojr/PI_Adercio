from classes import *
from menus import *
from crud import *
from api import *
import os
op = 0
busca_api()
os.system("cls")
while op != 9:
    op = menu_inicial()
    if op == 1:
        listar_ongs(cad_ongs)
    elif op == 2:
        listar_projetos(100)
    elif op == 3:
        criar_ong()
        indice = len(cad_ongs)-1
        print(cad_ongs[indice].ong, ' criada com sucesso')
    elif op == 4:
        os.system("cls")
        listar_ongs(cad_ongs)
        op1 = int(input('Escolha a ONG:'))
        if op1 > len(cad_ongs):
            print('Opção inválida')
        else:
            criar_projeto(op1, cad_ongs)
    elif op == 5:
        pass
    elif op == 7:
        listar_ongs(cad_ongs)
        op1 = int(input('Escolha uma ONG para deletar: '))
        if op1 > len(cad_ongs):
            print('Opção inválida')
        else:
            if len(cad_ongs[op1-1].projetos) != 0:
                print('Existem projetos cadastrados para essa ONG\nOs projetos deverão ser deletados primeiro.')
                print(f'{len(cad_ongs[op1-1].projetos)} projetos cadastrados')
            else:
                print(cad_ongs[op1-1].ong)
                url_1 = cad_ongs[op1-1].id
                deletar_ong(url_1)
        sleep(2.5)
        os.system("cls")
    elif op == 8:
        listar_ongs(cad_ongs)
        op1 = int(input('Escolha a ONG: '))
        listar_projetos(op1-1)