# Implementação livre
iteracao = 1

posicao = int(input("Digite uma posição de parada da sequencia fibonacci: "))
limite = int(input("Digite um limite para a sequencia fibonacci: "))

#primeiro laço de repetição para calcular o valor da posição desejada na sequência de Fibonacci.
while iteracao <= posicao:
    if iteracao == 1:
        valor_posicao = 1
    elif iteracao == 2:
        valor_posicao = 1

        numero_anterior = 1
        numero_antant = 1
    else:
        valor_posicao = numero_anterior + numero_antant

        numero_antant = numero_anterior
        numero_anterior = valor_posicao


    iteracao += 1

print(f"Valor da posição {posicao} da sequencia fibonacci: {valor_posicao}")

#segundo laço de repetição para exibir cada valor da sequência de Fibonacci, até o limite máximo.
iteracao = 1
while iteracao <= limite:
    if iteracao == 1:
        valor_posicao = 1
    elif iteracao == 2:
        valor_posicao = 1

        numero_anterior = 1
        numero_antant = 1
    else:
        valor_posicao = numero_anterior + numero_antant

        numero_antant = numero_anterior
        numero_anterior = valor_posicao

    print(f"Valor da posição atual da sequencia fibonacci: {valor_posicao}")
    iteracao += 1