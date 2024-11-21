class Estudiante(): #Definir una clase
    def __init__(self , nombre , nota): #definir una funcion 
        self.nombre=nombre
        self.nota=nota

    def imprimir(self):#definir una funcion
       print(f"Nombre:{self.nombre} \nNota: {self.nota}")

    def resultados(self): #definir una funcion
        if self.nota >= 7:
            print("Has APROBADO!")
        else:
            print("«Has REPROBADO!»")

estudiante1=Estudiante("Eliu" , 3)#Definir variable con el primer estudiante
estudiante1.imprimir()
estudiante1.resultados()

estudiante2=Estudiante("Sheccid" , 9)#Definir variable con el primer estudiante
estudiante2.imprimir()
estudiante2.resultados()