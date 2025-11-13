# Exemplo 

print("--------------------")

def saudacao(nome):
    print(f"Olá, {nome}!")

saudacao("Gustavo")


print("--------------------")

def quadrado(num): 
    res = num ** 2
    return res

resultado = quadrado(4)
print(f"O quadrado de 4 é {resultado}")

print("--------------------")

# Chama função com multiplos parametros
def soma(a, b):
    res = a + b
    return res

total = soma(5, 5)
print(f"O resultado da soma é {total}")

print("--------------------")
