from banco import Banco

class Agencia(Banco):
    def __init__(self, nome, endereco, numero):
        self.nome, self.endereco = nome, endereco
        super().__init__(self.nome, self.endereco)