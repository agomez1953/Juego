from PyQt4 import QtGui
import mesa
import funciones_juego
import os

def showcard (card_ui, carta):
    '''Toma la imagen de la tarjeta de la clase de tarjeta en mesa y la muestra en la interfaz ui'''
    image = QtGui.QPixmap.fromImage(carta.getgraphic())
    pixmap = QtGui.QPixmap(image)
    card_ui.setPixmap(pixmap)
    card_ui.setHidden(False)
    return 

def showback(card_ui):
    '''muestra el reverso de una tarjeta para la tarjeta boca abajo de los distribuidores en el ui'''
    path = os.getcwd()
    image = QtGui.QImage(path + '/cartas/back.png')
    pixmap = QtGui.QPixmap(image)
    card_ui.setPixmap(pixmap)
    card_ui.setHidden(False)
    return

def hidecards(list1,list2):
    '''oculta las imagenes de la tarjeta en la interfaz de usuario hasta que se llaman con la funcion showcard'''
    for i in range(0, len(list1)):
        list1[i].setHidden(True)
        list2[i].setHidden(True)
    return

def buttoncontrol(ui):
    '''establece todos los botones a las condiciones iniciales con las apuestas como la unica opcion'''
    ui.btnHit.setEnabled(False)
    ui.btnDouble.setEnabled(False)
    ui.btnStay.setEnabled(False)      
    ui.btnBet.setEnabled(True)
    ui.btnIni.setEnabled(False)



    
def betfunction(self):
        
    self.ui.btnBet.setEnabled(False)
    self.ui.labWarning.clear()
    hidecards(self.mano_dealer, self.mano_jugador)
         
    self.manos = funciones_juego.inicializar_cartas(self.aparato)
    self.apuesta = [0]
    twenty_one = [False, False]

    showcard(self.ui.dCard, self.manos[0][0])
    showback(self.ui.dCard_2)

    for i in range(0, len(self.manos[1])):
        showcard(self.mano_jugador[i], self.manos[1][i])
            
    self.apuesta = int(self.ui.lineBet.text())
    self.dinero -= self.apuesta
    self.ui.labMoney.setText(str(self.dinero))
        
        
    self.ui.labDealer.setText(str(self.manos[0][0].getpunto()))
    self.ui.labPlayer.setText(str(funciones_juego.puntos_mano(self.manos[1])))
    for i in range(0,2):
        if funciones_juego.blackjack_dealer(self.manos[i]) == True:
            twenty_one[i] = True
    if twenty_one != [False, False]:
        self.ui.labDealer.setText(str(funciones_juego.puntos_mano(self.manos[0])))
        showcard(self.mano_dealer[1], self.manos[0][1])
        if twenty_one == [True, True]:
            self.dinero += funciones_juego.ganancias(self.apuesta, 1)
        elif twenty_one == [False, True]:
            self.dinero += int(funciones_juego.ganancias(self.apuesta, 2.5))
            
        self.ui.labMoney.setText(str(self.dinero))
        buttoncontrol(self.ui)

    else:
        self.ui.btnHit.setEnabled(True)
        self.ui.btnDouble.setEnabled(True)
        self.ui.btnStay.setEnabled(True)