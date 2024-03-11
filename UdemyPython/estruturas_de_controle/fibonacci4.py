# 0 1 2 3 5


def fibonacci(num):  # num -> quantos numeros de fibonacci
    resultado = [0, 1]
    primeiro = 0
    segundo = 1
    for i in range(0,num-2):
        resultado.append(resultado[-1] + resultado[-2])
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(10):
        print(fib, end=', ')
