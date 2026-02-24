import urllib.request

url = input("Digite a URL: ")

try:
    f = urllib.request.urlopen(url)
    html = f.read().decode()

    contador = html.lower().count("<p")

    print("Quantidade de parágrafos:", contador)

except:
    print("Erro ao acessar a URL.")