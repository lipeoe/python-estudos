import os

def verificar_positivo(valor):
    if valor >= 0:
        return "Positivo"
    else:
        return "Negativo"

# Define a função que testa cada número lido
def testar_positivo(valor):
    status = verificar_positivo(valor)
    print(f"Valor = {valor}, Status = {status}")
    resultado.write(f"{valor},{status}\n")
    return

# rotina principal para abrir arquivo de dados de teste e gravar os resultados
print("Resultado")

pasta_de_entrada = "python-01"
arquivo_de_entrada = os.path.join(pasta_de_entrada, "valores.txt")
arquivo_de_saida = os.path.join(pasta_de_entrada, "resultado.txt")


# ggravar no arquivo txt com resultado do teste
resultado = open(arquivo_de_saida, "w")
print(" ")
print("Mostrando os resultados do teste")
with open(arquivo_de_entrada, "r") as arquivo:
    for registro in arquivo:
        valor = int(registro.strip())
        testar_positivo(valor)

arquivo.close()
resultado.close()
# Abrir e ler o arquivo de resultado
with open(arquivo_de_saida, "r") as resultado:
    print("Mostrando todos os registros do arquivo resultado")
    for registro in resultado:
        print(registro.strip())