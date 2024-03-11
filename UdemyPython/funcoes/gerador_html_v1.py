def tag_bloco(texto, classe='sucess'):
    return f'<div class="{classe}">{texto}</div>'

if __name__ == '__main__':
    # Testes (Assertion) Verifica a condição, se nao for verdadeiro dá erro!
    assert tag_bloco('Incluido com sucesso!') == \
        '<div class="sucess">Incluido com sucesso!</div>'
    assert tag_bloco('Teste', 'asser') == \
        '<div class="asser">Teste</div>'