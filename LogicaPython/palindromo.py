 

def verificapalindromo(palavra):
    palavra = palavra.lower()
    if  palavra == palavra[::-1]:
        return palavra + " é um palindromo: " + palavra[::-1]
    return palavra+" Não é Palindromo"



print(verificapalindromo("abacaxi"))