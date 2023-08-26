import unittest
import sqlite3
from pergunta01 import  Produto

class TesteProduto:
    def setUp(self):
        self.banco = sqlite3.connect(':memory:')
        self.cursor = self.banco.cursor()

        self.cursor.execute("")


    def teste_add(self):
        resultado = Produto("Leite em Pó",12,4)
        self.assertEqual(resultado,("Leite em Pó",12,4))
