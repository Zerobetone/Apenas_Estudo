class Animal:

    def falar(self):
        return "O animal está fazendo barulho"
    


class Cachorro(Animal):
        def som_cachorro(self):
  
            return self.falar() + " o cachorro está latindo "

class Gato(Animal):
        def som_gato(self):
            
            return self.falar() + " o gato está miando " 
        
gato = Gato()
cachorro = Cachorro()

print( gato.som_gato() )
print( cachorro.som_cachorro() )    
