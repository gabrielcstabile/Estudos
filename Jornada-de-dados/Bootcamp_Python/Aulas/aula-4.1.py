import json

# Trabalhando com lista

produto: str = "PS5"
produto_2: str = "Xbox"
produto_3: str = "PC Gamer"
produto_4: str = "Nintendo Switch 2"

produtos: list = []

produtos.append(produto)
produtos.append(produto_2)
produtos.append(produto_3)
produtos.append(produto_4)
produtos.pop()

print(produtos)

# Trabalhando com dicionário

produto_01: dict = {
    "Console":"PS5",
    "Quantidade":5,
    "Valor": 4000,
    "Disponibilidade": True
}

produto_02: dict = {
    "Console":"XBOX",
    "Quantidade":10,
    "Valor": 4000,
    "Disponibilidade": True
}

carrinho: list = []

carrinho.append(produto_01)
carrinho.append(produto_02)

print(carrinho)

carrinho_json = json.dumps(carrinho)
print(carrinho_json)