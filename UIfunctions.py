from PyQt4 import QtGui
import gamestart
import gamefunctions
import os

def showcard (card_ui, carta):
    '''Takes the image of the card from the card class in gamestart  and shows it on the ui'''
    image = QtGui.QPixmap.fromImage(carta.getgraphic())
    pixmap = QtGui.QPixmap(image)
    card_ui.setPixmap(pixmap)
    card_ui.setHidden(False)
    return 

def showback(card_ui):
    '''shows the back of a card for the dealers face down card in the ui'''
    path = os.getcwd()  #gets current directory to use to find the image of the back of the card
    image = QtGui.QImage(path + '/cartas/back.png')
    pixmap = QtGui.QPixmap(image)
    card_ui.setPixmap(pixmap)
    card_ui.setHidden(False)
    return

def hidecards(list1,list2):
    '''hides the card images in the ui until they are called with the showcard function'''
    for i in range(0, len(list1)):
        list1[i].setHidden(True)
        list2[i].setHidden(True)
    return

def buttoncontrol(ui):
    '''sets all buttons to initial conditions with betting the only option'''
    ui.btnHit.setEnabled(False)
    ui.btnDouble.setEnabled(False)
    ui.btnStay.setEnabled(False)      
    ui.btnBet.setEnabled(True)
    
def betfunction(self):
        
    self.ui.btnBet.setEnabled(False)
    self.ui.labWarning.clear()
    hidecards(self.mano_dealer, self.mano_jugador) #calls function to hide the card graphics in the ui
        
    #Sets starting conditions of self.money and a starting self.shoe        
         
    self.manos = gamefunctions.inicializar_cartas(self.aparato)
    self.apuesta = [0] #list containing the initial bet and all bets for each hand
    twenty_one = [False, False]
            
    #shows intial cards for dealer ui
    showcard(self.ui.dCard, self.manos[0][0])
    showback(self.ui.dCard_2)
        
    #shows initial cards for player in ui
    for i in range(0, len(self.manos[1])):
        showcard(self.mano_jugador[i], self.manos[1][i])
            
    self.apuesta = int(self.ui.lineBet.text())
    self.dinero -= self.apuesta
    self.ui.labMoney.setText(str(self.dinero))
        
        
    self.ui.labDealer.setText(str(self.manos[0][0].getpunto()))
    self.ui.labPlayer.setText(str(gamefunctions.puntos_mano(self.manos[1])))
    for i in range(0,2):
        if gamefunctions.blackjack_dealer(self.manos[i]) == True:
            twenty_one[i] = True
    if twenty_one != [False, False]:
        self.ui.labDealer.setText(str(gamefunctions.puntos_mano(self.manos[0])))
        showcard(self.mano_dealer[1], self.manos[0][1])
        if twenty_one == [True, True]:                 #checks to see if both hands have blackjack
            self.dinero += gamefunctions.ganancias(self.apuesta, 1)
        elif twenty_one == [False, True]:                                         #check to see if the player has blackjack
            self.dinero += int(gamefunctions.ganancias(self.apuesta, 2.5))
            
        self.ui.labMoney.setText(str(self.dinero))
        buttoncontrol(self.ui)
                                                    #check to see if the dealer had blackjack
                
            
    else:   #Enables all the buttons to control the self.hands
        self.ui.btnHit.setEnabled(True)
        self.ui.btnDouble.setEnabled(True)
        self.ui.btnStay.setEnabled(True)
