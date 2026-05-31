# Importa o tkinter 
from tkinter import *
from tkinter import ttk

# cores
cor1 = "#313538" # cinza
cor2 = "#2e424f" # azul acinzentado

# Cria a janela com configurações básicas
janela = Tk()
janela.title("Calculadora")
janela.geometry("470x636")
janela.config(bg = cor1)

# Divide a janela em dois quadros
frame_tela = Frame(janela, width = 470, height = 100, bg = cor2)
frame_tela.grid(row = 0, column = 0)

frame_corpo = Frame(janela, width = 470, height = 536)
frame_corpo.grid(row = 1, column = 0)

janela.mainloop()