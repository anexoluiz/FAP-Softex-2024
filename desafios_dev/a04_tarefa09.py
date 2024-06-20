import tkinter as tk

janela = tk.Tk()
janela.title("Maior número")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

labels = ["Primeiro", "Segundo"]
w = {}

# Usando grid para colocar label ao lado de entry
for i in range(0, 2):
    w[f"label{i}"] = tk.Label(janela, text=f"{labels[i]} número:")
    w[f"label{i}"].grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
    w[f"entry{i}"] = tk.Entry(janela)
    w[f"entry{i}"].grid(row=i, column=1, padx=10, pady=5)
w["resultado_label"] = tk.Label(janela, text="")
w["resultado_label"].grid(row=len(labels), columnspan=2, padx=10, pady=5)

# Função para atualizar o maior número
def atualizar_maximo(*args):
    try:
        n1 = w["entry0"].get()
        n2 = w["entry1"].get()
        if n1 == "" or n2 == "":
            w["resultado_label"].config(text="")
            return
        w["resultado_label"].config(text=f"O maior número é: {max(float(n1), float(n2)):.2f}")
    except ValueError:
        w["resultado_label"].config(text="")

for i in range(0, 2):
    w[f"entry{i}"].bind("<KeyRelease>", atualizar_maximo)

janela.mainloop()
