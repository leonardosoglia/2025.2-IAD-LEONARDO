nome_arquivo = input("Enter a file name: ")

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

print(histograma)