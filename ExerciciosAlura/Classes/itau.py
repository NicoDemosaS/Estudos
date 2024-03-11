class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'{self.titular.ljust(10)} ¦ Saldo: {self.saldo} ¦ Estado: {self.estado_conta}'
    
    def alternar_conta(self):
        self._ativo = not self._ativo
        return self._ativo
    
    @property
    def estado_conta(self):
        return 'Ativo' if self._ativo else 'Desativo'


def main():
    Ethan = ContaBancaria('Ethan', 3650)
    print(Ethan)
    Ethan.alternar_conta()
    print(Ethan)

if __name__ == '__main__':
    main()