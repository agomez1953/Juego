import sys
import blackjackui
import gamestart
from UIfunctions import *
from gamefunctions import *


class main(QtGui.QMainWindow):
       
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = blackjackui.Ui_Blackjack()
        self.ui.setupUi(self)
        
        self.ui.btnBet.clicked.connect(self.betClicked)
        self.ui.btnStay.clicked.connect(self.stayClicked)
        self.ui.btnDouble.clicked.connect(self.doubleClicked)
        self.ui.btnHit.clicked.connect(self.hitClicked)
        
        self.deck = deck()
        self.aparato = create_shoe(self.deck, 1)  #creates a deck of cards to be used during the game
        
        #sets up the initial game conditions
        self.dinero = 500
        self.ui.labMoney.setText(str(self.dinero))
        self.manos = []
        self.apuesta = 0
        
        #list of card graphics in the ui
        self.mano_dealer = [self.ui.dCard, self.ui.dCard_2, self.ui.dCard_3, self.ui.dCard_4, self.ui.dCard_5, self.ui.dCard_6, self.ui.dCard_7, self.ui.dCard_8, self.ui.dCard_9, self.ui.dCard_10]
        self.mano_jugador = [self.ui.pCard, self.ui.pCard_2, self.ui.pCard_3, self.ui.pCard_4, self.ui.pCard_5, self.ui.pCard_6, self.ui.pCard_7, self.ui.pCard_8, self.ui.pCard_9, self.ui.pCard_10]
        
        #disables all buttons that control the hand
        buttoncontrol(self.ui)

    def betClicked(self):
        try:
            if (int(self.ui.lineBet.text()) > self.dinero or int(self.ui.lineBet.text()) < 0):
                self.ui.labWarning.setText("Please enter a number less than " + str(self.dinero) + " and greater than 0")
            else:
                betfunction(self)
        except:
            self.ui.labWarning.setText("Please enter a number less than " + str(self.dinero) + " and greater than 0")

        self.ui.lineBet.clear()
                          

    def hitClicked(self):
        '''usuario que muestra la tarjeta que se acaba de agregar a la mano'''
        self.ui.btnDouble.setEnabled(False)
        hit(self.manos[1], self.aparato)
        
        #determines the position of the last card added to the hand and shows it
        i = len(self.manos[1])-1
        showcard(self.mano_jugador[i], self.manos[1][i])
        self.ui.labPlayer.setText(str(puntos_mano(self.manos[1])))
        
        #if player busts takes player to end of the game automatically
        if(puntos_mano(self.manos[1])>21):
            self.stayClicked()
    

    def doubleClicked(self):
        '''handles the case where the player doubles the bet by adding to the bet and getting one more card'''
        self.dinero -= self.apuesta
        self.apuesta *= 2
        self.ui.labMoney.setText(str(self.dinero))
        hit(self.manos[1],self.aparato)
        i = len(self.manos[1])-1
        showcard(self.mano_jugador[i], self.manos[1][i])
        self.ui.labPlayer.setText(str(puntos_mano(self.manos[1])))
        self.stayClicked()
        
    
    def stayClicked(self):
        '''handles endgame situation and has the dealer play out hand and calculates winnings'''
        #turns off all play buttons and activates btnBet
        buttoncontrol(self.ui)
        winner = calculos(self.manos[0], self.manos[1], self.aparato)  #calls function to see which hand won
        
        #shows the dealers cards and how many points it is worth in the ui
        self.ui.labDealer.setText(str(puntos_mano(self.manos[0])))
        for i in range(0, len(self.manos[0])):
            showcard(self.mano_dealer[i], self.manos[0][i])
        
        self.dinero += ganancias(self.apuesta, winner)  #updates self.money based on bet
        self.ui.labMoney.setText(str(self.dinero))
    
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    Window = main()
    Window.show()    
    app.exec_()
