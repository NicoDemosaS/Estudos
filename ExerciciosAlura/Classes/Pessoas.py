class Pessoas:
    def __init__(self, nome, idade, profissao):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao

    def __str__(self):
        return f'Nome:{self.nome} / Idade:{self.idade} /Profissao:{self.profissao}'
    
    @property
    def aniversario(self):
        self.idade += 1


    @property
    def saudacao(self):
        print(f'Saudação! {self.profissao}')
    
def main():
    marinheiro = Pessoas('Ethan', 28, 'Marinheiro')
    
    print(marinheiro)
    
    marinheiro.aniversario
    
    print(marinheiro)
    marinheiro.saudacao

if __name__ == '__main__':
    main()