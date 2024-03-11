# 0 1 2 3 5


def fibonacci(num):  # num -> quantos numeros de fibonacci
    cont = 0
    a = 0
    b = 1
    while cont != num:
        print(a, end=', ') 
        c = a + b
        a = b
        b = c
        cont = cont + 1

if __name__ == '__main__':
    fibonacci(50)
