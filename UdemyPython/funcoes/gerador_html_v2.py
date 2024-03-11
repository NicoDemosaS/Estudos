def tag_bloco(texto, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</div>'

if __name__ == '__main__':
    print(tag_bloco('bloco', inline=True))