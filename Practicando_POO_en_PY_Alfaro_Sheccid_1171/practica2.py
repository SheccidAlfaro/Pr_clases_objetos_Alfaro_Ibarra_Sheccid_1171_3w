
class Persona:#Definir una clase
   def __init__(self, n, e):#definir una funcion 
        self.nombre=n
        self.edad=e

   def cumpleaños(self):#Definir una funcion
        self.edad += 1

p=Persona(input("Coloca tu nombre: "),int(input("Coloque su edad:")))#crear una variable que haga preguntas al usuario
p.cumpleaños()
p.cumpleaños()
print(f"{p.nombre} cumple {p.edad} años")

