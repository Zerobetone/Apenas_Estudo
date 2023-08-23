

class Produto:
    def __init__(self):
        self.lista = []
 

    def add(self,nome,quantidade,preco):
        self.produto ={"nome":nome, "quantidade":quantidade, "preco":preco}
        self.lista.append(self.produto)
        return self.produto["nome"] + " adicionado com sucesso!"
    
    def listar(self):
        if not self.lista:
            return "Lista vazia"

        return self.lista
    
    def atualiza(self, id, novo_nome, nova_quantidade, novo_preco):
        id=int(id)-1
        if (0< id >len(self.lista)):
            return "Id Inválido"

        self.lista[id]={"nome":novo_nome, "quantidade":nova_quantidade, "preco":novo_preco}
        return "Produto atualizado com sucesso!"

    def excluir(self,id):
        id=id-1
        if 0<id>len(self.lista):
            return "O id não faz parte da lista"
        nome_do_produto = self.lista[id]["nome"]
        self.lista.pop(id)
        return "Produto : "+ nome_do_produto +" excluído!"


produto = Produto()

print("Primeira Inserção: ",produto.add("Leite em pó",10,18))
print("Segunda Inserção: ",produto.add("Açucar",11,13))
print("Terceira Inserção: ",produto.add("Café",10,18))


print("Impreção dos produto: ", produto.listar())

print("Atualização de Leite: ", produto.atualiza(1,"Leite Condensado",12,34))
print("Impreção do produto atualizado: ", produto.listar())

print(produto.excluir(2))
print("Impreção após produto excluído: ", produto.listar())


