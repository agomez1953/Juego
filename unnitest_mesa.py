from unittest import TestCase
from mesa import *

class Testmesa(TestCase):

    def test_getpunto(self):
        dado = Carta('A', 'P', 500, '')
        espero = 500
        recibo = dado.getpunto()
        self.assertEqual(espero, recibo)


    def test_getrango(self):
        dado = Carta('A', 'P', 500, '')
        espero = 'A'
        recibo = dado.getrango()
        self.assertEqual(espero, recibo)

    def test_getgrapic(self):
        dado = Carta('A', 'P', 500, '')
        espero = ''
        recibo = dado.getgraphic()
        self.assertEqual(espero, recibo)

    def test_Baraja(self):
        pass

    def test_crear_aparato(self):
        pass

    def test_repartir_carta(self):
        pass
