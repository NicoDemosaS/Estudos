# Callable quer dizer que é uma algo que pode ser 'CHAMADO" tipo list()
# Entao basicamente é uma função? 

def executar(funcao):
    if callable(funcao):
        funcao()

def bom_dia():
    print('Bom dia')


def buonasera():
    print('Buonasera')


if __name__ == '__main__':
    executar(bom_dia)
    executar(buonasera)