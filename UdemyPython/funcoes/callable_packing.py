def calc_preco_final(preco_bruto, calc_imposto, *params):
    return preco_bruto + preco_bruto * calc_imposto(*params)


def calcularImpostox(importado):
    return 0.22 if importado else 0.13

def calcularImpostoy(explosivo, fator_mult=1):
    return 0.11 * fator_mult if explosivo else 0

if __name__ == '__main__':
    preco_bruto = 134.98
    preco_final = calc_preco_final(preco_bruto, calcularImpostox, True)
    print(preco_final)
    # preco_final = calc_preco_final(preco_final, calcularImpostoy, True, 1.5)
    #print(f'preço final sera {preco_final}')
