import tkinter as tk

tarefasLista = []

tarefaEmEdicao = None
tarefaEmEdicaoIndex = None

janela = tk.Tk()
janela.title("Lista de tarefas")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

labelAdicionar = tk.Label(janela, text="Adicionar tarefa")
inputAdicionar = tk.Entry(janela)
labelAdicionar.grid(row=0, column=0, padx=5, pady=5)
inputAdicionar.grid(row=0, column=1, columnspan=8, padx=5, pady=5)


def adicionar():
    tarefaAtual = inputAdicionar.get()
    if inputAdicionar.get() == "" or tarefasLista.count(tarefaAtual) > 0:
        return None
    if tarefaAtual:
        global tarefaEmEdicao
        global tarefaEmEdicaoIndex
        if tarefaEmEdicaoIndex != None:
            tarefasLista[tarefaEmEdicaoIndex] = tarefaAtual
            tarefaEmEdicao.config(text="- " + tarefaAtual)
            inputAdicionar.delete(0, tk.END)
            janela.update()
            tarefaEmEdicao = None
            tarefaEmEdicaoIndex = None
            return None
        tarefasLista.append(tarefaAtual)
        index = len(tarefasLista) - 1
        inputAdicionar.delete(0, tk.END)  # Limpa o campo de texto
        novaTarefa = tk.Label(janela, text="- " + tarefaAtual, justify=tk.LEFT, wraplength=200)
        botaoEditar = tk.Button(
            janela, text="✏️", cursor="hand2", font=("Segoe UI Emoji", 8)
        )
        botaoExcluir = tk.Button(
            janela, text="❌", cursor="hand2", font=("Segoe UI Emoji", 8)
        )
        novaTarefa.grid(row=index + 1, column=0, columnspan=7, padx=5, pady=5, sticky="w")
        botaoEditar.grid(row=index + 1, column=7, padx=2, pady=5)
        botaoExcluir.grid(row=index + 1, column=8, padx=2, pady=5)

        def excluir():
            novoIndice = tarefasLista.index(novaTarefa.cget("text")[2:])
            tarefasLista.pop(novoIndice)
            novaTarefa.destroy()
            botaoEditar.destroy()
            botaoExcluir.destroy()

        def editar():
            global tarefaEmEdicao
            global tarefaEmEdicaoIndex
            tarefaEmEdicao = novaTarefa
            tarefaEmEdicaoIndex = tarefasLista.index(novaTarefa.cget("text")[2:])
            inputAdicionar.delete(0, tk.END)
            inputAdicionar.insert(0, tarefasLista[tarefaEmEdicaoIndex])

        botaoEditar.bind("<Button-1>", lambda e: editar())
        botaoExcluir.bind("<Button-1>", lambda e: excluir())
    else:
        inputAdicionar.focus()


inputAdicionar.bind("<Return>", lambda e: adicionar())

janela.mainloop()
