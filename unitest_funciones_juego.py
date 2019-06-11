from unittest import TestCase
from funciones_juego import *

class Testfunciones_juego(TestCase):

    def test_inicializar_cartas(self):
        dado = Instrumentos('Violonchelo', 'cuerdas', 4)
        espero = 'el instrumento Violonchelo es de cuerdas, tiene afinacion fa y melodia jazz'
        recibo = dado.clas_instrumento('fa', 'jazz')
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
