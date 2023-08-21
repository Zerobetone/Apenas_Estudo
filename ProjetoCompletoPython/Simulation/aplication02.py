pessoas = [
    {"nome": "João", "idade": 19},
    {"nome": "Lucas", "idade": 19},
    {"nome": "Mateus", "idade": 19},
    {"nome": "Marcos", "idade": 19}
]

def verifica_dicionario(lista_dici):
    try:
        if not lista_dici:
            return None
        soma = 0
        cont = 0
        for elemento in lista_dici:
            if 'idade' in elemento:
                soma += elemento['idade']
                cont += 1

        if cont == 0:
            return None

        return soma / cont
    except KeyError:
        print("Um dicionário não contém a chave 'idade'")
        return None

print("A média das idades das pessoas do dicionario é ", verifica_dicionario(pessoas))
