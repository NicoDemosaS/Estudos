
try:
    arquivo = open('/home/demosa/Programas/manipulacao_arquivo/dados.csv', 'r')
    
    for registro in arquivo:
         print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
except:
    print('ERRO!')
finally:
    arquivo.close()
