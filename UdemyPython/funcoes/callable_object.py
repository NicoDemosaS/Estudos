class Potencia:
    # Calcula potencia especifica de um numero
    def __init__(self, expoente):
        self.expoente = expoente


    def __call__(self, base):
        return base ** self.expoente
    

if __name__ == '__main__':
    quadrado = Potencia(2)
    cubo = Potencia(3)

    if callable(quadrado) and callable(cubo):
        print(f'quadrado - {quadrado(3)}, cubo - {cubo(5)}')