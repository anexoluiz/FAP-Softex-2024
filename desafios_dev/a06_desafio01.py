import tkinter as tk

TuplaUFS = ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO')

janela = tk.Tk()
janela.title("Estados Brasileiros")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

label = tk.Label(janela, text="Todos os estados")
label.pack(padx=10, pady=5)
label2 = tk.Label(janela, text="\n".join(TuplaUFS))
label2.pack(padx=10, pady=5)

janela.mainloop()