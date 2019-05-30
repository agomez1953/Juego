from random import randint

class Baraja:

    __VALORES__ = {'TA':1,'T2':2,'T3':3,'T4':4,'T5':5,'T6':6,'T7':7,'T8':8,'T9':9,'T10':10,'TJ':10,'TQ':10,'TK':10,
                       'PA':1,'P2':2,'P3':3,'P4':4,'P5':5,'P6':6,'P7':7,'P8':8,'P9':9,'P10':10,'PJ':10,'PQ':10,'PK':10,
                       'CA':1,'C2':2,'C3':3,'C4':4,'C5':5,'C6':6,'C7':7,'C8':8,'C9':9,'C10':10,'CJ':10,'CQ':10,'CK':10,
                       'DA':1,'D2':2,'D3':3,'D4':4,'D5':5,'D6':6,'D7':7,'D8':8,'D9':9,'D10':10,'DJ':10,'DQ':10,'DK':10}

    defecto = ['TA','T2','T3','T4','T5','T6','T7','T8','T9','T10','TJ','TQ','TK',
               'PA','P2','P3','P4','P5','P6','P7','P8','P9','P10','PJ','PQ','PK',
               'CA','C2','C3','C4','C5','C6','C7','C8','C9','C10','CJ','CQ','CK',
               'DA','D2','D3','D4','D5','D6','D7','D8','D9','D10','DJ','DQ','DK']

    def __init__(self):
        self.estado = self.defecto.copy()

    def barajar(self):
        copia = self.defecto.copy()
        resultado = []

        while copia:
            pos = randint(0, len(copia) -1)
            resultado.append(copia.pop(pos))

        self.estado = resultado

    def entregar(self):

        return self.estado.pop()