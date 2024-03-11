# 0 1 2 3 5


def fibonacci(num):  # num -> quantos numeros de fibonacci
    resultado = [0, 1]
    while True:
        resultado.append(sum(resultado[-2:]))
        if len(resultado) == num:
            break
        #resultado.append(sum(resultado[-1], resultado[-2]))
    return resultado


if __name__ == '__main__':
    for fib in fibonacci(10):
        print(fib, end=', ')
