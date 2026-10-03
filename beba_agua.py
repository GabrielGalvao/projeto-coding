"""Lembretes simples para ajudar a manter a hidratação."""

copos_consumidos = 0

# O menu continua aparecendo até a pessoa escolher sair.
while True:
    print("\n=== BEBA ÁGUA ===")
    print("1. Receber lembretes")
    print("2. Registrar copos de água")
    print("3. Sair")
    opcao = input("Escolha uma opção: ")

    #ao escolher a opção 1, o programa solicita a quantidade de lembretes e inicia um loop para mostrar cada lembrete.
    if opcao == "1":
        quantidade = int(input("Quantos lembretes deseja receber? "))
        numero_lembrete = 1

        print("\nLembretes iniciados.")
        # Este laço repete enquanto ainda houver lembretes para mostrar.
        while numero_lembrete <= quantidade:
            input("Pressione Enter para ver o próximo lembrete...")
            print(f"Lembrete {numero_lembrete}: hora de beber água!")
            numero_lembrete += 1

        print("Fim dos lembretes.")
        
    #ao escolher a opção 2, o programa solicita a quantidade de copos consumidos e atualiza o total.
    elif opcao == "2":
        copos = int(input("Quantos copos você bebeu? "))
        copos_consumidos += copos
        print(f"Total registrado: {copos_consumidos} copo(s).")

    #ao escolher a opção 3, o programa termina com o break e uma mensagem de despedida.
    elif opcao == "3":
        print("Até a próxima. Cuide da sua hidratação!")
        break
    else:
        print("Opção inválida. Escolha 1, 2 ou 3.")