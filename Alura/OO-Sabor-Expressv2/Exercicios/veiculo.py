class Veiculo:
    def __init__(self, marca, modelo):
        self.marca, self.modelo = marca, modelo
        self._ligado = False

    def __str__(self):
        return f'Veiculo: {self.marca} -> {self.ligado_desligado}'
    
    @property
    def ligado_desligado(self):
        return 'Ligado' if self._ligado else 'Desligado'