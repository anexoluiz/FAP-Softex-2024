import tkinter as tk

janela = tk.Tk()
janela.title("Peso ideal")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

def calcular(*args):
    try:
        h = float(entry0.get())
        if sexo.get() == 1:
            p = (72.7 * h) - 58
        else:
            p = (62.1 * h) - 44.7
        resultado.config(text=f"Peso ideal: {p:.2f}")
    except ValueError:
        resultado.config(text="")


label0 = tk.Label(janela, text="Sexo:")
label0.grid(row=0, column=0, padx=5, pady=5)

sexo = tk.IntVar()
radio1 = tk.Radiobutton(janela, text="Masculino", value=1, variable=sexo, command=calcular)
radio1.grid(row=0, column=1, padx=5, pady=5)
radio1.select()

radio2 = tk.Radiobutton(janela, text="Feminino", value=0, variable=sexo, command=calcular)
radio2.grid(row=0, column=2, padx=5, pady=5)

label1 = tk.Label(janela, text="Altura:")
label1.grid(row=1, column=0, padx=5, pady=5)

entry0 = tk.Entry(janela)
entry0.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

resultado = tk.Label(janela, text=" ")
resultado.grid(row=2, columnspan=3, padx=5, pady=5)

entry0.bind("<KeyRelease>", calcular)

janela.mainloop()
