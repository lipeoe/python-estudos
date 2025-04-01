import os

def soma(num1, num2):
    resultado = num1 + num2
    return resultado

def testar_soma(num1, num2, resultadoEsperado):
    resultado = soma(num1, num2)
    print(f"{num1} + {num2} = {resultado}")
    if resultado == resultadoEsperado:
        print(f"Resultado: {resultado}\nResultado esperado: {resultadoEsperado}")
    else:
        print(f"O resultado esperado era: {resultadoEsperado} e foi {resultado}")
    return

num1 = int(input("Digite um número: "))
num2 = int(input("Digite um número: "))
resultadoEsperado = int(input("Digite o resultado esperado: "))

testar_soma(num1, num2, resultadoEsperado)