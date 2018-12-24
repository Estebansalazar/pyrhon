# -*- coding: utf-8 -*-
"""
clase
propiedad
métodos=define comportamiento de las clases
parametro "self":
"""

class Coche():
    #nuestro estado inicial= constructor. El constructor le da un estado inicial a los objetos de una clase.
    #metodo "__init__(self)"": especifica que esto es un método constructor agregandolo el self a cada uno
    def __init__(self):
        #self.__ruedas nos pèrmite encapsular variables
        self.__largoChasis=250
        self.__anchoChasis=120
        self.__ruedas=4
        self.__enmarcha=False

    def arrancar (self,arrancamos):
        #miCoche.arrancamos
        self.__enmarcha=arrancamos

        if(self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if(self.__enmarcha and chequeo):
            return "el coche esta en marcha"

        elif(self.__enmarcha and chequeo==false):
            return "algo a ido mal en el chequeo"

        else:
            return "el coche está varado \n"

#el metodo estado nos proporciona el estado de nuestro objeto
    def estado (self):
        print("El coche tiene %s"%(self.__ruedas)," ruedas. Un largo de %s"%(self.__largoChasis), " y un largo de chasis de %s"%(self.__anchoChasis),"\n")

        #__ encapsulamos el metodo, al hacer esto el método no
        #será llamado desde fuera
    def __chequeo_interno(self):
        print("realizando chequeo interno")
        sel.gazolina="ok"
        self.aceite="ok"
        self.puertas="cerradas"

        if(self.gazolina=="ok" and self.aceite=="ok" and sel.puertas=="cerradas"):
            return True
        else:
            return False



#instanciamos nuestra clase
#Creamos nuestro primer objeto
miCoche=Coche()

print (miCoche.arrancar(True))
#miCoche viaja y se almacena en self
#lo que estamos diciendo en verdad es:
#self.enmarcha=True es lo mismo que miCoche.enmarcha=True
print(miCoche.estado())

#creamos nuestro segunda instancia de clase u objeto

print("----------segunda instancia de la clase---------")
miCoche2=Coche()
print (miCoche2.arrancar(False))
print(miCoche2.estado())
