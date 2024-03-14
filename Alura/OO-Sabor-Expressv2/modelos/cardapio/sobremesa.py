from modelos.cardapio.item_cardapio import ItemCardapio

class Sobremesa(ItemCardapio):
    def __init__(self, nome, preco, tipo, tamanho):
        super().__init__(nome, preco)
        self.tipo, self.tamanho = tipo, tamanho

    def __str__(self):
        return f'{self.nome} / {self.preco} / {self.tipo} / {self.tamanho}'