from classes import *
from menus import *
from crud import *
from api import *
import os
cad_ongs = []
op = 0
while op != 6:
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