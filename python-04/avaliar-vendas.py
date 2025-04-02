import os
import json

pasta_de_entrada = "python-04"
arquivo_de_entrada = os.path.join(pasta_de_entrada, "dados.txt")
arquivo_de_saida = os.path.join(pasta_de_entrada, "total_venda.txt")
arquivo_de_saida_2 = os.path.join(pasta_de_entrada, "valor_por_cliente.txt")

def verifica_dados(arquivo_de_entrada):
    vendas = []
    with open(arquivo_de_entrada, "r") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split(";")

            vendas.append({
                "codigo_cliente": int(dados[0]),
                "nome_cliente": dados[1],
                "codigo_produto": int(dados[2]),
                "descricao": dados[3],
                "quantidade": int(dados[4]),
                "valor": int(dados[5]),
                "valor_total": int(dados[6])
            })
    print(json.dumps(vendas, indent=4))
    return vendas




def calcula_total(vendas, arquivo_de_saida):
    valor_por_cliente = {}
    soma_total = 0

    for venda in vendas:
        cliente = venda["codigo_cliente"]
        if cliente not in valor_por_cliente:
            valor_por_cliente[cliente] = venda["valor_total"]
        else:
            valor_por_cliente[cliente] += venda["valor_total"]
        soma_total += venda["valor_total"]


    with open(arquivo_de_saida, "w") as arquivo:
        for cliente, valor_total in valor_por_cliente.items():
            arquivo.write(f"Código cliente: {cliente} | Valor por cliente:{valor_total}\n")
        arquivo.write(f"\nSoma Total: {soma_total}\n")

    print(f"Soma: {soma_total}.")


def verifica_valor_total(vendas):
    valor_por_cliente = {}

    for venda in vendas:
        cliente = venda["codigo_cliente"]
        valor_esperado = int(venda["valor"]) * int(venda["quantidade"])
        if cliente not in valor_por_cliente:
            valor_por_cliente[cliente] = valor_esperado
        else:
            valor_por_cliente[cliente] += valor_esperado
        if valor_esperado != int(venda["valor_total"]):
                print(f"O valor total: {venda["valor_total"]} não corresponde ao valor esperado: {valor_esperado}")
        else:
            print(f"O valor esperado: {valor_esperado} é igual ao valor total por cliente: {venda["valor_total"]}")
    return valor_por_cliente



vendas = verifica_dados(arquivo_de_entrada)
valor_total = calcula_total(vendas, arquivo_de_saida)
resultado = verifica_valor_total(vendas)


          

