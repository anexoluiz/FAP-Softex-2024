import tkinter as tk

janela = tk.Tk()
janela.title("Salário mensal")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

w = {}
w["label1"] = tk.Label(janela, text="Digite seu salario por hora:")
w["entry1"] = tk.Entry(janela)
w["label2"] = tk.Label(janela, text="Digite as horas trabalhadas:")
w["entry2"] = tk.Entry(janela)
w["resultado_label"] = tk.Label(janela, text="")

for widget in w.values():
    widget.pack(padx=10, pady=5)

def atualizar_salario(*args):
    try:
        s = w["entry1"].get()
        h = w["entry2"].get()
        if s == "" or h == "":
            w["resultado_label"].config(text="")
            return
        total = float(s) * float(h)
        ir = total * 0.11
        inss = total * 0.08
        sindicato = total * 0.05
        w["resultado_label"].config(text=f"+ Salário bruto:\tR$ {total:.2f}\n- IR:\t\tR$ {ir:.2f}\n- INSS:\t\tR$ {inss:.2f}\n- sindicato:\tR$ {sindicato:.2f}\n+ Salário líquido:\tR$ {total - ir - inss - sindicato:.2f}", justify="left")
    except ValueError:
        w["resultado_label"].config(text="")

w["entry1"].bind("<KeyRelease>", atualizar_salario)
w["entry2"].bind("<KeyRelease>", atualizar_salario)

janela.mainloop()