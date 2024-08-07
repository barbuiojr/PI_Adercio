from time import sleep
import os
def menu_inicial():
    print("""1 - Listar ONGS
2 - Listar projetos
3 - Criar ONG
4 - Criar projeto
5 - Editar ONG
6 - Editar Projeto
7 - Deletar ONG
8 - Deletar Projeto
9 - Sair
Escolha uma opçao --->""")
    op = input()
    while not op.isnumeric():
        op = input('Opção inválida.\nVocê deve escolher um número do menu.')
        print(op)
    while int(op)<1 or int(op)>9:
        op = input('Opção inválida\nAs opções disponíveis vão de 1 a 9:')
    os.system("cls")
    return int(op)