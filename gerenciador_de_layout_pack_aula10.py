from tkinter import *
#gerenciador pack vai ser implementado nesse código
#PROPIEDADE SIDE DO GERENCIADOR PACK
janela = Tk()

lb1 = Label(janela,text="Label 1",bg="green")
lb2 = Label(janela,text="Label 2",bg="red")
lb3 = Label(janela,text="Label 3",bg="yellow")
lb4 = Label(janela,text="Label 4",bg="blue")

lb1.pack()
lb2.pack()
lb3.pack()
lb4.pack(side=BOTTOM)

janela.geometry("400x400+200+200")
janela.mainloop()
