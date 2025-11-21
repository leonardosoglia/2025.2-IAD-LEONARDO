try:
    horas = float(input("Digite as horas trabalhadas: "))
    taxa = float(input("Digite a taxa horária: "))
except:
    print("Erro, por favor utilize uma entrada numérica")
    quit()

if horas > 40:
    horas_extras = horas - 40
    pagamento = (40 * taxa) + (horas_extras * taxa * 1.5)
else:
    pagamento = horas * taxa

print("Pagamento:", pagamento)