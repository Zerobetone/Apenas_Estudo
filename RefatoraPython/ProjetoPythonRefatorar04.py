#def calcular_estatisticas(numeros):
#    total = sum(numeros)
#    quantidade = len(numeros)
#    media = total / quantidade
#    maior = max(numeros)
#    menor = min(numeros)
#    return total, quantidade, media, maior, menor

# Exemplo de uso
#valores = [10, 15, 20, 25, 30]
#total, quantidade, media, maior, menor = calcular_estatisticas(valores)
#print("Total:", total)
#print("Quantidade:", quantidade)
#print("Média:", media)
#print("Maior:", maior)
#print("Menor:", menor)

def calcular_estatisticas(numeros):
    total = sum(numeros)
    quantidade = len(numeros)
    media = total / quantidade
    maior = max(numeros)
    menor = min(numeros)
    return total, quantidade, media, maior, menor

# Exemplo de uso
valores = [10, 15, 20, 25, 30]
total, quantidade, media, maior, menor = calcular_estatisticas(valores)
print("Total:", total)
print("Quantidade:", quantidade)
print("Média:", media)
print("Maior:", maior)
print("Menor:", menor)