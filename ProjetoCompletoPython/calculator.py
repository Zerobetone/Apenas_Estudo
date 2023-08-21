
class Calculator:

    def __init__(self):
        self.data = []

    def add_data(self,value):
        self.data.append(value)

    def soma(self):
        return sum(self.data)
    

    def mean(self):
        if (len(self.data) ==0):
            return None
        return sum(self.data)/len(self.data)
    
    def maior(self):
        if((len(self.data) )== 0):
            return None
        maior = self.data[0]
        for value in self.data:
            if(maior<value):
                maior = value
        return maior
    
    def menor(self):
        if((len(self.data) )== 0):
            return None
        menor = self.data[0]
        for value in self.data:
            if(menor>value):
                menor = value
        return menor    

#Calculo

#calc = Calculator()
#calc.add_data(3)
#calc.add_data(4)
#calc.add_data(7)

#print("Soma", calc.soma())
#print("Média", calc.mean())
#print("Maior", calc.maior())
#print("Menor", calc.menor())