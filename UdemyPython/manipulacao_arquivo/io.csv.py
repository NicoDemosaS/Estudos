import csv

with open('dados.csv') as entrada:
    for registro in csv.reader(entrada):
        print(registro)