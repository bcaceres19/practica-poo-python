class Animal():
    def sonido(self):
        pass

class Gato(Animal):
    def sonido(self):
        return "Miau"
    
class Perro(Animal):
    def sonido(self):
        return "Guau"

def hacer_sonido(animal:Animal):
    print(animal.sonido())    
    
gato = Gato()
perro = Perro()

hacer_sonido(gato)
hacer_sonido(perro)

#Es para ver el tipo de dato que se le da
print(type(1))