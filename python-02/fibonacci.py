import os

def fibonacci(n):
    if n == 0: return 0
    if n == 1: return 1

    return fibonacci(n-1) + fibonacci(n-2)

def testa_fibonacci(n):
    resultado = fibonacci(n)
    print(f"resultado =  {fibonacci(n)}, resultado = {resultado}")
    resultadoFib.write(f"{n}, {resultado}\n")
    return


print("Resultado")

pasta_de_entrada = "python-02"
arquivo_de_entrada = os.path.join(pasta_de_entrada, "numeros_fibonacci.txt")
arquivo_de_saida = os.path.join(pasta_de_entrada, "resultado_fibonacci.txt")

resultadoFib = open(arquivo_de_saida, "w")

print("Resultados")
with open(arquivo_de_entrada, "r") as arquivo:
    for numeros in arquivo:
        numero = int(numeros.strip())
        testa_fibonacci(numero)

arquivo.close()
resultadoFib.close()

with open(arquivo_de_saida, "r") as resultado:
    print("Mostrando resultados fibonacci")
    for numeros in resultado:
        print(numeros.strip())
