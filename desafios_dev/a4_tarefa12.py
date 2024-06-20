import tkinter as tk

janela = tk.Tk()
janela.title("Sexo")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

w = {}
w["label0"] = tk.Label(janela, text="Sexo:")
w["entry0"] = tk.Entry(janela)
w["result"] = tk.Label(janela, text=" ")

for widget in w.values():
    widget.pack(padx=5, pady=5)

def validarSexo():
    try:
        s = w["entry0"].get()
        if s == "M" or s == "m":
            sexo = "Masculino"
        elif s == "F" or s == "f":
            sexo = "Feminino"
        else:
            w["result"].config(text="")
            return
        w["result"].config(text=f"Sexo: {sexo}")
    except ValueError:
        w["result"].config(text="")

w["entry0"].bind("<KeyRelease>", lambda e: validarSexo())

janela.mainloop()