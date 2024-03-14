from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Melancia', 12, 'Grande')
prato_paozinho = Prato('Paozinho', 100, 'Melhor paozinho da cidade')
prato_paozinho.aplicar_desconto(30)
sobresa_pudim = Sobremesa('Pudim', 100, 'Doce', 'Pequeno')
Restaurante.adicionar_no_cardapio(restaurante_praca, bebida_suco)
Restaurante.adicionar_no_cardapio(restaurante_praca, prato_paozinho)
Restaurante.adicionar_no_cardapio(restaurante_praca, sobresa_pudim)
sobresa_pudim.aplicar_desconto(25)

def main():
    restaurante_praca.exibir_cardapio

if __name__ == '__main__':
    main()