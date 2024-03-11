def resultado_f1(primeiro='L.Hamilton',
                 segundo='M. Verstappen',
                 terceiro='S. vettel'):
    print(f'1) - {primeiro}')
    print(f'2) - {segundo}')
    print(f'3) - {terceiro}')


if __name__ == '__main__':
    podium = {
            'primeiro':'L.Carlinhos',
            'segundo':'M. Verstappen',
            'terceiro':'S. vettel'}
    resultado_f1(**podium)