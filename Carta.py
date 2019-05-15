class Carta:

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


