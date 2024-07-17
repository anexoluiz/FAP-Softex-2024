import tkinter as tk

janela = tk.Tk()
janela.title("Salário mensal")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

w = {}
w["label1"] = tk.Label(janela, text="Digite seu salario atual:")
w["entry1"] = tk.Entry(janela)
w["resultado_label"] = tk.Label(janela, text=" \n \n \n ", justify="left")

for widget in w.values():
    widget.pack(padx=10, pady=5)

def atualizar_salario(*args):
    try:
        s = w["entry1"].get()
        if s == "":
            w["resultado_label"].config(text="")
            return
        elif float(s) <= 280:
            aumento = 0.20
        elif float(s) <= 700:
            aumento = 0.15
        elif float(s) <= 1500:
            aumento = 0.10
        else:
            aumento = 0.05
        aumento_reais = float(s) * aumento
        w["resultado_label"].config(text=f"Salário atual:\tR$ {float(s):.2f}\nAumento(%):\t{aumento * 100:.0f}%\nAumento (reais):\tR$ {aumento_reais:.2f}\nNovo salário:\tR$ {float(s) + aumento_reais:.2f}")
    except ValueError:
         w["resultado_label"].config(text=" \n \n \n ")

w["entry1"].bind("<KeyRelease>", atualizar_salario)

janela.mainloop()