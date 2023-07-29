import sqlite3

banco = sqlite3.connect('primeiro_banco.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade integer, email text)")

#Atribuição de várivel nome - dado solicitado ao usuário
nome = input("Digite um nome? ")

#Atribuição de várivel idade - dado solicitado ao usuário
idade = int(input("Quantos anos essa pessoa tem? "))

#Atribuição de várivel email - dado solicitado ao usuário
email = input("Qual seu email? ")

#Inserção dos dados no Banco
cursor.execute("INSERT INTO pessoas VALUES (?, ?, ?)", (nome, idade, email))

#Commit dos dados no Banco
banco.commit()

#SELEÇÃO DOS DADOS PRESENTES NA TABELA PESSOAS
cursor.execute("SELECT * FROM pessoas")

print(cursor.fetchall())
