cont_vogal = 0
cont_consoante = 0

#o programa sempre continua aceitando novas letras até que o usuário digite '#', que encerra o loop.
while True:
    letra = input("Digite uma letra: ")

    #condição para encerrar o loop caso o usuário digite '#'.
    if letra == '#':
        break

    #verifica se a entrada é uma letra, caso contrário, exibe uma mensagem de erro e continua o loop.
    if not letra.isalpha():
        print("Entrada inválida. Digite apenas uma letra.")
        continue

    #verifica se a letra digitada é uma vogal ou consoante, incrementando o contador correspondente.
    #o lower() é usado para garantir que a verificação seja case-insensitive, ou seja, não importa se a letra é maiúscula ou minúscula.
    if letra.lower() in 'aeiou':
        cont_vogal += 1
    else:
        cont_consoante += 1

#ao final, o programa exibe a quantidade de vogais e consoantes digitadas, e informa qual foi digitada em maior quantidade.
print(f"Quantidade de vogais: {cont_vogal}")
print(f"Quantidade de consoantes: {cont_consoante}")


if cont_vogal == cont_consoante:
    print("A quantidade de vogais e consoantes é igual.")
else:
    #o if está dentro do else, para que só seja executado se a quantidade de vogais e consoantes for diferente.
    if cont_vogal > cont_consoante:
        mais = "vogais"
        menos = "consoantes"
    elif cont_consoante > cont_vogal:
        mais = "consoantes"
        menos = "vogais"

    print(f"Foram digitadas mais {mais} do que {menos}.")

