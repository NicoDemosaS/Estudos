class Carro:
    def __init__(self, max):
        self.velocidade = max
    
    
    def frear(self, x):
        if (self.velocidade - x) < self.velocidade:
            self.velocidade = self.velocidade - x

            if (self.velocidade - x) < 0:
                self.velocidade = 0
        return self.velocidade

    def acelerar(self, x):
        if (self.velocidade + x) < 180:
            self.velocidade = self.velocidade + x

            if (self.velocidade + x) >= 180:
                self.velocidade = 180
        return self.velocidade


if __name__ == '__main__':
    c1 = Carro(95)
    
    print('Acelerando!')
    for _ in range(25):
       print(c1.acelerar(8), end= '-> ')
    
    c2 = Carro(80)

    print("\nFreando!")
    for _ in range(10):
        print(c2.frear(10), end= '-> ')

    # Velocidade Minima 0:
    # Velocidade Maxima 180:




    #for _ in range(10):
        #print(c1.frear(8))    