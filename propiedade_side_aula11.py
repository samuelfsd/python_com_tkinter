from tkinter import *
#PROPIEDADE SIDE VINCULA UMA EXTREMIDADE A UM COMPONENTE 
janela = Tk()



lb1 = Label(janela,text="RIGTH", bg="white") 
lb2 = Label(janela,text="BOTTOM", bg="white") 
lb3 = Label(janela,text="LEFT", bg="white") 
lb4 = Label(janela,text="TOP", bg="white") 

lb1.pack(side=RIGHT)
lb2.pack(side=BOTTOM)
lb3.pack(side=LEFT)
lb4.pack(side=TOP)

janela["bg"] = "black"
janela.geometry("400x400+200+200")
janela.mainloop()