"""
Una funcion decoradora coloca una funcionalidad extra
dentro de un funcion
"""
#Forma atigua
def decorador(funcion):
    def funcionModificada():
        print("Antes de llamar a la funcion")
        funcion()
        print("Despues de llamar a la funcion")
    return funcionModificada

def saludo():
    print("Hola Brahian")
    
saludoModificado = decorador(saludo)    
saludoModificado()

#Forma recomendada
@decorador
def saludoDos():
    print("Hola Brahian dos")

saludoDos()