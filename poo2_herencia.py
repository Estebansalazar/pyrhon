# -*- coding: utf-8 -*-

class Vehiculos():

    def __init__(self,marca,modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False

    def arrancar (self):
        self.enmarcha=True

    def acelerar (self):
        self.acelerar=True

    def frenar (self):
        self.frenar=True

    def estado (self):
        print ("La marca es: %s"%(self.marca), "\n Modelor %s"%(self.modelo), "\n Acelerado %s"%(self.acelera), "\n Frenar %s"%(self.frena))

# Class Moto (), en los parentesis escribimos el nombre
#de la clase que heredamos

class Furgoneta (Vehiculos):

    def carga (self, cargar):
        self.cargado=cargar

        if(self.cargado):
            return "la Furgoneta esta cargada"
        else:
            return "la furgoneta no está cargada"



class Vhelectricos():
    # creamos el constructor con el __init__
    def __init__ (self):
        self.autonomia=100

    def cargaelectrica (self):
        self.cargando=True





class Moto (Vehiculos):
    hcaballito=""

    #sobreescribimos el metodo estado, usando el mismo nombre del metodo
    #y los mismos parametros. sobreescribimos el metodo de la clase padre(la invalidamos)
    def estado (self):
        print ("La marca es: %s"%(self.marca), "\n Modelor %s"%(self.modelo), "\n Acelerado %s"%(self.acelera), "\n Frenar %s"%(self.frena), "\ncaballito: %s"%(self.hcaballito))


    def caballito (self):
        self.hcaballito="estoy haciendo un caballito"



miMoto=Moto("Ducati","murcielago")
miMoto.caballito()
miMoto.estado()

miFurgoneta=Furgoneta("Xiami","1000")
miFurgoneta.arrancar()
miFurgoneta.estado()
miFurgoneta.carga(True)

#herencia múltiple con Vhelectricos, vehículos.
#BicicletaElectrica, tienes prefenrencia la primera clase indicada es de cir Vhelectricos, es decir tomamos su constructor.
class BicicletaElectrica (Vhelectricos, Vehiculos):
    pass

miBici = BicicletaElectrica()