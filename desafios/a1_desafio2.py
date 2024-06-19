import tkinter as tk
from tkinter import messagebox


def atualizar_soma(*args):
    try:
        n1 = int(entry1.get()) if entry1.get() else 0
        n2 = int(entry2.get()) if entry2.get() else 0
        if not entry1.get() or not entry2.get():
            # Colocar uma mensagem para digitar as notas se tiver um nome
            if entry0.get():
                return resultado_label.config(text="Digita suas notas, " + entry0.get())
            return resultado_label.config(text="")
        # Caso não tenha nome mas tenha as notas, pedir para digitar o nome
        if not entry0.get():
            return resultado_label.config(text="Digita seu nome logo acima?")
        média = (n1 + n2) / 2
        return resultado_label.config(
            text=f"A sua primeira nota é: {n1}\na segunda é: {n2}\ne a média é: {média}"
        )
    except ValueError:
        resultado_label.config(text="Por favor, insira notas válidos.")


root = tk.Tk()
root.title("Média das notas")

# Desativando o resize e o maximize
root.resizable(False, False)
root.attributes("-toolwindow", True)
root.attributes("-topmost", True)  # Sempre no topo por que não tem icone na taskbar

# Criar os elementos da janela
label0 = tk.Label(root, text="Como você se chama?")
entry0 = tk.Entry(root)
label1 = tk.Label(root, text="Digite a primeira nota")
entry1 = tk.Entry(root)
label2 = tk.Label(root, text="Digite a segunda nota")
entry2 = tk.Entry(root)
resultado_label = tk.Label(root, text="")

# Juntar todos os elementos em um array
widgets = [label0, entry0, label1, entry1, label2, entry2, resultado_label]

# Empacotar todos com margens para melhorar a visualização
for widget in widgets:
    widget.pack(padx=10, pady=5)

# Adicionar keyup para atualizar a soma enquanto digita os valores
# mas no nome foi só um onblur para não atualizar a cada letra
entry0.bind("<FocusOut>", atualizar_soma)
entry1.bind("<KeyRelease>", atualizar_soma)
entry2.bind("<KeyRelease>", atualizar_soma)

root.mainloop()
