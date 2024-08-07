class Celular:
    #"self" es una forma de hacerse referencia a si mismo
    #"__init__" es como un constructor
    def __init__(self, marca, modelo, camara):
        self.marca = marca
        self.modelo = modelo
        self.camara = camara

celular1 = Celular('Samsung', 'S27', '48MP')
celular2 = Celular('Apple', '15', '50MP')

print(celular1.marca)
print(celular2.marca)



