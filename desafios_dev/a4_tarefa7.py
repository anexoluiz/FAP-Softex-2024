import tkinter as tk

janela = tk.Tk()
janela.title("Peso excedente")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

w = {}
w["label0"] = tk.Label(janela, text="Quilos de pesca:")
w["entry0"] = tk.Entry(janela)
w["result"] = tk.Label(janela, text=" ")

for widget in w.values():
    widget.pack(padx=5, pady=5)

def calcular():
    try:
        if (w["entry0"].get() == ""):
            w["result"].config(text="")
            return
        elif (float(w["entry0"].get()) > 50):
            p = float(w["entry0"].get()) - 50
            v = p * 4
        else:
            p = 0
            v = 0
        w["result"].config(text=f"Excedente: {p:.2f} kg \nMulta: R$ {v:.2f}")
    except ValueError:
        w["result"].config(text="")

w["entry0"].bind("<KeyRelease>", lambda e: calcular())

janela.mainloop()