# -*- coding: utf-8 -*-

class Persona ():
    
    def __init__(self,nombre,edad, Lugar_residencia):
         
        #creo una variable "self.nombre" que sea igual a lo que  introduzcamos
        #en el parametro "nombre" que introducimos en el contructor
        self.nombre=nombre
        self.edad=edad
        self.Lugar_residencia=Lugar_residencia

    def descripcion (self):
        print("Nombre: ", self.nombre, "\nedad:  ",self.edad, "\nLugar residencia: ", self.Lugar_residencia)

class Empleado (Persona):

    def __init__(self,salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):

        """
        ¿que hace el método super?
        El metodo super esta llamado al metodo de la clase padre
        es decir llama al metodo init, ejecuta primero el metood
        intit de la clase padre, les pasamos los datos y seguimos
        """
        super().__init__(nombre_empleado, edad_empleado, residencia_empleado)

        self.salario=salario

        self.antiguedad=antiguedad

    

Antonio = Empleado (2312423,12)
Antonio.descripcion()