from tkinter import *

#fazendo uma função para mudar o nome teste depois que o botão for pressionado
def bt_click():
    print("bt_click")

    lb["text"] = "Funcionou!!!"

janela = Tk()

#criando um botão
bt = Button(janela,width=20, text="OK", command=bt_click)
bt.place(x=100,y=100)

#criando um Label 
lb = Label(janela,text="Teste")
lb.place(x=100,y=150)


janela.geometry("300x300+200+200")
janela.mainloop()