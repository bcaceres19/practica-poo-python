class MiClass:
    def __init__(self):
        self.__atributo_privado = "valor"
        self._atributo_semi_privado = "valor dos"
        self.atrbibuto_publico = "valor tres"
    
    #metodo privado
    def __hablar(self):
        print("hablar")
    
    #metodo semi privado
    def _hablarDos(self):
        print("Uno")

    #metodo publico
    def hablar(self):
        print("tres")   
        
objeto = MiClass();
print(objeto.__atributo_privado)
print(objeto._atributo_semi_privado)
print(objeto.atrbibuto_publico)
