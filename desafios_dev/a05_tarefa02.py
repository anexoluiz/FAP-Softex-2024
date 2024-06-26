import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

label0 = tk.Label(text="Digite os valores")
label0.pack()
label1 = tk.Label(text="+ Somar\n- Subtrair\n* Multiplicar\n/ Dividir", justify="left")
label1.pack()
entry0 = tk.Entry()
entry0.pack()
label1 = tk.Label(text="")
label1.pack()

def calcular(x):
    try:
        resultado = eval(entry0.get())
        label1.config(text=f"Resultado: {resultado}")
    except:
        label1.config(text="")

entry0.bind("<KeyRelease>", lambda x: calcular(x))

janela.mainloop()
