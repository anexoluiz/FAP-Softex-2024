import tkinter as tk

janela = tk.Tk()
janela.title("Tempo estimado")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

w = {}
w["label1"] = tk.Label(janela, text="Tamanho do arquivo (MB):")
w["entry1"] = tk.Entry(janela)
w["label2"] = tk.Label(janela, text="Velocidade da rede (Mbps):")
w["entry2"] = tk.Entry(janela)
w["resultado_label"] = tk.Label(janela, text="")

for widget in w.values():
    widget.pack(padx=10, pady=5)

def calcular_tempo(*args):
    try:
        size = w["entry1"].get()
        speed = w["entry2"].get()
        if size == "" or speed == "":
            w["resultado_label"].config(text="")
            return
        minutes = (float(size) * 8) / float(speed) / 60
        seconds = (minutes - int(minutes)) * 60
        w["resultado_label"].config(text=f"Tempo: {minutes:.0f} min {seconds:.0f} seg")
    except ValueError:
        w["resultado_label"].config(text="")

w["entry1"].bind("<KeyRelease>", calcular_tempo)
w["entry2"].bind("<KeyRelease>", calcular_tempo)

janela.mainloop()