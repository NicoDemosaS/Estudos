class Musica:
    def __init__(self, nome, genero, duracao):
        self.nome = nome
        self.genero = genero
        self.duracao = duracao

    def __str__(self):
        return f'''-Nome: {self.nome} -Genero: {self.genero} -Duracao: {self.duracao} '''
    
bohemian = Musica('Bohemian', 'Rock', 355)

print(bohemian)