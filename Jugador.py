from Carta import Carta
import random

class Jugador:
    def __init__(self, nombre, dinero):
        """
        Esta funcion sirve como constructor
        :param nombre: esta variable es el nombre del jugador
        :param dinero: esta variable es el dinero del jugador
        """
        self.nombre = nombre
        self.dinero = dinero

    def __repr__(self):
        """
        Esta funcion es para imprimir cada uno de las cartas
        :return:
        """
        return f'EL jugador es {self.nombre} y tiene { self.dinero} pesos'

    def pedir(self):
        while True:
            return True