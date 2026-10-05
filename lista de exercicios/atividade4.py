print("=== CAMPO MINADO ===")

# O administrador cria o nome e a senha para acessar a configuração.
nome_administrador = input("Nome do administrador: ")
senha_administrador = input("Crie uma senha: ")
tentativas = 0
acesso_liberado = False

# O login termina quando a senha estiver certa ou as três tentativas acabarem.
while True:
	senha_digitada = input("Digite a senha do administrador: ")
	if senha_digitada == senha_administrador:
		acesso_liberado = True
		print(f"Bem-vindo, {nome_administrador}!")
		break
	else:
		tentativas += 1
		print(f"Senha incorreta. Tentativa {tentativas} de 3.")	
		if tentativas == 3:
			print("O programa será encerrado.")
			break

if acesso_liberado:
	# A dificuldade define se serão cadastradas três ou cinco bombas.
	dificuldade = input("Escolha a dificuldade (facil ou dificil): ").lower()
	while dificuldade != "facil" and dificuldade != "dificil":
		print("Digite facil ou dificil.")
		dificuldade = input("Escolha a dificuldade: ").lower()

	if dificuldade == "facil":
		quantidade_bombas = 3
	else:
		quantidade_bombas = 5

	# Cada bomba fica guardada em uma variável.
	bomba1 = -1
	bomba2 = -1
	bomba3 = -1
	bomba4 = -1
	bomba5 = -1
	bombas_cadastradas = 0

	# Pedimos posições válidas e não aceitamos uma posição repetida.
	while bombas_cadastradas < quantidade_bombas:
		posicao = input(f"Posição da bomba {bombas_cadastradas + 1} (1 a 15): ")
		if not posicao.isdigit():
			print("Digite um número inteiro.")
		else:
			posicao = int(posicao)
			if posicao < 1 or posicao > 15:
				print("A posição deve estar entre 1 e 15.")
			elif (posicao == bomba1 or posicao == bomba2 or posicao == bomba3
				  or posicao == bomba4 or posicao == bomba5):
				print("Essa posição já foi usada.")
			else:
				if bombas_cadastradas == 0:
					bomba1 = posicao
				elif bombas_cadastradas == 1:
					bomba2 = posicao
				elif bombas_cadastradas == 2:
					bomba3 = posicao
				elif bombas_cadastradas == 3:
					bomba4 = posicao
				else:
					bomba5 = posicao
				bombas_cadastradas += 1

	# Limpamos a tela para os jogadores não verem as posições das bombas.
	print("\n" * 50)

	# Pedimos os nomes e começamos a pontuação de cada jogador em zero.
	jogador1 = input("Nome do Jogador 1: ")
	jogador2 = input("Nome do Jogador 2: ")
	pontos_jogador1 = 0
	pontos_jogador2 = 0
	total_palpite = 0
	vez_jogador1 = True
	partida_acabou = False
	vencedor = ""
	motivo_vitoria = ""

	# A partida continua enquanto ninguém explodir e ninguém fizer três pontos.
	while (not partida_acabou and pontos_jogador1 < 3
		   and pontos_jogador2 < 3):
		if vez_jogador1:
			jogador_atual = jogador1
		else:
			jogador_atual = jogador2

		palpite = input(f"{jogador_atual}, escolha uma posição (1 a 15): ")
		if not palpite.isdigit():
			print("Digite um número inteiro.")
			continue

		palpite = int(palpite)
		if palpite < 1 or palpite > 15:
			print("A posição deve estar entre 1 e 15.")
			continue

		total_palpite += 1
		if (palpite == bomba1 or palpite == bomba2 or palpite == bomba3
				or palpite == bomba4 or palpite == bomba5):
			print(f"Explosão! {jogador_atual} encontrou uma bomba.")
			partida_acabou = True
			if vez_jogador1:
				vencedor = jogador2
			else:
				vencedor = jogador1
			motivo_vitoria = "porque o adversário explodiu"
		else:
			# Cada palpite seguro dá um ponto para o jogador da vez.
			if vez_jogador1:
				pontos_jogador1 += 1
				print(f"Ponto seguro! {jogador1}: {pontos_jogador1}/3.")
			else:
				pontos_jogador2 += 1
				print(f"Ponto seguro! {jogador2}: {pontos_jogador2}/3.")

			# Avisamos se uma bomba estiver uma posição antes ou depois.
			if (palpite - 1 == bomba1 or palpite + 1 == bomba1
					or palpite - 1 == bomba2 or palpite + 1 == bomba2
					or palpite - 1 == bomba3 or palpite + 1 == bomba3
					or palpite - 1 == bomba4 or palpite + 1 == bomba4
					or palpite - 1 == bomba5 or palpite + 1 == bomba5):
				print("Cuidado, você está perto de uma bomba!")

			# Depois de um palpite seguro, o outro jogador recebe a vez.
			vez_jogador1 = not vez_jogador1

	# Se ninguém explodiu, vence quem atingiu três pontos.
	if motivo_vitoria == "":
		motivo_vitoria = "por atingir 3 palpites seguros"
		if pontos_jogador1 == 3:
			vencedor = jogador1
		else:
			vencedor = jogador2

	# Mostramos o vencedor e quantos palpites foram feitos.
	print("\n=== FIM DE JOGO ===")
	print(f"Vencedor: {vencedor}, {motivo_vitoria}.")
	print(f"Total de palpites: {total_palpite}.")
