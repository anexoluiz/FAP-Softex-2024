import tkinter as tk

TuplaUFS = ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO')
ListaUFS = []

janela = tk.Tk()
janela.title("Estados Brasileiros")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

label = tk.Label(janela, text="Adicionar estado")
label.pack(padx=10, pady=5)
entry0 = tk.Entry(janela)
entry0.pack(padx=10, pady=5)
label2 = tk.Label(janela, text="Estados adicionados")
label2.pack(padx=10, pady=5)

def adicionar():
    if (entry0.get() in ListaUFS):
        return label.config(text="Estado já adicionado")
    elif (entry0.get() not in TuplaUFS):
        return label.config(text="Estado inválido")
    ListaUFS.append(entry0.get())
    label3 = tk.Label(janela, text="[X] "+entry0.get(), justify='left', cursor='hand2')
    label3.pack(padx=10, pady=0)
    entry0.delete(0, tk.END)
    def deletethis():
        currentUf = label3.cget("text")[-2:]
        ListaUFS.remove(currentUf)
        label3.destroy()
    label3.bind("<Button-1>", lambda x: deletethis())

entry0.bind("<Return>", lambda x: adicionar())

janela.mainloop()