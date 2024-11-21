class Calculadora():#definir una clase
    def __init__(self, num1, num2):#Definir una funcion 
        self._num1=num1
        self._num2=num2

    def suma(self):#Definir una funcion
        resultado=self._num1 + self._num2
        print(f"El resultado de la suma es: {self._num1} + {self._num2}={resultado}")

    def resta(self):#Definir una funcion
        resultado=self._num1 - self._num2
        print(f"El resultado de la resta es: {self._num1} -  {self._num2}={resultado}")

    def division(self):#Definir una funcion
        resultado=self._num1 // self._num2
        print(f"El resultado de la divisón es: {self._num1} // {self._num2}= {resultado}")

    def multiplicacion(self):#Definir una funcion
        resultado=self._num1 * self._num2
        print(f"El resultado de la multiplicación es: {self._num1} * {self._num2} = {resultado}")

operacion=Calculadora(20, 7)#mostrar el resultado como los datos q  ue se solicitan para que funcione la funcion
operacion.suma()

operacion=Calculadora(25, 10)
operacion.resta()

operacion=Calculadora(50, 10)
operacion.division()

operacion=Calculadora(7, 9)
operacion.multiplicacion()