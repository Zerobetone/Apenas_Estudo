palavras ="abacate abacaxi banana uva abacate mamao uva uva melancia banana banana"

def cont_palavras(palavras):
    palavras = palavras.lower().split()
    dicionario_palavra ={}
    for palavra in palavras:
        if palavra in dicionario_palavra:
            dicionario_palavra[palavra]+=1
        else:
            dicionario_palavra[palavra]=1

    print(dicionario_palavra) 




cont_palavras(palavras)