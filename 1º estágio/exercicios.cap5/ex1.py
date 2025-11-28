soma = 0
quantidade = 0

while True:
    entrada = input("Digite um número: ")

    if entrada.lower() == "pronto":
        break

    try:
        numero = float(entrada)
        soma += numero
        quantidade += 1
    except:
        print("Entrada Inválida")

if quantidade > 0:
    media = soma / quantidade
    print(soma, quantidade, media)
else:
    print("Nenhum número válido foi digitado.")
