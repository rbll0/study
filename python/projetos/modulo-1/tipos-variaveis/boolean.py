# Booleanos em Python suporta dois valores: True (Verdadeiro) e False (Falso).

# Condicional 

if True: 
    print("Isso é verdade!")
else:
    print("Isso é falso!")

# Operadores Lógicos: and e or


# And - Retorna True se ambos os operandos forem True
if True and True: # Se ambos forem verdadeiros executa o bloco
    print("Ambos são verdadeiros!")

if True and False: # Se um for falso, não executa o bloco
    print("Isso não será impresso.")

# Or - Retorna True se pelo menos um dos operandos for True

if True or False: # Se um for verdadeiro, executa o bloco
    print("Pelo menos um é verdadeiro!")

if False or False: # Se ambos forem falsos, não executa o bloco
    print("Isso não será impresso.")

if True or True: # Se ambos forem verdadeiros, executa o bloco
    print("Ambos são verdadeiros novamente!")
