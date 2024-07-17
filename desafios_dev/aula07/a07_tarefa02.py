import tkinter as tk

janela = tk.Tk()
janela.title("Tabuada")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

label0 = tk.Label(janela, text="Qual número?")
entry0 = tk.Entry(janela)
result = tk.Label(janela, text="\n"*10)
label0.grid(row=0, column=0)
entry0.grid(row=0, column=1)
result.grid(row=1, column=0, columnspan=2)

def atualizar():
    try:
        n = entry0.get()
        if (n == ""):
            return result.config(text="\n"*10)
        n = int(n)
        finalText = ""
        for i in range(1, 11):
            finalText += f"\n{n} x {i} = {n*i}"
        result.config(text=finalText)
    except ValueError:
        result.config(text="")

entry0.bind("<KeyRelease>", lambda event: atualizar())

janela.mainloop()