import json
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

# --- 1. DADOS DE PRODUÇÃO ---
# Dados extraídos da questão, padronizando os nomes das linhas 
dados_producao_raw = """
LinhaA 120
LinhaB 150
LinhaA 130
LinhaC 90
LinhaB 160
LinhaA 110
"""

# Processamento da string de dados para uma lista de tuplas
registros = []
for linha in dados_producao_raw.strip().split('\n'):
    nome, valor = linha.split()
    registros.append((nome, int(valor)))

# TAREFA 1: Calcule a produção total de cada linha
producao_por_linha = {} 
for nome, valor in registros:
    producao_por_linha[nome] = producao_por_linha.get(nome, 0) + valor

# Tarefa 2: Calcule a produção total geral e a média de produção por registro 
total_geral = sum(producao_por_linha.values())
media_por_registro = total_geral / len(registros)

# Tarefa 3: Identifique a linha com maior produção acumulada 
linha_maior_producao = max(producao_por_linha, key=producao_por_linha.get)

# Tarefa 4: Crie a função classifica_producao(total) 
def classifica_producao(total):
    if total >= 350:
        return "Alta"
    elif 200 <= total < 350:
        return "Média"
    else:
        return "Baixa"

# Tarefa 5: Aplique essa função à produção total de cada linha 
classificacao_linhas = {linha: classifica_producao(total) for linha, total in producao_por_linha.items()}


# --- 2. TRECHO HTML ---
html_doc = """
<html>
<body>
<p>Supervisor responsável: Carla Mendes</p>
<a href="http://fabrica.com/relatorio">Relatório diário</a>
</body>
</html>
""" 

# Tarefa 6: Extraia, do trecho HTML, o nome do supervisor responsável 
soup = BeautifulSoup(html_doc, 'html.parser')
texto_paragrafo = soup.find('p').text
supervisor = texto_paragrafo.replace("Supervisor responsável: ", "")

# Tarefa 7: Vantagem de usar BeautifulSoup em vez de expressão regular para HTML 
# COMENTÁRIO: 
# O BeautifulSoup cria uma árvore de análise estruturada (parse tree) para a página.
# Diferente de expressões regulares, que tratam o HTML como um texto simples e 
# podem falhar facilmente se houver quebras de linha ou mudanças de formatação, 
# o BeautifulSoup consegue navegar pelas tags de forma robusta e sem erros de parsing.


# --- 3. DADOS EM JSON ---
json_data = '''
{
"setor": "Usinagem",
"meta_diaria": 400,
"paradas": 3,
"tempo_parado": 42.5
}
''' 

# Tarefa 8: Converta o JSON em estrutura Python e imprima as informações 
dados_json = json.loads(json_data)
setor = dados_json["setor"]
meta_diaria = dados_json["meta_diaria"]
tempo_parado = dados_json["tempo_parado"]
print("--- TAREFA 8: Dados JSON ---")
print(f"Setor: {setor} | Meta Diária: {meta_diaria} | Tempo Parado: {tempo_parado}\n")

# Tarefa 9: Calcule o percentual da produção total geral em relação à meta diária 
percentual_meta = (total_geral / meta_diaria) * 100


# --- 4. DADOS EM XML ---
xml_data = '''
<dados>
<linhas>
<linha>
<nome>LinhaA</nome>
<eficiencia>92.5</eficiencia>
</linha>
<linha>
<nome>LinhaB</nome>
<eficiencia>88</eficiencia>
</linha>
<linha>
<nome>LinhaC</nome>
<eficiencia>79.5</eficiencia>
</linha>
</linhas>
</dados>
''' 
# Tarefa 10: Leia o XML e mostre o nome e a eficiência de cada linha 
root = ET.fromstring(xml_data)
eficiencias = {}
print("--- TAREFA 10: Eficiência das Linhas (XML) ---")
for linha in root.findall('.//linha'):
    nome = linha.find('nome').text
    eficiencia = float(linha.find('eficiencia').text)
    eficiencias[nome] = eficiencia
    print(f"Linha: {nome} - Eficiência: {eficiencia}%")

# Tarefa 11: Identifique qual é a linha menos eficiente, com base no XML 
linha_menos_eficiente = min(eficiencias, key=eficiencias.get)


# --- RELATÓRIO FINAL ---
# Tarefa 12: Exiba um relatório textual organizado 
print("\n" + "="*40)
print("RELATÓRIO DE PRODUÇÃO".center(40))
print("="*40)
print(f"Setor: {setor}")
print(f"Supervisor responsável: {supervisor}")
print(f"Percentual da meta atingido: {percentual_meta:.2f}% (Meta de {meta_diaria})")
print("-" * 40)
print("PRODUÇÃO POR LINHA:")
for linha, total in producao_por_linha.items():
    print(f" - {linha}: Total {total} un. | Classificação: {classificacao_linhas[linha]}")
print("-" * 40)
print(f"Linha menos eficiente: {linha_menos_eficiente} ({eficiencias[linha_menos_eficiente]}%)")
print("="*40)