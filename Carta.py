class Carta:

    carta :int

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