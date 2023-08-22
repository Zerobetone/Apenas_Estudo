
def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo,"r") as arquivo:
            linhas = arquivo.readlines()
            return linhas
    except FileNotFoundError:
        print("O arquivo {} não existe".format(nome_arquivo))
        return []
    

nome_do_arquivo = "dados.txt"
linhas = ler_arquivo(nome_do_arquivo)
soma=0
for linha in linhas:
    linha= int(linha.strip())
    soma+=linha


print(" A soma dos valores em linhas no arquivo {} é {}!".format(nome_do_arquivo, soma))