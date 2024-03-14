from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.porta = portas

    def __str__(self):
        return super().__str__()