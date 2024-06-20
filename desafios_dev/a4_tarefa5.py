import tkinter as tk

janela = tk.Tk()
janela.title("Peso ideal")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

w = {}
w["label0"] = tk.Label(janela, text="Altura:")
w["entry0"] = tk.Entry(janela)
w["result"] = tk.Label(janela, text=" ")

for widget in w.values():
    widget.pack(padx=5, pady=5)

def converter():
    try:
        h = float(w["entry0"].get())
        p = (72.7 * h) - 58
        w["result"].config(text=f"Peso ideal: {p:.2f} kg")
    except ValueError:
        w["result"].config(text="")

w["entry0"].bind("<KeyRelease>", lambda e: converter())

janela.mainloop()