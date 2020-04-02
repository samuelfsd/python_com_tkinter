from tkinter import *
#gerenciador de leiaut 
janela = Tk()
lb = Label(janela,text="Fala Galera!!!") #janela é o contenier e o texto é após
lb.place(x=100,y=100) #dimensões de onde vai ficar escrito o que eu digitei na linha anterior 

janela.title("Janela Principal.")

janela.geometry("300x300+200+200")


janela.mainloop()