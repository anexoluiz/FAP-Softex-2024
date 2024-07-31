import tkinter as tk

produtosPorLoja = {"Loja A": [], "Loja B": [], "Loja C": []}
estoquePorLoja = {"Loja A": [], "Loja B": [], "Loja C": []}

produtoEmEdicao = None
produtoEmEdicaoIndex = None

janela = tk.Tk()
janela.title("Frente de loja")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)


labelProduto = tk.Label(janela, text="Produto: ")
labelProduto.grid(row=0, column=0, padx=5, pady=5)
inputProduto = tk.Entry(janela)
inputProduto.grid(row=0, column=1, columnspan=6, padx=5, pady=5)

labelEstoque = tk.Label(janela, text="Estoque: ")
labelEstoque.grid(row=1, column=0, padx=5, pady=5)
inputEstoque = tk.Entry(janela)
inputEstoque.grid(row=1, column=1, columnspan=6, padx=5, pady=5)

variavelLoja = tk.StringVar(janela)
variavelLoja.set("Loja A")
menuLoja = tk.OptionMenu(janela, variavelLoja, *produtosPorLoja.keys())
menuLoja.grid(row=0, rowspan=2, column=7, columnspan=2, padx=5, pady=5)

def atualizar_exibicao_produtos(tk_janela):
    global produtoEmEdicao, produtoEmEdicaoIndex
    produtoEmEdicao = None
    produtoEmEdicaoIndex = None
    for widget in tk_janela.winfo_children():
        if widget not in [labelProduto, labelEstoque, inputProduto, inputEstoque, menuLoja]:
            widget.destroy() 

    lojaAtual = variavelLoja.get()
    for index, produto in enumerate(produtosPorLoja[lojaAtual]):
        produto_label = tk.Label(tk_janela, text=f"- {produto} (Estoque: {estoquePorLoja[lojaAtual][index]})", justify=tk.LEFT, wraplength=400)
        editar_button = tk.Button(tk_janela, text="✏️", cursor="hand2", font=("Segoe UI Emoji", 8))
        excluir_button = tk.Button(tk_janela, text="❌", cursor="hand2", font=("Segoe UI Emoji", 8))

        produto_label.grid(row=index + 2, column=0, columnspan=7, padx=5, pady=5, sticky="w")
        editar_button.grid(row=index + 2, column=7, padx=1, pady=5)
        excluir_button.grid(row=index + 2, column=8, padx=1, pady=5)

        editar_button.bind("<Button-1>", lambda e, prod=produto: iniciar_edicao(prod, tk_janela))
        excluir_button.bind("<Button-1>", lambda e, prod=produto: excluir_produto(prod, tk_janela))

def iniciar_edicao(produto, root):
    global produtoEmEdicao, produtoEmEdicaoIndex
    lojaAtual = variavelLoja.get()
    produtoEmEdicao = produto
    produtoEmEdicaoIndex = produtosPorLoja[lojaAtual].index(produto)

    inputProduto.delete(0, tk.END)
    inputProduto.insert(0, produto)
    inputEstoque.delete(0, tk.END)
    inputEstoque.insert(0, estoquePorLoja[lojaAtual][produtoEmEdicaoIndex])

def excluir_produto(produto, root):
    lojaAtual = variavelLoja.get()
    index = produtosPorLoja[lojaAtual].index(produto)
    produtosPorLoja[lojaAtual].pop(index)
    estoquePorLoja[lojaAtual].pop(index)
    atualizar_exibicao_produtos(root)

def adicionar_ou_editar(event):
    global produtoEmEdicao, produtoEmEdicaoIndex

    produtoAtual = inputProduto.get().strip()
    estoqueAtual = inputEstoque.get().strip()
    lojaAtual = variavelLoja.get()

    if not produtoAtual or not estoqueAtual:
        return

    if produtoEmEdicao:
        produtosPorLoja[lojaAtual][produtoEmEdicaoIndex] = produtoAtual
        estoquePorLoja[lojaAtual][produtoEmEdicaoIndex] = estoqueAtual
        produtoEmEdicao = None
        produtoEmEdicaoIndex = None
    elif produtoAtual in produtosPorLoja[lojaAtual]:
        index = produtosPorLoja[lojaAtual].index(produtoAtual)
        estoquePorLoja[lojaAtual][index] = estoqueAtual
    else:
        produtosPorLoja[lojaAtual].append(produtoAtual)
        estoquePorLoja[lojaAtual].append(estoqueAtual)

    inputProduto.delete(0, tk.END)
    inputEstoque.delete(0, tk.END)
    atualizar_exibicao_produtos(janela)

inputProduto.bind("<Return>", adicionar_ou_editar)
inputEstoque.bind("<Return>", adicionar_ou_editar)
variavelLoja.trace_add("write", lambda *args: atualizar_exibicao_produtos(janela))

janela.mainloop()
