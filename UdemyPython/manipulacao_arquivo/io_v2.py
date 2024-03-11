

arquivo = open('/home/demosa/Programas/manipulacao_arquivo/dados.csv', 'r')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.split(',')),end='')
arquivo.close()