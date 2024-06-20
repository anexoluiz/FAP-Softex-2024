import tkinter as tk

janela = tk.Tk()
janela.title("Média de anual")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

labels = ["Primeira", "Segunda", "Terceira", "Quarta"]
w = {}

# Usando grid para colocar label ao lado de entry
for i in range(0, 4):
    w[f"label{i}"] = tk.Label(janela, text=f"{labels[i]} nota:")
    w[f"label{i}"].grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
    w[f"entry{i}"] = tk.Entry(janela)
    w[f"entry{i}"].grid(row=i, column=1, padx=10, pady=5)
w["resultado_label"] = tk.Label(janela, text="")
w["resultado_label"].grid(row=len(labels), columnspan=2, padx=10, pady=5)

# Função para atualizar o maior número
def atualizar_media(*args):
    try:
        n1 = w["entry0"].get()
        n2 = w["entry1"].get()
        n3 = w["entry2"].get()
        n4 = w["entry3"].get()
        if n1 == "" or n2 == "" or n3 == "" or n4 == "":
            w["resultado_label"].config(text="")
            return
        media = (float(n1) + float(n2) + float(n3) + float(n4)) / 4
        w["resultado_label"].config(text=f"Média: {media:.1f}")
    except ValueError:
        w["resultado_label"].config(text="")

for i in range(0, 4):
    w[f"entry{i}"].bind("<KeyRelease>", atualizar_media)

janela.mainloop()
