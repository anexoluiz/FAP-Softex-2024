import tkinter as tk

janela = tk.Tk()
janela.title("Eleição")
janela.resizable(False, False)
janela.attributes("-toolwindow", True)
janela.attributes("-topmost", True)

label0 = tk.Label(janela, text="Qual o número de eleitores?")
entry0 = tk.Entry(janela)
label0.grid(row=0, column=0)
entry0.grid(row=0, column=1)
candidato1 = tk.Button(janela, text="Candidato 1")
candidato2 = tk.Button(janela, text="Candidato 2")
candidato3 = tk.Button(janela, text="Candidato 3")
candidato1.grid(row=1, column=0)
candidato2.grid(row=2, column=0)
candidato3.grid(row=3, column=0)
resultado = tk.Label(janela, text="")
resultado.grid(row=1, rowspan=3, column=1)

votos = [0, 0, 0]
def votar(candidato):
    try:
        n = entry0.get()
        if (n == "" or n == "0"):
            return resultado.config(text="")
        n = int(n)
        if (n < 1):
            return resultado.config(text="")
        votos[candidato] += 1
        if (votos[0] + votos[1] + votos[2] >= n):
            if (votos.count(max(votos)) > 1):
                resultado.config(text="Candidato 1: " + str(votos[0]) + "\nCandidato 2: " + str(votos[1]) + "\nCandidato 3: " + str(votos[2]) + "\n>> Empate <<")
            else:
                resultado.config(text="Candidato 1: " + str(votos[0]) + "\nCandidato 2: " + str(votos[1]) + "\nCandidato 3: " + str(votos[2]) + "\nCandidato " + str(votos.index(max(votos)) + 1) + " venceu")
            for item in [candidato1,candidato2,candidato3,entry0]:
                item.config(state=tk.DISABLED)
        else:
            resultado.config(text="Candidato 1: " + str(votos[0]) + "\nCandidato 2: " + str(votos[1]) + "\nCandidato 3: " + str(votos[2]) + "\n")
    except ValueError:
        resultado.config(text="Número de eleitores inválido")

candidato1.bind("<Button-1>", lambda event: votar(0))
candidato2.bind("<Button-1>", lambda event: votar(1))
candidato3.bind("<Button-1>", lambda event: votar(2))

janela.mainloop()
