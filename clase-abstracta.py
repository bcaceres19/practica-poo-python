from abc import ABC, abstractclassmethod

#Forma de crear una clase abstracta
class Persona(ABC):
    @abstractclassmethod
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    #Metodo abstracto
    """@abstractclassmethod
    def trabajar(self):
        pass    """
   
    def presentarse(self):
        print(f"Hola, me llamo: {self.nombre} y tengo {self.edad} años")
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo) 
        self._actividad = actividad
        
pedro = Estudiante("Brahian", 19, "Masculino", "Uno")       
pedro.presentarse()
