
import os


def imprimirTablero(tablero):
    for i in range(3):
        print(f' {tablero[i][0]} | {tablero[i][1]}  | {tablero[i][2]}  ')


def entrada(tablero,turno):
    print(f'Tira {turno}')
    posicion = input('Ingresa la coordenada: ')
    pt = posicion.split(',')
    for elem in pt:
        if int(elem) not in range(0,3):
            print('Coordenada no valida')
            entrada(tablero, turno)

    if tablero[int(pt[0])][int(pt[1])] == '-':
        tablero[int(pt[0])][int(pt[1])] = turno
    else:
        print('Posicion ocupada, elige otro lugar')
        entrada(tablero, turno)
    return tablero


def no_terminado(tablero):
    for i in range(3):
            #Linea horizontal
            if tablero[i][0] != '-' and tablero[i][1] != '-' and tablero[i][2] != '-':
                if tablero[i][0] == tablero[i][1] and tablero[i][1] == tablero[i][2]:
                    print(f'Gana jugador {tablero[i][0]}')
                    return False
            #Linea hacia vertical
            elif tablero[0][i] != '-' and tablero[1][i] != '-' and tablero[2][i] != '-':
                if tablero[0][i] == tablero[1][i] and tablero[1][i] == tablero[2][i]:
                    print(f'Gana jugador {tablero[0][i]}')
                    return False
                
    #diagonal 
    if tablero[0][0] != '-' and tablero[1][1] != '-' and tablero[2][2] != '-':
         if tablero[0][0] == tablero[1][1] and tablero[1][1] == tablero[2][2]:
            print(f'Gana jugador {tablero[0][0]}')
            return False
    elif tablero[0][2] != '-' and tablero[1][1] != '-' and tablero[2][0] != '-':
         if tablero[0][2] == tablero[1][1] and tablero[1][1] == tablero[2][0]:
            print(f'Gana jugador {tablero[0][2]}')
            return False

    return True


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)



def run():
    tablero = [['-','-','-'],['-','-','-'],['-','-','-']]
    contador = 1
    imprimirTablero(tablero)
    print('')
    while(no_terminado(tablero)):
        if contador % 2 == 0:
            tablero = entrada(tablero,'X')
        else: 
            tablero = entrada(tablero,'O')
        clearConsole()
        imprimirTablero(tablero)
        contador += 1 


if __name__ == '__main__':
    run()