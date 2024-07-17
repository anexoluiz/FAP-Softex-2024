import tkinter as tk

janela = tk.Tk()
janela.title("Contagem regressiva")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

label0 = tk.Label(text="Quantos segundos?")
label0.grid(row=0, column=0, padx=10, pady=5)
entry0 = tk.Entry()
entry0.grid(row=0, column=1, padx=10, pady=5)
label1 = tk.Label(text="")
label1.grid(row=1, columnspan=2, padx=10, pady=5)

def contagem_regressiva(*args):
    try:
        segundos = int(entry0.get())
        if segundos < 0:
            label1.config(text="")
            return
        for i in range(segundos, -1, -1):
            if (i == 0):
                label1.config(text="Acabou o tempo!")
                return
            label1.config(text=f"Contagem: {i}")
            janela.update()
            janela.after(1000)
    except ValueError:
        label1.config(text="")
        return

entry0.bind("<KeyRelease>", contagem_regressiva)

janela.mainloop()