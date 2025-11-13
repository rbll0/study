print("Exemplo de importação de módulo padrão em Python.")
from math import sqrt

raiz_quadrada = sqrt(25)
print(f"a raiz quadrada de 25 é {raiz_quadrada}")

print("\nExemplo de criação e utilização de um módulo personalizado.")
import meu_modulo

mensagem = meu_modulo.saudacao("Gustavo")
dobro = meu_modulo.dobro(10)

print(mensagem)
print(f"O dobro de 10 é {dobro}")
