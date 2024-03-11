def log(funcao):
    def decorator(*args, **kwargs):
        print('Decorator')
        resultado = funcao(*args, **kwargs)
        print('Final decorator')
        return resultado
    return decorator


@log
def soma(x, y):
    print(x + y)


soma(4, 5)