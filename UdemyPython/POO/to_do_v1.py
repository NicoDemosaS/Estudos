from datetime import datetime

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.data = datetime.now()

    def concluir(self):
        self.feito = True

    def __str__(self):
        return self.descricao + (' (Concluida)' if self.feito else '')    

def main():
    casa = []
    casa.append(Tarefa('Lavar Prato'))
    casa.append(Tarefa('Passar Roupa'))
    casa.append(Tarefa('Lavar Calçada'))

    [tarefa.concluir() for tarefa in casa if tarefa.descricao == 'Lavar Prato']
    for tarefa in casa:
        print(f'{tarefa}')

    #for tarefa in casa:
    #    if tarefa.descricao == 'Lavar Prato':
    #        tarefa.feito = 'Concluido'
    #        print(f'{tarefa.descricao} -> {tarefa.feito}')


if __name__ == '__main__':
    taref1 = Tarefa('Passar Pano')
    main()


