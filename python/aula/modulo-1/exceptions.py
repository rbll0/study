print("Exemplo de exceções em Python")

while True:
    try: # Bloco de código que pode gerar exceções
        numero = int(input("Digite um número: ")) 
        res = (10 / numero)
       
    except ValueError as ve: # Captura exceções específicas
        print(f"Erro de valor: {ve}")    
    except Exception as e: # Captura qualquer outra exceção
        print(f"Ocorreu um erro: {e}")
    else:
         print(f"O resultado é {res}") # Se não ocorrer erro
    finally:
        print("Execução finalizada.")  # Sempre executa, independentemente de erro ou não
