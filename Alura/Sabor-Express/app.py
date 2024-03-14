import os

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

restaurantes = [{'Nome':'Pizza','Categoria':'Italiano','Ativo':False},
                {'Nome':'Cantina','Categoria':'Padrao','Ativo':False}]

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def exibir_titulo(texto):
    print(texto)
    print(len(texto) * '-')

def cadastrar_novo_restaurante():
    os.system('clear')
    exibir_titulo('Cadastrando novo Restaurante')
    nome_restaurante = input('Nome do restaurante: ')    
    categoria_restaurante = input('Categoria: ')
    dados_do_restaurante = {'Nome':nome_restaurante, 'Categoria':categoria_restaurante, 'Ativo':False}
    
    restaurantes.append(dados_do_restaurante)
    
    print(f'Restaurante: {nome_restaurante} com Categoria: {categoria_restaurante} cadastrado com SUCESSO!\n')
    input('\nDigite algo pra confirmar: ')
    
    main()

def listar_restaurante():
    os.system('clear')
    exibir_titulo('Listando os Restaurantes\n')
    print(f"{'Nome do Restaurante'.ljust(23)} / {'Categoria'.ljust(20)} /{' Estado'}")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['Nome']
        categoria_restaurante = restaurante['Categoria']
        ativo_restaurante = 'ativado' if restaurante['Ativo'] else 'desativado'
        print(f'-{nome_restaurante.ljust(22)} / {categoria_restaurante.ljust(20)} / {ativo_restaurante.ljust(20)}')
    
    input('\nDigite algo para confirmar')
    main()

def alternar_restaurante():
    exibir_titulo('Alternando restaurante')
    
    nome_restaurante = input('Nome do restaurante:')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['Nome']:
            restaurante_encontrado = True
            restaurante['Ativo'] = not restaurante['Ativo']
    if not restaurante_encontrado:
        print(f'{nome_restaurante} nao encontrado')

    mensagem = f'{nome_restaurante} foi ativado com sucesso' if restaurante['Ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
    print(mensagem)

    input('\nDigite para confirmar')
    main()

def finalizar_app():
    os.system('clear') 
    print('Finalizando o app')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1: 
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2: 
            listar_restaurante()
        elif opcao_escolhida == 3: 
            alternar_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
    
    except Exception as erro:
        print(f'Opção Invalida {erro}')

def main():
    os.system('clear')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()
