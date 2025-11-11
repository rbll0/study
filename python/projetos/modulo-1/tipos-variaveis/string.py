# Declaração de strings em Python
nome_completo = "Gustavo Rabelo"

nome_completo_aspas = """ Gustavo Rabelo """ # String com aspas triplas (permite múltiplas linhas)

nome_completo_quebrado = "Gustavo \
    Rabelo" # String quebrada em múltiplas linhas com barra invertida

nome = "Gustavo"
sobrenome = "Rabelo"

# Formatação de strings
print("Nome completo (1a forma):", nome_completo) # Concatenação com vírgula
print("Nome completo (2a forma):" + nome_completo) # Concatenação com +
print("Nome completo (3a forma):" + "Gustavo" + "Rabelo") # Concatenação com f-string e +
print("Nome completo (4a forma):" + "Gustavo", "Rabelo") # Concatenação com f-string
print("Nome completo (5a forma):", nome_completo_aspas) # Usando aspas triplas
print("Nome completo (6a forma):", nome_completo_quebrado) # Usando barra invertida
print("Nome completo (7a forma): %s" % nome_completo) # Formatação com operador %
print("Nome completo (8a forma): %s %s" % (nome,sobrenome)) # Formatação com múltiplos valores e operador %
print(f"Nome completo (9a forma): {nome} {sobrenome}" ) # Formatação com f-strings
print("Nome completo (10a forma): {}".format(nome_completo)) # Formatação com método format
print("Nome completo (11a forma): {} {}".format(nome,sobrenome)) # Formatação com múltiplos valores e método format 

