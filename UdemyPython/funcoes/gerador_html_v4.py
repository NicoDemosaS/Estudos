bloco_atrs = ('bloco_id', 'bloco_acesskey')
ul_atrs = ('ul_id', 'ul_style   ')


def get_atrs(informados, suportados):
    return ' '.join(f"{k.split('_')[-1]}='{v}'"
                    for k, v in informados.items() if k in suportados)


def tag_bloco(texto, *args, classe='sucess', inline=False, **novos_atrs):
    # tag = 'span' if inline else 'div'
    atributos = get_atrs(novos_atrs, bloco_atrs)
    if inline == True:
        tag = 'span'
    else:
        tag = 'div'
    # html = texto if not callable(texto) else texto(*args)
    if not callable(texto):
        html = texto
    else:
        html = texto(*args, **novos_atrs)


    return f'<{tag} {atributos}="{classe}">{html}</{tag}>'


def tag_lista(*itens, **novos_atrs):
    #for item in itens:
        #lista.append(''.join(f'<li>{item}</li>'))
    lista = ''.join((f'<li>{item}</li>' for item in itens))
    return f'<ul {get_atrs(novos_atrs, ul_atrs)}>{lista}</ul>'


if __name__ == '__main__':
    # print(tag_bloco('bloco', inline=True))
    # print(tag_bloco(tag_lista('Item1','Item2'),classe='Info'))
    print(tag_bloco(tag_lista, 'Sabado', 'Domingo', classe='info', inline=True,
                    bloco_id='BLABLABLA', taporra_seilamano='NAO SEI??', ul_id='IDD UL'))