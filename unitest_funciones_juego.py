from unittest import TestCase
from funciones_juego import *
from mesa import *

class Testfunciones_juego(TestCase):

    def test_inicializar_cartas(self):
        dado = ()
        espero = ''
        recibo = dado.inicializacion_cartas()
        self.assertEqual(espero, recibo)

    def test_blackjack_dealer(self):
       pass

    def test_split(self):
        pass

    def test_double(self):
        pass

    def test_hit(self):
        pass

    def test_dealer_play(self):
        pass

    def test_puntos_mano(self):
        pass

    def test_calculos(self):
        pass

    def test_ganancias(self):
        pass
