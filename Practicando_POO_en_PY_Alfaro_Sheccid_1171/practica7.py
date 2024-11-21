class Universidad():#Definir una clase
  def __init__(self,Nombre):#definir una funcion que se ejecuta al crear un objeto
    self.Nombre=Nombre

class Carerra():#Definir una clase
  def carrera(self,especialidad):#definir una funcion que se ejecuta al crear un objeto
    self.especialidad=especialidad

class Estudiante(Universidad,Carerra):#Definir una clase
  def datos(self,nombre,edad):#definir una funcion que se ejecuta al crear un objeto
    self.nombre=nombre
    self.edad=edad
    print(f"El nombre del estudiante es {self.nombre}, tiene {self.edad} años, su especialidad es {self.especialidad}. Estudia en la preparatoria {self.Nombre}")

persona=Estudiante("CBTIs128")#definir variables para utilizar en la clase
persona.carrera("Programacion")
persona.datos("Sheccid", 16)