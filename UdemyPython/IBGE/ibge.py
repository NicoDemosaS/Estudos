import csv
# Le e printa somente o [4] e [9] da Lista desafio.csv

with open('desafio.csv', 'r', encoding='ISO 8859-1') as entrada:
    arquivo = csv.reader(entrada)
    cont = 0
    for registro in arquivo:
        if cont > 0:
            print(f'{registro[3]} -> {registro[8]}')
        cont = cont + 1
