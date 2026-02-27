import re

nome_arquivo = input("Digite o nome do arquivo: ")

try:
    arquivo = open(nome_arquivo)
except:
    print("Arquivo não encontrado:", nome_arquivo)
    exit()

soma = 0
contador = 0

for linha in arquivo:
    numeros = re.findall('^New Revision: ([0-9]+)', linha)
    if len(numeros) > 0:
        soma = soma + float(numeros[0])
        contador = contador + 1

if contador > 0:
    media = soma / contador
    print(media)