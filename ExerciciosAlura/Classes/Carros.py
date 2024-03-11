class Carro:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

    def __str__(self):
        return f'-{self.modelo} / {self.cor} / {self.ano}'
    
nissan = Carro('Nissan', 'Cinza', 1998)
print(nissan)
        