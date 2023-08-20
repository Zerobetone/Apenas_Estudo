#def analisar_texto(texto):
#    palavras = texto.lower().split()
#    ocorrencias = {}
#    for palavra in palavras:
#        if palavra in ocorrencias:
#            ocorrencias[palavra] += 1
#        else:
#            ocorrencias[palavra] = 1
#    return ocorrencias
#
# Exemplo de uso
#texto = "Este é um exemplo de um texto. Um exemplo simples."
#resultado = analisar_texto(texto)
#print(resultado)

def ocorrencias_palavra(lista_palavras):
    ocorrencia = {}
    for palavra in lista_palavras:
        ocorrencia[palavra] = ocorrencia.get(palavra, 0)+1
    return ocorrencia


def processar_palavra(texto):
    palavras = texto.lower().split()
    return palavras

def analisar_texto(texto):
    palavra = processar_palavra(texto)
    ocorrencias = ocorrencias_palavra(palavra)
    return ocorrencias



texto = "Este é um exemplo de um texto. Um exemplo simples."
resultado = analisar_texto(texto)
print(resultado)
