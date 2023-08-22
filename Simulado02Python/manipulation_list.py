lista = [
    {"nome": "Paulo", "idade": 19, "nota": 9},
    {"nome": "Gustavo", "idade": 18, "nota": 9},
    {"nome": "Lucas", "idade": 17, "nota": 10},
    {"nome": "Mateus", "idade": 16, "nota": 10},
    {"nome": "Eduardo", "idade": 15, "nota": 8}
]


def calc_media(lista):
    if not lista:

        return None

    soma =0
    for aluno in lista:
        soma+=aluno["nota"]
    return soma/len(lista)

def maior_nota(lista):
    if not lista:

        return None

    maior = lista[0]
    for aluno in lista:
        if(maior["nota"]<aluno["nota"]):
            maior = aluno
        
    return maior["nome"]



print("A média da turma foi ", calc_media(lista))
print("O aluno com maior nota foi o ", maior_nota(lista))
