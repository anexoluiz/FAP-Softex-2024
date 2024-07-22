import tkinter as tk

janela = tk.Tk()
janela.title("Carros")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

l={}
e={}
l['marca'] = tk.Label(janela, text="Marca")
e['marca'] = tk.Entry(janela)
l['modelo'] = tk.Label(janela, text="Modelo")
e['modelo'] = tk.Entry(janela)
l['ano'] = tk.Label(janela, text="Ano")
e['ano'] = tk.Entry(janela)
l['cor'] = tk.Label(janela, text="Cor")
e['cor'] = tk.Entry(janela)

for idx, value in enumerate(l.values()):
    value.grid(row=idx, column=0)
for idx, value in enumerate(e.values()):
    value.grid(row=idx, column=1)


def ligar(button):
    if button["text"] == "OFF":
        button.config(text="ON")
    else:
        button.config(text="OFF")

def remover(frame):
    l.remove(frame)
    for widget in frame.winfo_children():
        widget.destroy()

def inserir():
    if e['marca'].get() == '' or e['modelo'].get() == '' or e['ano'].get() == '' or e['cor'].get() == '':
        return
    newframe = tk.Frame(janela)
    newlabel = tk.Label(newframe, text=f"{e['marca'].get()} {e['modelo'].get()} {e['ano'].get()} {e['cor'].get()}")
    ligarbutton = tk.Button(newframe, text="OFF", command=lambda: ligar(ligarbutton))
    removerbutton = tk.Button(newframe, text="Remover", command=lambda: remover(newframe))
    newlabel.grid(row=0, column=0)
    ligarbutton.grid(row=0, column=1)
    removerbutton.grid(row=0, column=2)
    newframe.grid(row=len(l)+1, column=0, columnspan=2)
    l.append(newframe)
    for entry in e.values():
        entry.delete(0, tk.END)

janela.bind("<Return>", lambda event: inserir())
janela.mainloop()