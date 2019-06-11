from mesa import *
base_baraja = Baraja()

def inicializar_cartas(aparato):

    '''Funcion repartir 2 cartas al jugador y el reparto devuelve la mano del
    repartidor como mano de primera mano como segundo en una lista'''

    mano_jugador = [repartir_carta(aparato)]
    mano_dealer = [repartir_carta(aparato)]
    mano_jugador.append(repartir_carta(aparato))
    mano_dealer.append(repartir_carta(aparato))
    return [mano_dealer, mano_jugador]

def blackjack_dealer(manos):

    '''Funcion blackjack'''

    if puntos_mano(manos) == 21:
        return True
    else:
        return False        

def split(mano, aparato):

    ''' funcion mano es menor a 2, agregara una tarjeta
     Se ofrecera dividir y luego agregar eso a las manos
     Actualizar apuesta para representar esto tambien
     Devuelve 0 si no hay ninguna otra division devuelve la tarjeta'''
    
    if len(mano) == 2 and mano[0].getrango() == mano[1].getrango():
        accion = input("Te gustaria doblar?\n")
        if accion == 'y' or 's':
            carta = mano.pop()
            hit(mano, aparato)
            return carta
    return 0
    
def double(mano, aparato):

    '''Funcion que comprueba si el jugador quiere duplicar su apuesta y proporciona un hit'''

    accion = input("Quieres doblar la apuesta? \n")
    if accion == 'y' or 's':
        hit(mano, aparato)
        return 2
    else:
        return 0

def hit(mano, aparato):

    '''funcion anadir una carta a la mano, realiza un hit'''

    mano.append(repartir_carta(aparato))
    return mano
       
def dealer_play(mano_dealer, aparato):
    '''funcion que le permite al dealer jugar con la regla estandar de hit en 16 se quedarse en 17'''
    total = puntos_mano(mano_dealer)
    
    if total < 17:
        mano_dealer = (hit(mano_dealer, aparato))
        dealer_play(mano_dealer, aparato)
        
    else:
        return

def puntos_mano(mano):

    '''Funcion valor mano'''

    total = 0
    for cartas in mano:
        total += cartas.getpunto()   #elaluar metodos gets a cartas

    if total > 21:
        for cartas in mano:
            if cartas.getrango() == 'A':
                total -= 10
                if total <= 21:
                    break
    
    return total

def calculos(dealer, player, aparato):

    '''calcula los valores para cada mano y devuelve la tasa de retorno de la mano'''

    player_total = puntos_mano(player)
    if player_total > 21:
        return 0

    else:
        dealer_play(dealer, aparato)
        dealer_total = puntos_mano(dealer)
        
        if dealer_total > 21:
            return 2
        elif dealer_total < player_total:
            return 2
        elif dealer_total == player_total:
            return 1
        else:
            return 0
        
def ganancias(apuesta, rate):

    '''Actualiza la cantidad de dinero que el jugador tiene y  gano'''

    return apuesta * rate
