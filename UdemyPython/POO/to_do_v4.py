from datetime import datetime, timedelta

class Projetos:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    def __iter__(self):
        return self.tarefas.__iter__()

    def add(self, descricao, vencimento=None):
        self.tarefas.append(Tarefa(descricao, vencimento))

    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]
    
    def procurar(self, descricao):
        return [tarefa for tarefa in self.tarefas
         if tarefa.descricao == descricao][0]
        
    def __str__(self):
        return f'{self.nome} , {len(self.pendentes())} tarefas(s) pendentes'


class Tarefa:
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.data = datetime.now()
        self.vencimento = vencimento

    def concluir(self):
        self.feito = True

    def __str__(self):
        status = []
        if self.feito:
            self.descricao = self.descricao + ' (Concluido)'
        elif self.vencimento:
            if self.vencimento < datetime.now():
                status.append('(VENCIDO)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vencendo em {dias} dias)')
        return f'{self.descricao} '+ ' '.join(status)

class TarefaRecorrente(Tarefa):
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(self.dias)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)
    
def main():
    casa = Projetos('Tarefas de Casa')
    casa.tarefas.append(TarefaRecorrente('Passar Pano', datetime.now))
    casa.tarefas.append(casa.procurar('Passar Pano').concluir())
    for tarefa in casa: 
        print(tarefa)

if __name__ == '__main__':
    main()


