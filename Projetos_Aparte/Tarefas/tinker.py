from tkinter import *
from funcoes import criarArquivo

janela = Tk()

janela.title('Tarefas')

texto_orientacao = Label(janela, text= 'Teste para Sistema de Managment de ARQUIVOS!')
texto_orientacao.grid(column=0, row=0)

botao = Button(janela, text='Criar Arquivo', command=criarArquivo)
botao.grid(column=0, row=1)
janela.mainloop()   