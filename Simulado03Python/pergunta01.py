import sqlite3

try:
    banco = sqlite3.connect('dados.db')
    cursor = banco.cursor()

    #Verifica se existe a tabela produtos
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='produtos'")
    tabela_existe = cursor.fetchone()
    #SE NÃO EXISTIR A TABELA, CRIAR A TABELA
    if not tabela_existe:
        cursor.execute("CREATE TABLE produtos (nome text, quantidade integer, preco float)")
    #implemente métodos para adicionar, buscar e atualizar produtos no banco de dados.


    class Produto:
        def __init__(self,nome,quantidade,preco):
            self.nome = nome
            self.quantidade = int(quantidade)
            self.preco = float(preco)

    
        def add(self):
            cursor.execute("INSERT INTO produtos VALUES (?,?,?)",(self.nome,self.quantidade,self.preco))
            banco.commit()
            
            return "Dados inseridos com Sucesso!"

        def buscar(self):
            cursor.execute("SELECT * FROM produtos")
            return cursor.fetchall()

        def atualizar(self, novo_nome, nova_quantidade, novo_preco):
            cursor.execute("UPDATE produtos SET nome =?, quantidade=?, preco=? WHERE nome=?",(novo_nome,nova_quantidade,novo_preco,self.nome))
            banco.commit()

except sqlite3.Error as err:
    print("ERRO", err)


produto = Produto("Leite em pó",10,19)

produto.add()
lista_produtos = produto.buscar()
print(lista_produtos)


produto.atualizar("Leite condesado", 4,2)
produtos_atualizados = produto.buscar()
print(produtos_atualizados)

banco.close()