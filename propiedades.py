class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
          
    #Forma apara evitar que se comporte
    #como funcion si no como propiedad
    #Permite usar la nomenclatura del punto
    #Para usar los getters
    @property
    def nombre(self):
        return self.__nombre    
    
    #Forma de generar setters
    @nombre.setter    
    def nombre(self, nombre):
        self.__nombre = nombre
        
    #Forma de eliminar datos    
    @nombre.deleter    
    def nombre(self):
        del self.__nombre
    
brahian = Persona("Brahian", 12)

nombreB = brahian.nombre
print(nombreB)
brahian.nombre = "Juan"
nombreNuevo = brahian.nombre
print(nombreNuevo)

del brahian.nombre #Elimina el nombre 
