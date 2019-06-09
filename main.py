import sys
import blackjackui
import mesa
from UIcomplilacion import *
from funciones_juego import *


class main(QtGui.QMainWindow):
       
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = blackjackui.Ui_Blackjack()
        self.ui.setupUi(self)
        
        self.ui.btnBet.clicked.connect(self.betClick)
        self.ui.btnStay.clicked.connect(self.stayClicked)
        self.ui.btnIni.clicked.connect(self.iniClick)
        # self.ui.btnDouble.clicked.connect(self.doubleClicked)
        self.ui.btnHit.clicked.connect(self.hitClick)
        
        self.Baraja = Baraja()
        self.aparato = crear_aparato(self.Baraja, 1)
        

        self.dinero = 500
        self.ui.labMoney.setText(str(self.dinero))
        self.manos = []
        self.apuesta = 0
        

        self.mano_dealer = [self.ui.dCard, self.ui.dCard_2, self.ui.dCard_3, self.ui.dCard_4, self.ui.dCard_5, self.ui.dCard_6, self.ui.dCard_7, self.ui.dCard_8, self.ui.dCard_9, self.ui.dCard_10]
        self.mano_jugador = [self.ui.pCard, self.ui.pCard_2, self.ui.pCard_3, self.ui.pCard_4, self.ui.pCard_5, self.ui.pCard_6, self.ui.pCard_7, self.ui.pCard_8, self.ui.pCard_9, self.ui.pCard_10]
        

        buttoncontrol(self.ui)

    def betClick(self):
        try:
            if (int(self.ui.lineBet.text()) > self.dinero or int(self.ui.lineBet.text()) <= 0):
                self.ui.labWarning.setText("Ingrese un numero menor a " + str(self.dinero) + " y mayor que 0")
            elif self.dinero == 0:
                self.ui.labWarning.setText("Ya no tiene dinero")
            else:
                betfunction(self)
        except:
            self.ui.labWarning.setText("Ingrese un numero menor a " + str(self.dinero) + " y meyor que 1")

        self.ui.lineBet.clear()
        self.ui.btnIni.setEnabled(True)
                          

    def hitClick(self):

        '''usuario que muestra la tarjeta que se acaba de agregar a la mano'''

        # self.ui.btnDouble.setEnabled(False)
        hit(self.manos[1], self.aparato)
        i = len(self.manos[1])-1
        showcard(self.mano_jugador[i], self.manos[1][i])
        self.ui.labPlayer.setText(str(puntos_mano(self.manos[1])))
        

        if(puntos_mano (self.manos[1]) > 21):
            self.stayClicked()

    def iniClick(self):
        self.Baraja = Baraja()
        self.aparato = crear_aparato(self.Baraja, 1)

        self.dinero = 500
        self.ui.labMoney.setText(str(self.dinero))
        self.manos = []
        self.apuesta = 0

        self.mano_dealer = [self.ui.dCard, self.ui.dCard_2, self.ui.dCard_3, self.ui.dCard_4, self.ui.dCard_5,
                            self.ui.dCard_6, self.ui.dCard_7, self.ui.dCard_8, self.ui.dCard_9, self.ui.dCard_10]
        self.mano_jugador = [self.ui.pCard, self.ui.pCard_2, self.ui.pCard_3, self.ui.pCard_4, self.ui.pCard_5,
                             self.ui.pCard_6, self.ui.pCard_7, self.ui.pCard_8, self.ui.pCard_9, self.ui.pCard_10]

        buttoncontrol(self.ui)


    # def doubleClicked(self):
    #
    #     '''maneja el caso donde el jugador duplica la apuesta agregando a la apuesta y obteniendo una carta mas'''
    #
    #     self.dinero -= self.apuesta
    #     self.apuesta *= 2
    #     self.ui.labMoney.setText(str(self.dinero))
    #     hit(self.manos[1],self.aparato)
    #     i = len(self.manos[1])-1
    #     showcard(self.mano_jugador[i], self.manos[1][i])
    #     self.ui.labPlayer.setText(str(puntos_mano(self.manos[1])))
    #     self.stayClicked()
        
    
    def stayClicked(self):

        '''maneja la situacion del juego final y hace que el crupier juegue la mano y calcula las ganancias'''

        buttoncontrol(self.ui)
        winner = calculos(self.manos[0], self.manos[1], self.aparato)
        self.ui.labDealer.setText(str(puntos_mano(self.manos[0])))
        for i in range(0, len(self.manos[0])):
            showcard(self.mano_dealer[i], self.manos[0][i])
        
        self.dinero += ganancias(self.apuesta, winner)
        self.ui.labMoney.setText(str(self.dinero))
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Window = main()
    Window.show()    
    app.exec_()
