import tkinter as tk

janela = tk.Tk()
janela.title("Paridade")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

w = {}
w["label1"] = tk.Label(janela, text="Digite um número\ninteiro:")
w["entry1"] = tk.Entry(janela)
w["resultado_label"] = tk.Label(janela, text="")

for widget in w.values():
    widget.pack(padx=10, pady=5)

def atualizar_paridade(*args):
    try:
        n = w["entry1"].get()
        if n == "":
            w["resultado_label"].config(text="")
            return
        n = int(n)
        if n % 2 == 0:
            w["resultado_label"].config(text=f"{n} é par")
        else:
            w["resultado_label"].config(text=f"{n} é ímpar")
    except ValueError:
        w["resultado_label"].config(text="")

w["entry1"].bind("<KeyRelease>", atualizar_paridade)

janela.mainloop()