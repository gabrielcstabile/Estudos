import csv

path: str = "./exemplo.csv"

arquivo_csv: list = []

with open(file = path, mode="r", encoding='utf-8') as arquivo:
    # Cria um objeto leitor de CSV
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print (arquivo_csv)
