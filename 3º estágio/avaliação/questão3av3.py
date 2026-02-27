nome_arquivo = input("Digite o nome do arquivo: ")

try:
    arquivo = open(nome_arquivo)
except:
    print("Arquivo não encontrado:", nome_arquivo)
    exit()

histograma = dict()

for linha in arquivo:
    if linha.startswith("From "):
        palavras = linha.split()
        email = palavras[1]
        histograma[email] = histograma.get(email, 0) + 1

lista_tuplas = list()

for email, contagem in histograma.items():
    lista_tuplas.append((contagem, email))

lista_tuplas.sort(reverse=True)

print(lista_tuplas[0][1], lista_tuplas[0][0])