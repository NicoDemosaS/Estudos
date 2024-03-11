class Livro:

    livros = []
    def __init__(self, nome, autor, data):
        self.nome = nome
        self.autor = autor
        self.data = data
        self.disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'{self.nome} / {self.autor} / {self.data} / {self.disponibilidade}'

    @classmethod
    def verificar_disponibilidade(cls, ano):
        if cls.livros:
            for livro in cls.livros:
                if livro.data == ano:
                    print(f'{livro.nome} / {livro.disponibilidade}')
                else:
                    return print('Nenhum livro encontrado')
            



    @property
    def disponibilidade(self):
        return 'Disponivel' if self.disponivel else 'Indisponivel'

    @property
    def emprestar_livro(self):
        self.disponivel = False

def main():
    Livro('Harry', 'Jk', 1993)
    Livro('Joaquin', 'BLA', 1992)
    Livro('ANITO', 'blo', 1992)

    Livro.verificar_disponibilidade(1990)
    
if __name__ == '__main__':
    main()
    