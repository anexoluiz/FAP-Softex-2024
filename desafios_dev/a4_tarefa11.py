import tkinter as tk

janela = tk.Tk()
janela.title("Sinal")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

w = {}
w["label0"] = tk.Label(janela, text="Valor:")
w["entry0"] = tk.Entry(janela)
w["result"] = tk.Label(janela, text=" ")

for widget in w.values():
    widget.pack(padx=5, pady=5)

def sinal():
    try:
        p = w["entry0"].get()
        if p == "":
            w["result"].config(text="")
            return
        elif float(p) > 0:
            sinal = "positivo"
        elif float(p) < 0:
            sinal = "negativo"
        else:
            sinal = "nulo"
        w["result"].config(text=f"Sinal: {sinal}")
    except ValueError:
        w["result"].config(text="")

w["entry0"].bind("<KeyRelease>", lambda e: sinal())

janela.mainloop()