
def criar_pessoa(lista_de_pessoa):
    print('CADASTRO DE NOVA PESSOA')
    nome = input('Digite o nome : ')
    telefone = int(input('Digite o número de telefone: '))
    idade = int(input('Digite a idade: '))
    email = input('Digite o email: ')
    
    pessoa = {
        'nome' : nome,
        'telefone' : telefone,
        'idade' : idade,
        'email' : email 
    }
    lista_de_pessoa.append(pessoa)
    print('Pessoa Cadastrada com sucesso')



def listar_pessoas(lista_de_pessoa):
     if not lista_de_pessoa:
        print('A lista de pessoas está vazia')
        return
     print('| LISTA DE PESSOAS |')
     for idx, pessoa in enumerate(lista_de_pessoa, start=1):
         print(f"{idx}. Nome: {pessoa['nome']}, Telefone: {pessoa['telefone']}, email:{pessoa['email']}")


def atualizar_pessoa(lista_de_pessoa):
    listar_pessoas(lista_de_pessoa)
    index = int(input("Digite o indice da pessoa que deseja atualizar: "))
    if 1 <= index <= len(lista_de_pessoa):
        nome = input('Digite o novo nome: ')    
        telefone = int(input('Digite o novo número de telefone: '))
        idade = int(input('Digite nova idade'))
        email = input('Digite o novo email')

        lista_de_pessoa[index-1]['nome']=nome
        lista_de_pessoa[index-1]['telefone']=telefone
        lista_de_pessoa[index-1]['idade']=idade
        lista_de_pessoa[index-1]['email']=email
        print("Pessoa atualizada com sucesso!")
    else:
         print("Índice inválido!")

def delete_pessoa(lista_de_pessoa):
    listar_pessoas(lista_de_pessoa)

    indx = input('| Digite o núemro indice da pessoa que deseja excluir|: ')
    if 1 <= indx <= len(lista_de_pessoa):
        del lista_de_pessoa[indx - 1]
        print("Pessoa excluída com sucesso!")
    else:
        print("Índice inválido!")


def main():
    lista_de_pessoa = []
    while True:
        print('\nSelecione uma opção')
        print('1 - CADASTRAR NOVA PESSOA')
        print('2 - LISTAR PESSOAS')
        print('3 - ATUALIZAR UM DADO')
        print('4 - EXCLUIR UM DADO')
        print('5 - SAIR')

        opcao = int(input('Digite o número de opção:'))


        switch = {

            1: criar_pessoa,
            2: listar_pessoas,
            3: atualizar_pessoa,
            4: delete_pessoa,
            5: exit
        }

        func = switch.get(opcao)
        if func:
            func(lista_de_pessoa)
        else:
            print('Opção Inválida tente novamente')  

if __name__ == "__main__":
    main()
