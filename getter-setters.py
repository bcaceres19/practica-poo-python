class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre;
        self.__edad = edad;
        
    def set_nombre(self, nombre):
        self.__nombre = nombre;
    
    def get_nombre(self):
        return self.__nombre;          
    
persona = Persona("Brahian", 12)

print(persona.get_nombre())
persona.set_nombre("Juan")
print(persona.get_nombre())