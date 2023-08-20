import sqlite3

try:
    banco = sqlite3.connect('primeiro_banco.db')

    cursor = banco.cursor()
#Exclusão de dados onde a idade for igual a 19
    cursor.execute("UPDATE pessoas SET nome = 'Luis' WHERE idade=25 ")

    banco.commit()
    banco.close()
    print("Os dados foram atualizados com sucesso!")

except sqlite3.Error as erro:
    print("Erro ao atualizar: ", erro)
