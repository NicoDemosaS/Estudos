from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, nome, marca, modelo):
        self.nome, self.marca, self.modelo = nome, marca, modelo
        self.ligado = False
    
    @abstractmethod
    def ligar(self):
        self.ligado = True
