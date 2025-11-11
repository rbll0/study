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

# String no Python são imutáveis
texto = "Python"
print(texto[0]) # Acessando o primeiro caractere
print(texto[1]) # Acessando o segundo caractere
print(texto[-1]) # Acessando o último caractere
print(texto[0:3]) # Fatiamento da string (do índice 0 ao 2)
print(texto[2:]) # Fatiamento da string (do índice 2 até o final)
print(texto[:3]) # Fatiamento da string (do início até o índice 2)

# Métodos úteis para manipulação de strings
name = "Gustavo Rabelo"
name.find("a") # Retorna o índice da primeira ocorrência de "a"
name.count("a") # Conta quantas vezes "a" aparece na string

name.encode("utf-8") # Codifica a string em bytes usando UTF-8
name.encode().decode("utf-8") # Decodifica os bytes de volta para string usando UTF-8

telefone = "(11)98765-4321"
telefone_formatado = telefone.replace("-", "").replace("(", "").replace(")", "") # Remove caracteres específicos da string

nome.completo.split(" ") # Divide a string em uma lista usando espaço como separador
"-".join(nome) # Junta os caracteres da string com "-" como separador

nome_strip = "xGustavox"
nome_strip.strip("x") # Remove os caracteres "x" do início e do fim da string
nome_strip.lstrip("x") # Remove os caracteres "x" do início da string
nome_strip.rstrip("x") # Remove os caracteres "x" do fim da string

nome_completo.startswith("Gus") # Verifica se a string começa com "Gus"
nome_completo.endswith("belo") # Verifica se a string termina com "belo

"us" in nome_completo # Verifica se "us" está contido na string
"abc" not in nome_completo # Verifica se "abc" não está contido na string
