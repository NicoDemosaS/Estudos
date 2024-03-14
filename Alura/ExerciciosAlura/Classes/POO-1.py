class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_doppio = Restaurante()
restaurante_doppio.nome = 'Doppio'
restaurante_doppio.categoria = 'Italiana'

nome_doppio = restaurante_doppio.nome 
categoria_doppio = restaurante_doppio.categoria

categoria = 'Bistro'

if restaurante_doppio.ativo:
    print(f'O restaurante {nome_doppio} - {categoria} esta ATIVO!')
else:
    print(f'O restaurante {nome_doppio} - {categoria} esta INATIVO')

restaurante_pizza = Restaurante()

restaurante_pizza.nome = 'Pizza'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

print(f'Restaurante {restaurante_pizza.nome} -> Ativo: {restaurante_pizza.ativo}')