class Carta(object):
    def __init__(self, rango, pinta, puntos, graphic):
        self.rango = rango
        self.pinta = pinta
        self.puntos = puntos
        self.graphic = graphic
        
    def __repr__(self):
        return self.pinta + self.rango

    def getpunto (self):
        return int(self.puntos)

    def getrango(self):
        return str(self.rango)

    def getgraphic(self):
        return self.graphic

    
def Baraja():
    '''Funcion crear a baraja y cartas'''
                             
    from PyQt4 import QtGui
    import os

    rango = {'A': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}
    pinta = ['P', 'C', 'D', 'T']

    new_baraja = []
    path = os.getcwd()  # metodo get el directorio actual para usar para encontrar la imagen de las tarjetas.
    for key in rango:
        for s in pinta:
            image = QtGui.QImage(path + '/cartas/' + s + key + '.png')
            new_baraja.append(Carta(str(key), s, rango[key], image))
    return new_baraja

def crear_aparato(Baraja, size):

    '''funcion que crea mazos de numeros de tamano en un zapato de blackjack en forma de diccionario con la cadena de la Tarjeta
     y el numero de la carta que queda en el mazo'''

    aparato = {}
    for carta in Baraja:
        aparato[carta]= size
    return aparato

def repartir_carta(aparato):

    '''Crear cartas de la baraja'''

    from random import choice
    dealt_card = choice(list(aparato.keys()))

    if aparato[dealt_card] == 0:
        return repartir_carta(aparato)
    else:
        aparato[dealt_card] -= 1
        return dealt_card
