import urllib.request

url = input("Digite a URL: ")

try:
    f = urllib.request.urlopen(url)

    total = 0
    mostrado = 0

    for linha in f:
        linha = linha.decode()
        total += len(linha)

        if mostrado < 3000:
            restante = 3000 - mostrado
            print(linha[:restante], end="")
            mostrado += len(linha[:restante])

    print("\n\nTotal de caracteres:", total)

except:
    print("Erro ao acessar a URL.")