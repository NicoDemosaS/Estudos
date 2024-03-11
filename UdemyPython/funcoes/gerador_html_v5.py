def tag_bloco(texto, *args, classe='sucess', inline=False):
    # tag = 'span' if inline else 'div'
    if inline == True:
        tag = 'span'
    else:
        tag = 'div'
    # html = texto if not callable(texto) else texto(*args)
    if not callable(texto):
        html = texto
    else:
        html = texto(*args)

    return f'<{tag} class="{classe}">{html}</{tag}>'


def tag_lista(*itens):
    #for item in itens:
        #lista.append(''.join(f'<li>{item}</li>'))
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul>{lista}</ul>'


if __name__ == '__main__':
    # print(tag_bloco('bloco', inline=True))
    # print(tag_bloco(tag_lista('Item1','Item2'),classe='Info'))
    print(tag_bloco(tag_lista, 'Sabado', 'Domingo', classe='info', inline=True))