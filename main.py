# Importa o tkinter 
from tkinter import *
from tkinter import ttk

# cores
cor1 = "#313538" # cinza
cor2 = "#2e424f" # azul acinzentado
cor3 = "#faf8f7" # branco
cor4 = "#0f0f0f" # preto
cor5 = "#e07204" # laranja
cor6 = "#8a8a8a" # cinza claro
cor7 = "#09759c" # azul

# Cria a janela com configurações básicas
janela = Tk()
janela.title("Calculadora")
janela.geometry("470x636")
janela.config(bg = cor1)

# Divide a janela em dois quadros
frame_tela = Frame(janela, width = 470, height = 135, bg = cor2)
frame_tela.grid(row = 0, column = 0)

frame_corpo = Frame(janela, width = 470, height = 501)
frame_corpo.grid(row = 1, column = 0)

# Cria label
valor_texto = StringVar()
app_label = Label(frame_tela, textvariable=valor_texto, width=18, height=3, padx=40, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 30'), bg=cor2, fg=cor3)
app_label.place(x=0, y=0)

# Define a variavel os valores digitados
valores_digitados = ''

# Cria funcao para aparecer o valores no frame_tela
def entrar_valores(event):
    global valores_digitados
    valores_digitados = valores_digitados + str(event)
    # Passa o valor para tela
    valor_texto.set(valores_digitados)

# Cria funcao para fazer a contas
def calcular():
    global valores_digitados
    valores_digitados = str(eval(valores_digitados))
    valor_texto.set(valores_digitados)

# Cria funcao de limpar tela
def limpar_tela():
    global valores_digitados
    valores_digitados = ''
    valor_texto.set("")

# Cria os botões
b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=32, height=6, bg=cor6, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_corpo, command=lambda:entrar_valores('%'), text="%", width=16, height=6, bg=cor6, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=230, y=0)
b_3 = Button(frame_corpo, command=lambda:entrar_valores('/'), text="/", width=16, height=6, bg=cor5, fg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=350, y=0)

b_4 = Button(frame_corpo, command=lambda:entrar_valores('7'), text="7", width=16, height=6, bg=cor6, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=100)
b_5 = Button(frame_corpo, command=lambda:entrar_valores('8'), text="8", width=16, height=6, bg=cor6, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=115, y=100)
b_6 = Button(frame_corpo, command=lambda:entrar_valores('9'), text="9", width=16, height=6, bg=cor6, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=230, y=100)
b_7 = Button(frame_corpo, command=lambda:entrar_valores('*'), text="*", width=16, height=6, bg=cor5, fg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=350, y=100)

b_8 = Button(frame_corpo, command=lambda:entrar_valores('4'), text="4", width=16, height=6, bg=cor6, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=200)
b_9 = Button(frame_corpo, command=lambda:entrar_valores('5'), text="5", width=16, height=6, bg=cor6, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=115, y=200)
b_10 = Button(frame_corpo, command=lambda:entrar_valores('6'), text="6", width=16, height=6, bg=cor6, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=230, y=200)
b_11 = Button(frame_corpo, command=lambda:entrar_valores('-'), text="-", width=16, height=6, bg=cor5, fg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=350, y=200)

b_12 = Button(frame_corpo, command=lambda:entrar_valores('1'), text="1", width=16, height=6, bg=cor6, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=300)
b_13 = Button(frame_corpo, command=lambda:entrar_valores('2'), text="2", width=16, height=6, bg=cor6, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=115, y=300)
b_14 = Button(frame_corpo, command=lambda:entrar_valores('3'), text="3", width=16, height=6, bg=cor6, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=230, y=300)
b_15 = Button(frame_corpo, command=lambda:entrar_valores('+'), text="+", width=16, height=6, bg=cor5, fg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=350, y=300)

b_16 = Button(frame_corpo, command=lambda:entrar_valores('0'), text="0", width=32, height=6, bg=cor6, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=400)
b_17 = Button(frame_corpo, command=lambda:entrar_valores('.'), text=".", width=16, height=6, bg=cor6, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=230, y=400)
b_18 = Button(frame_corpo, command=calcular, text="=", width=16, height=6, bg=cor7, fg=cor3, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=350, y=400)

janela.mainloop()