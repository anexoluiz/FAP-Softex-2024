import tkinter as tk
from tkinter import messagebox
import re


def calcular_imc(*args):
    try:
        nome = entry1.get()
        whatsapp_unformatted = re.sub(r"\D", "", entry2.get())
        if not entry1.get() or not entry2.get() or not entry3.get() or not entry4.get():
            return resultado_label.config(text="Preenche todos os campos.")
        elif not nome or not nome.isalpha():
            return resultado_label.config(
                text="Coloca um nome válido com pelo menos uma letra."
            )
        elif (len(whatsapp_unformatted) < 10) or (len(whatsapp_unformatted) > 11):
            return resultado_label.config(text="Coloca o WhatsApp com DDD e telefone")
        whatsapp = f"+55 ({whatsapp_unformatted[:2]}) {whatsapp_unformatted[2:len(whatsapp_unformatted)-4]}-{whatsapp_unformatted[len(whatsapp_unformatted)-4:]}"
        peso = float(entry3.get().replace(",", ".")) if entry3.get() else 0
        altura = float(entry4.get().replace(",", ".")) if entry4.get() else 0
        imc = peso / (altura**2)
        if imc < 18.5:
            nivel = "Abaixo do peso"
        elif imc < 24.9:
            nivel = "Peso normal"
        elif imc < 29.9:
            nivel = "Sobrepeso"
        elif imc < 34.9:
            nivel = "Obesidade grau 1 (leve)"
        elif imc < 39.9:
            nivel = "Obesidade grau 2 (moderada)"
        else:
            nivel = "Obesidade grau 3 (mórbida)"
        consumo = peso * 35
        resultado = (
            f"Nome:\t\t\t{nome}\n"
            f"WhatsApp:\t\t{whatsapp}\n"
            f"Peso:\t\t\t{peso:.2f} kg\n"
            f"Altura:\t\t\t{altura:.2f} m\n"
            f"Consumo de água diário:\t{consumo/1e3:.2f} L\n"
            f"IMC:\t\t\t{imc:.2f}\n"
            f"Nível de obesidade:\t{nivel}"
        )
        return messagebox.showinfo("Resultado", resultado)
    except ValueError:
        resultado_label.config(text="O peso e a altura tem que ser números.")
    except ZeroDivisionError:
        resultado_label.config(text="Coloca uma altura maior que 0")
    except Exception as e:
        resultado_label.config(text=f"Erro não mapeado: {e}")


def sair(*args):
    sair_text = "Aperte ESC novamente para sair."
    if resultado_label.cget("text") == sair_text:
        root.quit()
    resultado_label.config(text=sair_text)


root = tk.Tk()
root.title("Cálculo de IMC")
root.bind("<Return>", calcular_imc)  # Calcular com Enter
root.bind("<Escape>", sair)  # Sair com 2x ESC
root.bind(
    "<KeyPress>", lambda e: resultado_label.config(text="")
)  # Limpar as mensagens ao digitar

# Desativando o resize e o maximize
root.resizable(False, False)
root.attributes("-toolwindow", True)
root.attributes("-topmost", True)  # Sempre no topo por que não tem icone na taskbar

# Criar os elementos da janela
label1 = tk.Label(root, text="Como você se chama?")
entry1 = tk.Entry(root)
label2 = tk.Label(root, text="Qual seu WhatsApp?")
entry2 = tk.Entry(root)
label3 = tk.Label(root, text="Quantos quilos você pesa?")
entry3 = tk.Entry(root)
label4 = tk.Label(root, text="Qual sua altura em metros?")
entry4 = tk.Entry(root)

# Botão para calcular o IMC
button = tk.Button(root, text="Calcular IMC", command=calcular_imc)
resultado_label = tk.Label(root, text="")

# Juntar os labels e entries em arrays
widgets_labels = [label1, label2, label3, label4]
widgets_entries = [entry1, entry2, entry3, entry4]

# Empacotar em cada linha label ao lado do entry em cada uma linha
for i in range(4):
    widgets_labels[i].grid(row=i, column=0, padx=10, pady=5)
    widgets_entries[i].grid(row=i, column=1, padx=10, pady=5)
button.grid(row=4, column=0, columnspan=2, padx=10, pady=5)
resultado_label.grid(row=5, column=0, columnspan=2, padx=10, pady=5)

root.mainloop()
