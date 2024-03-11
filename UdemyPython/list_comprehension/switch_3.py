def get_tipo_dia(dia):
    dias = {
        (1, 7): 'Fim de Semana',
        tuple(range(2, 7)): 'Dia de semana',
    }
    dia_escolhido = (tipo for numeros, tipo in dias.items() if dia in numeros) # VAI SE FODER ENTENDI PORRA NENHUMA
    return next(dia_escolhido, '** dia invalido **') # ENTENDI KARALHOS NENHUM

if __name__ == '__main__':
    for dia in range(0,9):
        print(f'dia:{dia} -> {get_tipo_dia(dia)}')