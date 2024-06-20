import tkinter as tk

janela = tk.Tk()
janela.title("Metros para centímetros")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

w = {}
w["label0"] = tk.Label(janela, text="Valor em metros:")
w["entry0"] = tk.Entry(janela)
w["result"] = tk.Label(janela, text=" ")

for widget in w.values():
    widget.pack(padx=10, pady=5)

def converter():
    try:
        m = float(w["entry0"].get())
        cm = m * 100
        w["result"].config(text=f"Resultado: {cm:.2f} cm")
    except ValueError:
        w["result"].config(text="")

w["entry0"].bind("<KeyRelease>", lambda e: converter())

janela.mainloop()