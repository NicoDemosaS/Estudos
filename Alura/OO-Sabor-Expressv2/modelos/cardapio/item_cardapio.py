from abc import ABC, abstractmethod

class ItemCardapio:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    @abstractmethod
    def aplicar_desconto(self, desconto):
        self.preco = self.preco - (self.preco * desconto / 100)