from time import sleep
import os
def menu_inicial():
    print("""1 - Listar ONGS
2 - Listar projetos
3 - Criar ONG
4 - Criar projeto
5 - Buscar ONGs no banco de dados
6 - Deletar ONG
7 - Sair
Escolha uma opçao --->""")
    op = input()
    while not op.isnumeric():
        op = input('Opção inválida.\nVocê deve escolher um número do menu.')
        print(op)
    while int(op)<1 or int(op)>7:
        op = input('Opção inválida\nAs opções disponíveis vão de 1 a 7:')
    os.system("cls")
    return int(op)