class Persona():#definir una clase
  def __init__(self,nom,ape):#definir una funcion
    self.nombre=nom
    self.apellido=ape

  def nombre_completo(self):#Definir una funcion 
    print(self.nombre +""+self.apellido)

class Estudiante(Persona):#Definir una clase
  def __init__(self,nom,ape,carr):
    super().__init__(nom,ape)
    self.carrera=carr

  def mostrar_carrera(self):#Definir una funcion 
    print(self.carrera)