import tkinter as tk

janela = tk.Tk()
janela.title("Idade")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

label0 = tk.Label(text="Qual sua idade?")
label0.grid(row=0, column=0, padx=10, pady=5)
entry0 = tk.Entry()
entry0.grid(row=0, column=1, padx=10, pady=5)
label1 = tk.Label(text="")
label1.grid(row=1, columnspan=2, padx=10, pady=5)

def verificar_idade(*args):
    try:
        idade = int(entry0.get())
        if (idade < 12):
            idadeResultado = "Criança"
        elif (idade < 18):
            idadeResultado = "Adolescente"
        else:
            idadeResultado = "Adulto"
        label1.config(text=f"Você é: {idadeResultado}")
    except ValueError:
        label1.config(text="")

entry0.bind("<KeyRelease>", verificar_idade)

janela.mainloop()
