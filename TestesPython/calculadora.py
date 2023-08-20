class Calculator:
    def add(self, a, b):
        return a+b  # Implementar a operação de soma

    def subtract(self, a, b):
        return a-b  # Implementar a operação de subtração

    def multiply(self, a, b):
        return a*b  # Implementar a operação de multiplicação

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Não é permitido denominador zero")
        return a/b  # Implementar a operação de divisão