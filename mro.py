class A:
    def hablar(self):
        print("Hola desde A")
        
class B(A):
    def hablar(self):
        print("Hola desde B")

class C(B):
    def hablar(self):
        print("Hola desde C")
        
class D(C,A):
    def hablar(self):
        print("Hola desde D")
        
d = D()

d.hablar()        

#Para saber la jerarquia en la 
# herencia que tenga la clase
print(D.mro())