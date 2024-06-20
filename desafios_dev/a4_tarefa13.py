import tkinter as tk

janela = tk.Tk()
janela.title("Média")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

labels = ["Primeira", "Segunda"]
w = {}

# Usando grid para colocar label ao lado de entry
for i in range(0, 2):
    w[f"label{i}"] = tk.Label(janela, text=f"{labels[i]} nota:")
    w[f"label{i}"].grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
    w[f"entry{i}"] = tk.Entry(janela)
    w[f"entry{i}"].grid(row=i, column=1, padx=10, pady=5)
w["resultado_label"] = tk.Label(janela, text=" \n ", justify="left")
w["resultado_label"].grid(row=len(labels), columnspan=2, padx=10, pady=5)

# Função para atualizar a média
def atualizar_media(*args):
    try:
        n1 = w["entry0"].get()
        n2 = w["entry1"].get()
        if n1 == "" or n2 == "":
            w["resultado_label"].config(text=" \n ")
            return
        media = (float(n1) + float(n2)) / 2
        mensagem = "Aprovado com distinção" if media == 10 else ("Aprovado" if media >= 7 else "Reprovado")
        w["resultado_label"].config(text=f"Média: {media:.2f}\nSituação: {mensagem}")
    except ValueError:
        w["resultado_label"].config(text=" \n ")

for i in range(0, 2):
    w[f"entry{i}"].bind("<KeyRelease>", atualizar_media)

janela.mainloop()