class terrestre():#definir una clase
  def hablar(self):#definir una funcion
    print("Hola soy un animal terrestre!")

class Perro(terrestre):#definir una clase
  def hablar(self):#definir una funcion
    print("Soy un perro...")

class Gato(terrestre):#definir una clase
  def hablar(self,mensaje):#definir una funcion
    self.mensaje=mensaje
    print(mensaje)

errestre=terrestre()#definir una variable para llamar a la clase
errestre.hablar()

perro=Perro()#definir una variable para llamar a la clase
perro.hablar()

gato=Gato()#definir una variable para llamar a la clase
gato.hablar("Soy un gato...")