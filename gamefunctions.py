from gamestart import *
base_deck = deck()

def inicializar_cartas(aparato):
    '''deals 2 cards to player and dealer returns dealer hand as
    first hand player hand as second in a list'''
    mano_jugador = [repartir_carta(aparato)]
    mano_dealer = [repartir_carta(aparato)]
    mano_jugador.append(repartir_carta(aparato))
    mano_dealer.append(repartir_carta(aparato))
    return [mano_dealer, mano_jugador]

def blackjack_dealer(manos):
    '''checks to see if either of the first hands dealt are blackjack'''
    if puntos_mano(manos) == 21:
        return True
    else:
        return False        

def split(mano, aparato):
    '''if hand size is < 2, will add card else check for equal rank if
    they will it will offer to split and then create append that to hands
    update bet to represent this as well.  Returns 0 if no split else returns
    the card'''
    
    if len(mano) == 2 and mano[0].getrango() == mano[1].getrango():
        accion = input("Would you like to split?\n")
        if accion == 'y':
            carta = mano.pop()
            hit(mano,aparato)
            return carta
    return 0
    
def double(mano, aparato):
    '''checks if player would like to double their bet and provides a hit'''
    accion = input("Would you like to double? \n")
    if accion == 'y':
        hit(mano, aparato)
        return 2
    else:
        return 0

def hit(mano, aparato):
    '''adds a card to the hand, performs a hit'''
    mano.append(repartir_carta(aparato))
    return mano
       
def dealer_play(mano_dealer, aparato):
    '''lets dealer play with standard rule of hit on 16 stay on 17'''
    total = puntos_mano(mano_dealer)
    
    if total < 17:
        mano_dealer=(hit(mano_dealer, aparato))
        dealer_play(mano_dealer, aparato)       #recurrsive call to hit again
        
    else:
        return

def puntos_mano(mano):
    '''gives the value of the hand'''
    total = 0
    for cartas in mano:
        total += cartas.getpunto()   #gets values for cards

    if total > 21:
        for cartas in mano:   #makes ace =1 if 21 is overshot
            if cartas.getrango() == 'A':
                total -= 10
                if total <= 21:
                    break
    
    return total

def calculos(dealer, player, aparato):
    '''calculates the values for each hand and returns the rate of return of the hand'''
    player_total = puntos_mano(player)
    if player_total > 21:  #lose condition
        return 0

    else:
        dealer_play(dealer, aparato)
        dealer_total = puntos_mano(dealer)
        
        if dealer_total > 21:
            return 2
        elif dealer_total < player_total: #win condition
            return 2
        elif dealer_total == player_total:  #push condition
            return 1
        else:  #lose conition
            return 0
        
def ganancias(apuesta, rate):
    '''Updates the amount of money the player has based on how much they won'''
    return apuesta * rate
