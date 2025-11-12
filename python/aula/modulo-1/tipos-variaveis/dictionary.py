# Criando um dicionário em Python

pessoa = {
    "name": "Gustavo",
    "last_name": "Rabelo",
    "age": 22,
    "city": "São Paulo"
}

# Exibindo o dicionário
print("Meu dicionário:", pessoa)


# Acessando valores no dicionário
print("Nome:", pessoa["name"])
print("Idade:", pessoa["age"])
print("Cidade:", pessoa["city"])

# Atualizando valores no dicionário
pessoa["age"] = 23  # Atualizando a idade
print("Idade atualizada:", pessoa["age"])

# Removendo um par chave-valor
del pessoa["last_name"]

# Métodos úteis de dicionários

# Métodos keys(), values() e items()

# Keys
chaves = pessoa.keys()
print("Chaves do dicionário:", chaves)
print("Primeira chave:", list(chaves)[0])

# Values
valores = pessoa.values()
print("Valores do dicionário:", valores)
print("Primeiro valor:", list(valores)[0])

# Items
itens = pessoa.items()
print("Itens do dicionário:", itens)
print("Primeiro item:", list(itens)[0][1])
print("Segundo item: %s - %s" % (itens[1][0], itens[1][1]))
