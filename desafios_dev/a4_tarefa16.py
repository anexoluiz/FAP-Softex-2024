import random

membros = ['João', 'Maria', 'José', 'Ana', 'Carlos', 'Paula']
tarefas = ['Analisar requisitos', 'Desenvolver código', 'Testar aplicação', 'Documentar', 'Implantar', 'Manter', 'Revisar código', 'Reunião', 'Treinamento', 'Estudar', 'Pesquisar', 'Revisar documentação']

def sortear_tarefas():
    for i in range(0, len(tarefas)):
        print(f'{membros[random.randint(0,len(membros)-1)]} -> {tarefas[i]}')

sortear_tarefas()