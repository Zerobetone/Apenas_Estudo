#def calcular_media(lista):
#    total = 0
#    for num in lista:
#        total = total + num
#    media = total / len(lista)
#    return media
#
# Exemplos de uso
#valores = [10, 15, 20, 25, 30]
#print("Média:", calcular_media(valores))


def calcular_media(lista):
    soma= sum(lista)
    return soma/len(lista)

valores = [10, 15, 20, 25, 30]
print("Média:", calcular_media(valores))