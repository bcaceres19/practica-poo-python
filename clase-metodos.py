class Celular:
    #"self" es una forma de hacerse referencia a si mismo
    #"__init__" es como un constructor
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

    def llamar(self):
        print("Estas llamando un metodo")
        
    def cortar(self):
        print("Estas cortando un metodo")    
        
celular1 = Celular('Samsung', 'S27', '48MP')
celular1.llamar()
celular1.cortar()
