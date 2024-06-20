import tkinter as tk

janela = tk.Tk()
janela.title("Checar sinal")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

w = {}
w["label0"] = tk.Label(janela, text="Digite um número:")
w["entry0"] = tk.Entry(janela)
w["result"] = tk.Label(janela, text="")

for widget in w.values():
    widget.pack(padx=5, pady=5)

def checarSinal(*args):
    try:
        f = float(w["entry0"].get())
        if f > 0:
            r = "positivo"
        elif f < 0:
            r = "negativo"
        else:
            r = "neutro"
        w["result"].config(text=f"Este número é: {r}")
    except ValueError:
        w["result"].config(text="")

w["entry0"].bind("<KeyRelease>", checarSinal)

janela.mainloop()