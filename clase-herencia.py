class Persona:
    def __init__(self, nombre, edad, telefono):
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono

class Artista:
    def __init__(self, habilidad):
        self.habilidad = habilidad
     
    def mostrar_habilidad(self):
        return f"Mi habilidad es: {self.habilidad}"          

#Herencia simple
class Empleado(Persona):
    def __init__(self, trabajo, salario, nombre, edad, telefono):
        #Invoca constructor de la otra clase
        super().__init__(nombre, edad, telefono)
        self.trabajo = trabajo 
        self.salario = salario

#Herencia multiple
"""
    Con self hace referencia a la propia clase
    Con super() hace referencia a la clase heredada, es una buena practica
"""
class EmpleadoArtista(Persona, Artista):
    def __init__(self, nombre, edad, telefono, habilidad, salario, empresa): 
         Persona.__init__(self, nombre, edad, telefono)
         Artista.__init__(self, habilidad)
         self.salario = salario
         self.empresa = empresa
     
    def presentarse(self):
        return f"Hola soy {self.nombre} y {super().mostrar_habilidad()}"     

def saludar():
    pass #Se usa cuando un metodo o funcion no tienen datos

saludar()

roberto = Empleado("cocinero", "2000000", "Brahian", 20, "3016823624")

print(roberto.nombre)
print(roberto.trabajo)

juan = EmpleadoArtista("Brahian", 20, "3016823624", "Programador", "6580000", "Intempo");
print(juan.presentarse())

#Para saber si un una clase es herencia de otra clase
herencia = issubclass(EmpleadoArtista,Artista)

#Para saber si un objeto es una instancia de una clase
instancia= isinstance(roberto, EmpleadoArtista)

print(herencia)
print(instancia)