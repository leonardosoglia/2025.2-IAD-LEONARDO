numeros = []

while True:
    entrada = input("Digite um número: ")

    if entrada.lower() == "pronto":
        break

    try:
        numero = float(entrada)
        numeros.append(numero)
    except:
        print("Entrada Inválida")

if len(numeros) > 0:
    print("Máximo:", max(numeros))
    print("Mínimo:", min(numeros))
else:
    print("Nenhum número válido foi digitado.")
