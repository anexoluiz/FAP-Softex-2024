import tkinter as tk
from tkinter import messagebox


def atualizar_soma(*args):
    try:
        n1 = int(entry1.get()) if entry1.get() else 0
        n2 = int(entry2.get()) if entry2.get() else 0
        if not entry1.get() or not entry2.get():
            # Deixar o texto falando sobre a soma oculto se não tiver algum dos valores
            return resultado_label.config(text="")
        soma = n1 + n2
        return resultado_label.config(text=f"A soma dos números é: {soma}")
    except ValueError:
        resultado_label.config(text="Por favor, insira números válidos.")


root = tk.Tk()
root.title("Soma de dois números")

# Desativando o resize e o maximize
root.resizable(False, False)
root.attributes("-toolwindow", True)

# Criar os elementos da janela
label1 = tk.Label(root, text="Digite o primeiro número:")
entry1 = tk.Entry(root)
label2 = tk.Label(root, text="Digite o segundo número:")
entry2 = tk.Entry(root)
resultado_label = tk.Label(root, text="")

# Juntar todos os elementos em um array
widgets = [label1, entry1, label2, entry2, resultado_label]

# Empacotar todos com margens para melhorar a visualização
for widget in widgets:
    widget.pack(padx=10, pady=5)

# Adicionar keyup para atualizar a soma enquanto digita
entry1.bind("<KeyRelease>", atualizar_soma)
entry2.bind("<KeyRelease>", atualizar_soma)

root.mainloop()
