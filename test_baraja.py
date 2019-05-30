from unittest import TestCase
from Baraja import Baraja
import time

class TestBaraja(TestCase):

    def test_barajar(self):
        dado = Baraja()
        print({dado.estado})
        time.sleep(2)
        dado.barajar()
        print(f'{dado.estado}')

    def test_entregar(self):
        dado = Baraja()
        dado.barajar()
        print(f'{dado.estado}')
        espero_long = 51
        tipo_esperado = type('')
        entrega = dado.entregar()
        print(f'{dado.estado}')
        self.assertEqual(tipo_esperado, type(entrega))
        self.assertEqual(espero_long, len(dado.estado))