import tkinter as tk

janela = tk.Tk()
janela.title("Soma de dois números")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

w = {}
w["label1"] = tk.Label(janela, text="Digite o primeiro número:")
w["entry1"] = tk.Entry(janela)
w["label2"] = tk.Label(janela, text="Digite o segundo número:")
w["entry2"] = tk.Entry(janela)
w["resultado_label"] = tk.Label(janela, text="")

for widget in w.values():
    widget.pack(padx=10, pady=5)

def atualizar_soma(*args):
    try:
        n1 = w["entry1"].get()
        n2 = w["entry2"].get()
        if n1 == "" or n2 == "":
            w["resultado_label"].config(text="")
            return
        soma = float(n1) + float(n2)
        w["resultado_label"].config(text=f"{n1} + {n2} = {soma:.2f}")
    except ValueError:
        w["resultado_label"].config(text="")

w["entry1"].trace_add("write", atualizar_soma)