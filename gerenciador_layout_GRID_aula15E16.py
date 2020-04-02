from tkinter import *
#PROPIEDADES ROW E COLUMN

janela = Tk()

lb1 = Label(janela,text="Label 1")
lb2 = Label(janela,text="Label 2")
lb1.grid(row=1,column=1)#PROPIEDADE GRID COM LINHA(ROW) COLUNA(COLUMN)
lb2.grid(row=2,column=2)
janela.geometry("400x400+200+200")
janela.mainloop()