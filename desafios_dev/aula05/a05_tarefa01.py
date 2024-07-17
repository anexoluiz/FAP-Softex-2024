import tkinter as tk

janela = tk.Tk()

janela.title("Lista de carros")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

label0 = tk.Label(text="Adicionar carro")
label0.pack()
entry0 = tk.Entry()
entry0.pack()
label1 = tk.Label(text="Lista atual de carros")
label1.pack()
carrosWidgets = []

def remover_carro(x):
    x.widget.destroy()

def adicionar_carro():
    if entry0.get() == "":
        return
    carroAtual = tk.Label(text=entry0.get() + " [ X ]", cursor="hand2")
    entry0.delete(0, tk.END)
    carroAtual.pack()
    carroAtual.bind("<Button-1>", lambda x: remover_carro(x))

entry0.bind("<Return>", lambda x: adicionar_carro())

janela.mainloop()
