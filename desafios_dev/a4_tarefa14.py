import tkinter as tk

janela = tk.Tk()
janela.title("Mais barato")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

labels = ["primeiro", "segundo", "terceiro"]
w = {}

# Usando grid para colocar label ao lado de entry
for i in range(0, 3):
    w[f"label{i}"] = tk.Label(janela, text=f"Custo do {labels[i]} produto:")
    w[f"label{i}"].grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
    w[f"entry{i}"] = tk.Entry(janela)
    w[f"entry{i}"].grid(row=i, column=1, padx=10, pady=5)
w["resultado_label"] = tk.Label(janela, text="")
w["resultado_label"].grid(row=len(labels), columnspan=2, padx=10, pady=5)

# Função para atualizar a media
def escolher_produto(*args):
    try:
        v1 = w["entry0"].get()
        v2 = w["entry1"].get()
        v3 = w["entry2"].get()
        if v1 == "" or v2 == "" or v3 == "":
            w["resultado_label"].config(text="")
            return
        menor = min(float(v1), float(v2), float(v3))
        w["resultado_label"].config(text=f"Escolha o produto de: R$ {menor:.2f}")
    except ValueError:
        w["resultado_label"].config(text="")

for i in range(0, 3):
    w[f"entry{i}"].bind("<KeyRelease>", escolher_produto)

janela.mainloop()
