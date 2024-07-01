import tkinter as tk

tarefas = []

tarefaEmEdicao = None
tarefaEmEdicaoIndex = None

janela = tk.Tk()
janela.title("Lista de tarefas")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

label = tk.Label(janela, text="Adicionar tarefa")
entry0 = tk.Entry(janela)
label.grid(row=0, column=0, padx=5, pady=5)
entry0.grid(row=0, column=1, padx=5, pady=5)

def adicionar():
    tarefa = entry0.get()
    if (entry0.get() == ""):
        return None
    if tarefa:
        global tarefaEmEdicao
        global tarefaEmEdicaoIndex
        if (tarefaEmEdicaoIndex != None):
            tarefas[tarefaEmEdicaoIndex] = tarefa
            tarefaEmEdicao.config(text=str(tarefaEmEdicaoIndex+1)+". "+tarefa)
            entry0.delete(0,tk.END)
            janela.update()
            tarefaEmEdicao = None
            tarefaEmEdicaoIndex = None
            return None
        tarefas.append(tarefa)
        index = len(tarefas) - 1
        entry0.delete(0, tk.END)
        label0 = tk.Label(janela, text=str(len(tarefas)) + ". " + tarefa)
        button0 = tk.Button(janela, text="✏️", cursor="hand2")
        button1 = tk.Button(janela, text="❌", cursor="hand2")
        label0.grid(row=index + 1, column=0, padx=5, pady=5)
        button0.grid(row=index + 1, column=1, padx=5, pady=5)
        button1.grid(row=index + 1, column=2, padx=5, pady=5)
        def excluir(index):
            tarefas.pop(index)
            label0.destroy()
            button0.destroy()
            button1.destroy()
        def editar(index):
            global tarefaEmEdicao
            global tarefaEmEdicaoIndex
            tarefaEmEdicao = label0
            tarefaEmEdicaoIndex = index
            entry0.delete(0, tk.END)
            entry0.insert(0, tarefas[index])
        button0.bind("<Button-1>", lambda e: editar(index))
        button1.bind("<Button-1>", lambda e: excluir(index))
    else:
        entry0.focus()

entry0.bind("<Return>", lambda e: adicionar())
    
janela.mainloop()