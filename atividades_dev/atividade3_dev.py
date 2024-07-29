import tkinter as tk

produtosLista = []

produtoEmEdicao = None
produtoEmEdicaoIndex = None

janela = tk.Tk()
janela.title("Frente de loja")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

labelAdicionar = tk.Label(janela, text="Adicionar produto")
inputAdicionar = tk.Entry(janela)
labelAdicionar.grid(row=0, column=0, padx=5, pady=5)
inputAdicionar.grid(row=0, column=1, columnspan=8, padx=5, pady=5)


def adicionar():
    produtoAtual = inputAdicionar.get()
    if inputAdicionar.get() == "" or produtosLista.count(produtoAtual) > 0:
        return None
    if produtoAtual:
        global produtoEmEdicao
        global produtoEmEdicaoIndex
        if produtoEmEdicaoIndex != None:
            produtosLista[produtoEmEdicaoIndex] = produtoAtual
            produtoEmEdicao.config(text="- " + produtoAtual)
            inputAdicionar.delete(0, tk.END)
            janela.update()
            produtoEmEdicao = None
            produtoEmEdicaoIndex = None
            return None
        produtosLista.append(produtoAtual)
        index = len(produtosLista) - 1
        inputAdicionar.delete(0, tk.END)  # Limpa o campo de texto
        novoProduto = tk.Label(janela, text="- " + produtoAtual, justify=tk.LEFT, wraplength=200)
        botaoEditar = tk.Button(
            janela, text="✏️", cursor="hand2", font=("Segoe UI Emoji", 8)
        )
        botaoExcluir = tk.Button(
            janela, text="❌", cursor="hand2", font=("Segoe UI Emoji", 8)
        )
        novoProduto.grid(row=index + 1, column=0, columnspan=7, padx=5, pady=5, sticky="w")
        botaoEditar.grid(row=index + 1, column=7, padx=2, pady=5)
        botaoExcluir.grid(row=index + 1, column=8, padx=2, pady=5)

        def excluir():
            novoIndice = produtosLista.index(novoProduto.cget("text")[2:])
            produtosLista.pop(novoIndice)
            novoProduto.destroy()
            botaoEditar.destroy()
            botaoExcluir.destroy()

        def editar():
            global produtoEmEdicao
            global produtoEmEdicaoIndex
            produtoEmEdicao = novoProduto
            produtoEmEdicaoIndex = produtosLista.index(novoProduto.cget("text")[2:])
            inputAdicionar.delete(0, tk.END)
            inputAdicionar.insert(0, produtosLista[produtoEmEdicaoIndex])

        botaoEditar.bind("<Button-1>", lambda e: editar())
        botaoExcluir.bind("<Button-1>", lambda e: excluir())
    else:
        inputAdicionar.focus()


inputAdicionar.bind("<Return>", lambda e: adicionar())

janela.mainloop()
