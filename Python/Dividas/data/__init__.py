from os import remove

def criarArquivo(arq = 'LSISTEMA'):
    a = open(arq, 'wt+')
    a.close()
def ExistirArquivo(arq = 'LSISTEMA'):
    try:
        a = open(arq, 'rt')
        a.close()
    except:
        criarArquivo()

def cadastrarArquivo(nome):
    try:
        a = open('LSISTEMA', 'a')
        a.write(f'{nome}\n')
        a.close()
    except:
        print('ERRO AO ESCREVER')

def excluirArquivo():
    try:
        remove('LSISTEMA')
    except:
        print('ERRO AO EXCLUIR ARQUIVO')


def mostrarArquivo():
    try:
        a = open('LSISTEMA', 'rt')
        print(a.read())
        a.close()
    except:
        print('PROBLEMA AO LER ARQUIVO')
