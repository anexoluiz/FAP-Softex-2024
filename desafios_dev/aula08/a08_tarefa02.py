import tkinter as tk

janela = tk.Tk()
janela.title("Carros")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

l={}
e={}
l['marca'] = tk.Label(janela, text="Marca")
e['marca'] = tk.Entry(janela)
l['modelo'] = tk.Label(janela, text="Modelo")
e['modelo'] = tk.Entry(janela)
l['ano'] = tk.Label(janela, text="Ano")
e['ano'] = tk.Entry(janela)
l['cor'] = tk.Label(janela, text="Cor")
e['cor'] = tk.Entry(janela)

carros = []

for idx, value in enumerate(l.values()):
    value.grid(row=idx, column=0)
for idx, value in enumerate(e.values()):
    value.grid(row=idx, column=1)
def listener():
    if e['marca'].get() == '' or e['modelo'].get() == '' or e['ano'].get() == '' or e['cor'].get() == '':
        return
    carro = Carro(e['marca'].get(), e['modelo'].get(), e['ano'].get(), e['cor'].get())
    for entry in e.values():
        entry.delete(0, tk.END)

janela.bind("<Return>", lambda event: listener())

class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.frame = tk.Frame(janela)
        self.marca = tk.Label(self.frame, text=marca)
        self.modelo = tk.Label(self.frame, text=modelo)
        self.ano = tk.Label(self.frame, text=ano)
        self.cor = tk.Label(self.frame, text=cor)
        carros.append(self)
        self.ligado = False
        self.botaoligar = tk.Button(self.frame, text="OFF", command=self.ligar)
        self.botaoRemover = tk.Button(self.frame, text="Remover", command=self.remover)
        self.frame.grid(row=len(l)+len(carros), column=0)

    def ligar(self):
        self.ligado = not self.ligado

    def remover(self):
        self.frame.destroy()

janela.mainloop()