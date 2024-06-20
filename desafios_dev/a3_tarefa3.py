import tkinter as tk

janela = tk.Tk()
janela.title("Maior de 3")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

labels = ["Primeiro número:", "Segundo número:", "Terceiro número:"]
w = {}

# Usando grid para colocar label ao lado de entry
for i in range(0, 3):
    w[f"label{i}"] = tk.Label(janela, text=labels[i])
    w[f"label{i}"].grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
    w[f"entry{i}"] = tk.Entry(janela)
    w[f"entry{i}"].grid(row=i, column=1, padx=10, pady=5)
w["resultado_label"] = tk.Label(janela, text="")
w["resultado_label"].grid(row=len(labels), columnspan=2, padx=10, pady=5)

# Função para atualizar o maior número
def atualizar_maior(*args):
    try:
        n1 = w["entry0"].get()
        n2 = w["entry1"].get()
        n3 = w["entry2"].get()
        if n1 == "" or n2 == "" or n3 == "":
            w["resultado_label"].config(text="")
            return
        maior = max(float(n1), float(n2), float(n3))
        w["resultado_label"].config(text=f"O maior número é {maior}")
    except ValueError:
        w["resultado_label"].config(text="")

for i in range(0, 3):
    w[f"entry{i}"].bind("<KeyRelease>", atualizar_maior)

janela.mainloop()
