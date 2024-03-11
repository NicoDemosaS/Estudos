# Programa aonde DADA EQUAÇÃO Y=A.BX.C 
# O PROGRAMA NOS DE OS VALORES DE Y E X

def equacao1(numMaximodeX, a=2, b=3 , c=4):
    for x in range(0, numMaximodeX+1):
        equacao = (a* x) * b + c
        y = equacao
        print(f'Para x: {x}, y: {y}')

if __name__ == '__main__':
    equacao1(10, 3, 5, 3)
    # X ATE 10
