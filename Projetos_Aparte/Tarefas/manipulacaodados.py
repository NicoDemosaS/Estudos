import os
import csv

localcsv = '/home/demosa/Github/Projetos_Aparte/Tarefas/dados.csv' # Local do Arquivo

def criarArquivo():
    with open (localcsv, 'w', ) as dados: # CRIA/ABRE ARQUIVO DADOS.CSV
        if os.path.exists(localcsv): # VERIFICA EXISTENCIA DE DADOS.CSV
            try:
                print('Existencia do arquivo Verificada!')
            except Exception as error:
                print(f'{error} -> erro ao LER/CRIAR arquivo')


def lerArquivo():
    with open(localcsv, 'r') as saida:  # Abre arquivo
        try:
            leitura = csv.reader(saida)  # LE DADOS.CSV
            print('Dados Reconhecidos!')           
        except Exception as error:       # Verifica Erro
            print(f'{error} -> erro ao LER/CRIAR arquivo')
        for texto in leitura:
            print(texto)


def escreverArquivo(informação):
    with open(localcsv, 'a', newline='') as entrada: # Abre arquivo
        entrada.write(informação)


def deletarArquivo():
    os.remove(localcsv)


if __name__ == '__main__':
    criarArquivo()
    #escreverArquivo('asdasd JS\n')
    #lerArquivo()