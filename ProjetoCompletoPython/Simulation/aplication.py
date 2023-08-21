#Basicamente eu primeiramente importaria a biblioteca para nos fornecer as ferramentas necessárias para essa atividade
import sqlite3
#Segundo passo seria colocar nossa implementação dentro de uma estrutura de tratamento de váriveis, para evitar possíveis erros de inserção de dados no banco
try:
    #Terceiro passo : armazenaria a  conexão com o banco utilizando uma váriavel, caso o banco não existisse o comando se encarregaria de criar um arquivo .db para isso
    banco = sqlite3.connect('bd_aplications.db')

    #Quarto Passo seria criar um curso para permitir fazer consultas SQL no Python
    cursor = banco.cursor()


    #Quinto passo : Fiz esse passo devido não ter um db com dados já nele, essa linha de código irá criar uma tabela com nome livros e campos titulo, genero e ano
    cursor.execute("CREATE TABLE livros (titulo text, genero text, ano integer)")

    #Sexto passo : Fiz algumas inserções estaticamente, apenas para se ter dados em meu banco para a consulta
    titulo = "A hora da estrela"
    genero = "Romance"
    ano = 2002
    cursor.execute("INSERT INTO livros VALUES (?,?,?)", (titulo, genero, ano))
    banco.commit()

    titulo = "A moreninha"
    genero = "Romance"
    ano = 1998
    cursor.execute("INSERT INTO livros VALUES (?,?,?)", (titulo, genero, ano))
    banco.commit()

    titulo = "Corpo na biblioteca"
    genero = "Ficção"
    ano = 2010
    cursor.execute("INSERT INTO livros VALUES (?,?,?)", (titulo, genero, ano))
    banco.commit()

    titulo = "O Quinze"
    genero = "Drama"
    ano = 1915
    cursor.execute("INSERT INTO livros VALUES (?,?,?)", (titulo, genero, ano))

    banco.commit()
   


    #Sétimo passo: como a questão solicita uma consulta ao banco de dados na tabela livros, segue o trecho de código para essa tarefa
    cursor.execute("SELECT * FROM livros ")
    #Para imprimir todos os registros utilizei a função fetchall
    print(cursor.fetchall())

    banco.close()

except sqlite3.Error as err:
    print("ERRO ",err)



