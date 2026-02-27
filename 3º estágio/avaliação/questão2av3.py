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

maior_email = None
maior_contagem = None

for email, contagem in histograma.items():
    if maior_contagem is None or contagem > maior_contagem:
        maior_email = email
        maior_contagem = contagem

print(maior_email, maior_contagem)