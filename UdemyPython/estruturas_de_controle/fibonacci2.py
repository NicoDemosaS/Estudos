# 0 1 2 3 5


def fibonacci(num):  # num -> quantos numeros de fibonacci
    contador = 0
    primeiro = 0
    segundo = 1
    while contador != num:
        print(primeiro, end=', ') 
        terceiro = primeiro + segundo
        primeiro = segundo
        segundo = terceiro
        contador = contador + 1

if __name__ == '__main__':
    fibonacci(50)
