# Declaração 

# Exibindo a lista
my_list = [1,2,3,4,5, "Python", True, False]
print("Minha lista:", my_list)

# Exibindo os elementos da lista
my_list[0] = "Alterado"
print("Minha lista:", my_list)

print("my_list[0]",my_list[0])  # Primeiro elemento
print("my_list[5]",my_list[5])  # Quinto elemento
print("my_list[2:6]:",my_list[2:6]) # Fatiamento da lista do índice 2 ao 5
print("my_list[:6]:",my_list[:6]) # Fatiamento da lista do início ao índice 5
print("my_list[2:]:",my_list[2:]) # Fatiamento da lista do índice 2 até o final

# Métodos de listas

# Método append(): Adiciona um elemento ao final da lista
my_list.append(6)
print("Após append(6):", my_list)

# Método index(): Retorna o índice do primeiro elemento com o valor especificado
indice = my_list.index(6)
print("Índice do elemento 6:", indice)

# Método insert(): Insere um elemento em uma posição específica
my_list.insert(2, "Adicionando")
print("Após insert('Adicionando', 2):", my_list)

# Metodo pop(): Remove e retorna o último elemento da lista
ultimo_elemento = my_list.pop(3)
print("Após pop():", my_list)
print("Último elemento removido:", ultimo_elemento)

# remove(): Remove a primeira ocorrência de um valor específico
my_list.remove(True)
print("Após remove(True):", my_list)

# Método sort(): Ordena os elementos da lista (apenas para listas homogêneas)
my_list2 = [5, 2, 9, 1, 5, 6] # Não aceita misturar tipos diferentes
my_list2.sort()
print("Após sort():", my_list2)
