import tkinter as tk

janela = tk.Tk()
janela.title("Conversor de temperatura")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

w = {}
w["label0"] = tk.Label(janela, text="Temperatura em Fahrenheit:")
w["entry0"] = tk.Entry(janela)
w["result"] = tk.Label(janela, text=" ")

for widget in w.values():
    widget.pack(padx=5, pady=5)

def converter():
    try:
        f = float(w["entry0"].get())
        c = (f - 32) * 5/9
        w["result"].config(text=f"Valor em Celsius: {c:.2f} °C")
    except ValueError:
        w["result"].config(text="")

w["entry0"].bind("<KeyRelease>", lambda e: converter())

janela.mainloop()