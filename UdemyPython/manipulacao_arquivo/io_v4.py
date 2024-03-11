
try:
    with open('/home/demosa/Programas/manipulacao_arquivo/dados.csv', 'r') as arquivo:
        with open ('/home/demosa/Programas/manipulacao_arquivo/dados.txt', 'w') as saida:
            for registro in arquivo:
                pessoa = registro.strip().split(',')
                print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)
                # print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))
except Exception as error:
    print(error)
finally:
    arquivo.close()
    saida.close()
