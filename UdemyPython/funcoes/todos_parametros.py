def todos_param(*arg, **kwarg):
    print(f'args {arg}')
    print(f'kwargs {kwarg}')


if __name__ == '__main__':
    todos_param('um', 'dois', False)
    todos_param(primeiro='Nicolas Gabriel', esforçado=True)
    todos_param('Um', 'Dois',[1, 2, 3], primeiro='Nicolas Gabriel', sobrenome='Brunismann')