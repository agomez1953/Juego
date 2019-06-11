from unittest import TestCase
from mesa import *
import mesa as Test

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
         # self.assertEqual(Test.Baraja(), ['P9', 'C9', 'D9', 'T9', 'P2', 'C2', 'D2', 'T2', 'P10', 'C10', 'D10', 'T10', 'P7', 'C7', 'D7', 'T7', 'P4', 'C4', 'D4', 'T4', 'PJ', 'CJ', 'DJ', 'TJ', 'PA', 'CA',
         #                                   'DA', 'TA', 'P8', 'C8', 'D8', 'T8', 'PQ', 'CQ', 'DQ', 'TQ', 'PK', 'CK', 'DK', 'TK', 'P3', 'C3', 'D3', 'T3', 'P6', 'C6', 'D6', 'T6', 'P5', 'C5', 'D5', 'T5'])
        pass
    def test_crear_aparato(self):
        self.assertEqual(Test.crear_aparato(['A10', 'DA', 'TA', 'P8', 'C8', 'D8', 'T8', 'PQ', 'CQ'], ['51']), {'A10': ['51'], 'C8': ['51'], 'CQ': ['51'], 'D8': ['51'], 'DA': ['51'], 'P8': ['51'], 'PQ': ['51'], 'T8': ['51'], 'TA': ['51']})

    def test_repartir_carta(self):
        aparato = {'A10': ['51'], 'C8': ['51']}

        # self.addTypeEqualityFunc(Test.repartir_carta(aparato), 1)
        pass
