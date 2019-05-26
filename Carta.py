class Carta:
    """
    T = trebol
    P = picas
    C = corazones
    D = diamantes
    """
    carta :int
    baraja = {'TA':1,'T2':2,'T3':3,'T4':4,'T5':5,'T6':6,'T7':7,'T8':8,'T9':9,'T10':10,'TJ':10,'TQ':10,'TK':10,
    'PA':1,'P2':2,'P3':3,'P4':4,'P5':5,'P6':6,'P7':7,'P8':8,'P9':9,'P10':10,'PJ':10,'PQ':10,'PK':10,
    'CA':1,'C2':2,'C3':3,'C4':4,'C5':5,'C6':6,'C7':7,'C8':8,'C9':9,'C10':10,'CJ':10,'CQ':10,'CK':10,
    'DA':1,'D2':2,'D3':3,'D4':4,'D5':5,'D6':6,'D7':7,'D8':8,'D9':9,'D10':10,'DJ':10,'DQ':10,'DK':10
              }


    def __init__(self,valor,figura):
        """
        Esta funcion sirve como constructor
        :param valor: esta variable es el valor de la carta
        :param figura: esta variable es la figura de la carta
        """
        self.valor = valor
        self.figura = figura

    def __repr__(self):
        """
        Esta funcion es para imprimir cada uno de las cartas
        :return:
        """
        return f'La carta es{self.figura,self.valor}'

    def __eq__(self, other):
        """
        Esta funcion compara las cartas para ver si son iguales o no.
        :param other:
        :return:
        """
        return self.valor == other.valor and self.figura == other.figura

    def baraja(self,figura,valor):
        self.figura1 = figura
        self.figura2 = figura
        self.figura3 = figura
        self.figura4 = figura

        self.figura1 = 'Treboles'
        self.figura2 = 'Picas'
        self.figura3 = 'Corazones'
        self.figura4 = 'Diamantes'
    def comparar(self):
        if self.valor > 21:
            print('Pierdes')
        while(self.carta == 2):
            if self.valor == 21:
                print('BlackJack')

