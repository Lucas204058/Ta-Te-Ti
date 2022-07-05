import random


def dibujarTablero(tablero):
 print('   |   |')
 print(' ' + tablero[7] + ' | ' + tablero[8] + ' | ' + tablero[9])
 print('   |   |')
 print('-----------')
 print('   |   |')
 print(' ' + tablero[4] + ' | ' + tablero[5] + ' | ' + tablero[6])
 print('   |   |')
 print('-----------')
 print('   |   |')
 print(' ' + tablero[1] + ' | ' + tablero[2] + ' | ' + tablero[3])
 print('   |   |')

def ingresaLetraJugador():
    letra = ""
    while not(letra == "X" or letra == "O"):
        print("¿Deseas ser X o O?")
        letra = input().upper()
        
    if letra == "X":
        return ["O", "X"]
    else:
        return ["X", "O"]

def quienComienza():
    if random.randint(0, 1) == 0:
        return "la computadora"
    else:
        return "El jugador"
    
def jugarDeNuevo():
    print("¿Deseas volver a jugar? (si/no)?")
    return input().lower().startswith("S")

def hacerJugada(tablero, letra, jugada):
    tablero[jugada] = letra
    
def esGanador(ta, le):
    return((ta[7] == le and ta[8] == le and ta[9] == le)or
    (ta[4] == le and ta[5] == le and ta[6] == le)or
    (ta[1] == le and ta[2] == le and ta[3] == le)or
    (ta[7] == le and ta[4] == le and ta[1] == le)or
    (ta[8] == le and ta[5] == le and ta[2] == le)or
    (ta[9] == le and ta[6] == le and ta[3] == le)or
    (ta[7] == le and ta[5] == le and ta[3] == le)or
    (ta[9] == le and ta[5] == le and ta[1] == le)or