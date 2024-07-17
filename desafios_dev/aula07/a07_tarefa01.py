import tkinter as tk
import a07_funcoes as f

janela = tk.Tk()
janela.title("Calculadora")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

grid1 = {}
grid2 = {}
grid3 = {}
operation = tk.StringVar()
grid1["radiosoma"] = tk.Radiobutton(janela, text="Soma", value="soma", variable=operation)
grid1["radiosub"] = tk.Radiobutton(janela, text="Subtração", value="sub", variable=operation)
grid1["radiomult"] = tk.Radiobutton(janela, text="Multiplicação", value="mult", variable=operation)
grid1["radiodiv"] = tk.Radiobutton(janela, text="Divisão", value="div", variable=operation)
grid2["num1entry"] = tk.Entry(janela)
grid2["num2entry"] = tk.Entry(janela)
grid3["resulttext"] = tk.Label(janela, text="Resultado: ")
grid3["resultvalue"] = tk.Label(janela, text="")

def calcular(*args):
    n1 = grid2["num1entry"].get()
    n2 = grid2["num2entry"].get()
    op = operation.get()
    if (n1 == '' or n2 == ''):
        return
    opEscolhida = getattr(f, op)
    result = opEscolhida(float(n1), float(n2))
    grid3["resultvalue"].config(text=result)

for idx, value in enumerate(grid1.values()):
    value.config(command=calcular)
    value.grid(row=0, column=idx)

for idx, value in enumerate(grid2.values()):
    value.grid(row=1, column=idx*2, columnspan=2)

for idx, value in enumerate(grid3.values()):
    value.grid(row=2, column=idx*2, columnspan=2)

grid1["radiosoma"].select()

for item in grid2.values():
    item.bind("<KeyRelease>", calcular)

janela.mainloop()