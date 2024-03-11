

arquivo = open('/home/demosa/Programas/manipulacao_arquivo/dados.csv', 'r')
leitor = arquivo.read()
for linha in leitor.splitlines():
    print('Nome: {} Idade: {}'.format(*linha.split(',')))

