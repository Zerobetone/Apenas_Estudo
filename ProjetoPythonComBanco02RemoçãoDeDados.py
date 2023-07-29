import sqlite3

try:
    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()
#Exclusão de dados onde a idade for igual a 19
    cursor.execute("DELETE from pessoas WHERE idade = 41")

    banco.commit()
    banco.close()
    print("Os dados foram removidos com sucesso!")

except sqlite3.Error as erro:
    print("Erro ao excluir: ", erro)


