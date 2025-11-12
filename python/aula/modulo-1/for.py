# Exemplo de uso do loop for

# Iterando sobre uma lista
numbers = [1, 2, 3, 4, 5]
for elements in numbers:
    print(elements)

# Iterando sobre uma tupla
print("-----")
tuple = (1, 2, 3, 4, 5)
for elements in tuple:
    print(elements)
    
# Iterando um dicionário
print("-----")
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key in person: 
    print(key)

print("-----")
for value in person.values():
    print(value)

print("-----")
for key,values in person.items():
    print(f"{key}: {values}")

#range(): intervalo numérico
# [0,1,2,3,4]
range(0,10)
print("-----")
for numero in range(5):
    print("Numero:", numero)

print("-----")
for i in range(0, len(numbers)):
    print("Indice:", i)
    print("Valor:", numbers[i])

# enumerate(): índice e valor
print("-----")
list = ['a', 'b', 'c', 'd']
for indice, valor in enumerate(list):
    print(f"Índice: {indice}, Valor: {valor}")
