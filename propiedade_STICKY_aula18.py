from tkinter import *

janela = Tk()

lb1 = Label(janela,text="ESPAÇO", width="15",height=3, bg="blue")#whidth(largura) height(comprimento)
lbHORIZONTAL = Label(janela,text="HORIZONTAL",bg="yellow")
lbVERTICAL = Label(janela,text="VERTICAL",bg="yellow")


lb1.grid(row=0,column=0)
lbHORIZONTAL.grid(row=1,column=0,sticky=E)#UTILIZANDO A PROPIEDADE STICKY
lbVERTICAL.grid(row=0,column=1,sticky=S)


janela.geometry("200x100+100+100")

janela.mainloop()