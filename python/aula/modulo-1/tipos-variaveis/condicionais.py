# Condicionais em Python

# If, elif, else

# Exemplo básico de if
age = int(input("Digite sua idade: "))
if (age >= 18): 
    print("Você é maior de idade.")
elif (age >= 12):
    print("Você é um adolescente.")
else:
    print("Você é uma criança.")

# Exemplo com operadores lógicos
mensagem = "Pode tirar a carteira de habilitação." if age >= 18 else "Não pode tirar a carteira de habilitação."
print(mensagem)

