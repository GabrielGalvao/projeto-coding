
## Sempre continua aceitando novas turmas até que o usuário decida sair.
while True:
    nome_turma = input("Digite o nome da turma: ")
    nome_disciplina = input("Digite o nome da disciplina: ")
    qtd_alunos = int(input("Digite a quantidade de alunos: "))

    cont = 1
    soma_notas = 0

    #Verificando se a nota do aluno está entre 0 e 10, caso contrário, solicita novamente.
    while cont <= qtd_alunos:
        nota_aluno = float(input(f"Digite a nota do aluno {cont}: "))
        if not (nota_aluno < 0 or nota_aluno > 10):
            soma_notas += nota_aluno
            cont += 1
        else:
            print("Nota inválida. Digite uma nota entre 0 e 10.")

    #calculando a média da turma
    media_turma = soma_notas / qtd_alunos

    #determinando a mensagem de acordo com a média da turma
    if media_turma >= 7:
        status = "Turma bem avaliada"
    elif media_turma >= 5:
        status = "Turma em situação de alerta"
    else:
        status = "Turma precisa de intervenção"

    #relatório final da turma com nome da turma, quantidade de alunos, disciplina, média e mensagem.
    print(f"A média da turma {nome_turma} de {qtd_alunos} alunos na disciplina {nome_disciplina} é: {media_turma:.2f}. {status}")

    sair = input("Deseja sair? (s/n): ")
    
    #convertendo a resposta para minúscula e verificando se é 's' para sair do loop, caso contrário, continua o loop.
    if sair.lower() == 's':
        print("Saindo...")
        break
    else:
        print("Continuando...")