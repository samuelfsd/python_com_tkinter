import tkinter as tk #IMPORTANDO BIBLIOTECA E RENOMEANDO PARA tk 

janela = tk.Tk() #ATRIBUINDO A VARIAVEL JANELA A BIBLIOTECA 

janela.title("Janela Principal.") #COLOCAR TITULO USANDO .title 

janela["bg"] = "blue" #ASSIM QUE FAZ PARA MUDAR A COR DE FUNDO DA JANELA pode ser assim: janela["background"] = "green"

janela.geometry("800x300+100+100") #LARGURAxALTURA + ESQUEDA + DIREITA DO VIDEO 

janela.mainloop() #EXECUTANDO A JANLELA 
