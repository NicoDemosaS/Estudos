from data import *
from style import *
from time import sleep
ExistirArquivo()


while True:
    linha()
    print(''' 1 -> CADASTRAR\n 2 -> LISTA\n 3 -> EXCLUIR DIRETORIO\n 4 -> SAIR DO SISTEMA''')
    linha()
    op = int(input('ESCOLHA UM OPÇÃO:'))


    #OPÇÃO 1 CADASTRAR
    if op == 1:
        nome = input('NOME: ')
        cadastrarArquivo(nome)
        continue
    #OPÇÃO 2 VER LISTA
    if op == 2:
        linha()
        mostrarArquivo()
        linha()
        sleep(3)
        continue
    #OPÇÃO 3 EXCLUIR DIRETORIO
    if op == 3:
        print('1 PARA EXCLUIR')
        conf = int(input(': '))
        if conf == 1:
            print('EXCLUINDO DADOS')
            excluirArquivo()
        else:
            print('CONTINUANDO')
            continue
    #OPÇÃO 4 DAR BREAK
    if op == 4:
        break