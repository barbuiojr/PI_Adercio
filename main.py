from classes import *
from menus import *
from crud import *
from api import *
import os
op = 0
while op != 7:
    op = menu_inicial()
    if op == 1:
        listar_ongs(cad_ongs)
    elif op == 3:
        ong_atual = criar_ong()
        cad_ongs.append(ong_atual)
        print(ong_atual.ong,' criada com sucesso')
    elif op == 4:
        os.system("cls")
        listar_ongs(cad_ongs)
        on = int(input('Escolha a ONG:'))
        criar_projeto(on, cad_ongs)
    elif op == 5:
        busca_api()
        print(cad_ongs)
    elif op == 6:
        listar_ongs(cad_ongs)
        op1 = int(input('Escolha uma ONG para deletar: '))
        print(cad_ongs[op1-1].ong)
        url_1 = cad_ongs[op1-1].id
        deletar_ong(url_1)