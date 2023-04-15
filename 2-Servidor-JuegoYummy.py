#!/usr/bin python3
import socket
import random
import time

# Devuelve la eleccion de fichas para Cliente y Servidor
def eleccionFichas():

    fichaCliente="x"
    fichaServidor="o"

    return fichaCliente, fichaServidor

# Imprime el tablero de 3x3 en modo principiante
def imprimirTablero3x3(tablero3x3):
    print("\n")
    print(tablero3x3[0], " | ", tablero3x3[1], " | ", tablero3x3[2])
    print("-------------")
    print(tablero3x3[3], " | ", tablero3x3[4], " | ", tablero3x3[5])
    print("-------------")
    print(tablero3x3[6], " | ", tablero3x3[7], " | ", tablero3x3[8])
    print("\n")

# Imprime el tablero de 5x5 en modo avanzado
def imprimirTablero5x5(tablero5x5):
    print("\n")
    print(tablero5x5[0], " | ", tablero5x5[1], " | ", tablero5x5[2], " | ", tablero5x5[3], " | ", tablero5x5[4])
    print("-------------------------")
    print(tablero5x5[5], " | ", tablero5x5[6], " | ", tablero5x5[7], " | ", tablero5x5[8], " | ", tablero5x5[9])
    print("-------------------------")
    print(tablero5x5[10], " | ", tablero5x5[11], " | ", tablero5x5[12], " | ", tablero5x5[13], " | ", tablero5x5[14])
    print("-------------------------")
    print(tablero5x5[15], " | ", tablero5x5[16], " | ", tablero5x5[17], " | ", tablero5x5[18], " | ", tablero5x5[19])
    print("-------------------------")
    print(tablero5x5[20], " | ", tablero5x5[21], " | ", tablero5x5[22], " | ", tablero5x5[23], " | ", tablero5x5[24])
    print("\n")

# Comprobamos de forma vertical, horizontal y diagonal si existe ganador en 3x3
def comprobarGanador3x3(tablero3x3, jugador):
    if tablero3x3[0] == tablero3x3[1] == tablero3x3[2] == jugador or tablero3x3[3] == tablero3x3[4] == tablero3x3[5] == jugador or tablero3x3[6] == tablero3x3[7] == tablero3x3[8] == jugador or tablero3x3[0] == tablero3x3[3] == tablero3x3[6] == jugador or tablero3x3[1] == tablero3x3[4] == tablero3x3[7] == jugador or tablero3x3[2] == tablero3x3[5] == tablero3x3[8] == jugador or tablero3x3[0] == tablero3x3[4] == tablero3x3[8] == jugador or tablero3x3[2] == tablero3x3[4] == tablero3x3[6] == jugador:
        return True
    else:
        return False

# Comprobamos de forma vertical, horizontal y diagonal si existe ganador 5x5
def comprobarGanador5x5(tablero5x5, jugador):
    if tablero5x5[0] == tablero5x5[1] == tablero5x5[2] == tablero5x5[3] == tablero5x5[4] == jugador or \
       tablero5x5[5] == tablero5x5[6] == tablero5x5[7] == tablero5x5[8] == tablero5x5[9] == jugador or \
       tablero5x5[10] == tablero5x5[11] == tablero5x5[12] == tablero5x5[13] == tablero5x5[14] == jugador or \
       tablero5x5[15] == tablero5x5[16] == tablero5x5[17] == tablero5x5[18] == tablero5x5[19] == jugador or \
       tablero5x5[20] == tablero5x5[21] == tablero5x5[22] == tablero5x5[23] == tablero5x5[24] == jugador or \
       tablero5x5[0] == tablero5x5[5] == tablero5x5[10] == tablero5x5[15] == tablero5x5[20] == jugador or \
       tablero5x5[1] == tablero5x5[6] == tablero5x5[11] == tablero5x5[16] == tablero5x5[21] == jugador or \
       tablero5x5[2] == tablero5x5[7] == tablero5x5[12] == tablero5x5[17] == tablero5x5[22] == jugador or \
       tablero5x5[3] == tablero5x5[8] == tablero5x5[13] == tablero5x5[18] == tablero5x5[23] == jugador or \
       tablero5x5[4] == tablero5x5[9] == tablero5x5[14] == tablero5x5[19] == tablero5x5[24] == jugador or \
       tablero5x5[0] == tablero5x5[6] == tablero5x5[12] == tablero5x5[18] == tablero5x5[24] == jugador or \
       tablero5x5[4] == tablero5x5[8] == tablero5x5[12] == tablero5x5[16] == tablero5x5[20] == jugador:
        return True
    else:
        return False


# Comprobamos que el tablero este lleno
def tableroLleno(tablero):
    for i in tablero:
        if i == " ":
            return False
    else:
        return True

# Comprobamos que haya casillas libres
def casillaLibre(tablero3x3, casilla):
    return tablero3x3[casilla] == " "

# Se verifican los movimientos del cliente 3x3
# En la version del servidor no se necesita tal funcion para mover las casillas
def movimientoCliente(tablero3x3):
    posiciones=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    posicion=None
    while True:
        if posicion not in posiciones:
            # El servidor recibe la posicion del cliente
            posicion=str(ClientConn.recv(buffer_size), "utf-8")
        else:
            posicion=int(posicion)
            if not casillaLibre(tablero3x3, posicion-1):
                print("Posicion ocupada.")
                # Si la posicion esta ocupada el servidor manda mensaje que esta ocupada y vuelve a ingresar una posicion
                ClientConn.sendall(bytes("Posicion ocupada", "utf-8"))
            else:
                return posicion-1

#Movimientos Tablero5x5
def movimientoCliente5x5(tablero5x5):
    posiciones=["1", "2", "3", "4", "5", "6", "7", "8", "9","10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25"]
    posicion=None
    while True:
        if posicion not in posiciones:
            posicion=input("Elige una posicion del 1 al 25:\n")
        else:
            posicion=int(posicion)
            if not casillaLibre(tablero5x5, posicion-1):
                print("Posicion ocupada.")
            else:
                return posicion-1


# Se verifican los movimientos del servidor 3x3
def movimientoServidor(tablero3x3, jugador):
    for i in range(9):
        copia = list(tablero3x3)
        if casillaLibre(copia, i):
            copia[i] = jugador
            if comprobarGanador3x3(copia, jugador):
                return i
    while True:
        casilla = random.randint(0, 8)
        if not casillaLibre(tablero3x3, casilla):
            casilla = random.randint(0, 8)
        else:
            return casilla


# Se verifican los movimientos del servidor
def movimientoServidor5x5(tablero5x5, jugador):
    for i in range(25):
        copia = list(tablero5x5)
        if casillaLibre(copia, i):
            copia[i] = jugador
            if comprobarGanador5x5(copia, jugador):
                return i
    while True:
        casilla = random.randint(0, 24)
        if not casillaLibre(tablero5x5, casilla):
            casilla = random.randint(0, 24)
        else:
            return casilla

# Variables para el servidor
HOST = "127.0.0.1"
PORT = 65432
buffer_size = 1024

#Conexion del servidor
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPServerSocket:
    TCPServerSocket.bind((HOST, PORT))
    TCPServerSocket.listen()
    print("El servidor esta esperando a el cliente para conectarse al juego.")
    # Se acepta la conexion
    ClientConn, ClientAddr = TCPServerSocket.accept()
    with ClientConn:
        print("Conectado a", ClientAddr)
        print("El servidor esta esperando la dificultad del juego...")
        # Recibimos el mensaje del cliente
        data = str(ClientConn.recv(buffer_size), "utf-8") #Con utf-8 se quita el formato de bytes.
        print("El servidor ha recibido la dificultad del juego: ",data, end="\n")
        #Se checa la dificultad del juego.
        #Inicializamos las variables del juego
        tablero3x3 = [" "] * 9
        tablero5x5 = [" "] * 25
        cliente, servidor = eleccionFichas()
        # Se imprime un tablero en la aplicacion servidor dependiendo de la dificultad
        if not data:
            TCPServerSocket.close()
        elif data == "1":
            imprimirTablero3x3(tablero3x3)
        elif data == "2":
            imprimirTablero5x5(tablero5x5)
        # Se elige la ficha x para cliente y la o para el servidor
        if cliente == "x":
            turno = "Cliente"
        else:
            turno = "Servidor"
        # Enviar mensaje de confirmación al cliente
        ClientConn.send("Servidor: ¡Inicia el juego!".encode())
        #Inicia el juego
        start_time = time.time()
        partida = True
        while partida:
            if not data:
                break
            elif data == "1":
                if tableroLleno(tablero3x3):
                    print("¡Empate!")
                    ClientConn.sendall(bytes("empate","utf-8"))
                    partida = False
                    TCPServerSocket.close()
                elif turno == "Cliente":
                    casilla = movimientoCliente(tablero3x3)
                    tablero3x3[casilla] = cliente
                    turno = "Servidor"
                    imprimirTablero3x3(tablero3x3)
                    if comprobarGanador3x3(tablero3x3, cliente):
                        print("¡Gano el cliente!")
                        ClientConn.sendall(bytes("ganaste","utf-8"))
                        partida = False
                        TCPServerSocket.close()
                elif turno == "Servidor":
                    print("El servidor esta pensando...")
                    time.sleep(2)
                    casilla = movimientoServidor(tablero3x3, servidor)
                    tablero3x3[casilla] = servidor
                    # Enviamos la posicion del servidor
                    movimiento_servidor = str(casilla+1)
                    ClientConn.sendall(bytes(movimiento_servidor, "utf-8"))
                    turno = "Cliente"
                    imprimirTablero3x3(tablero3x3)
                    print(f"El servidor eligio la posicion {movimiento_servidor}")
                    if comprobarGanador3x3(tablero3x3, servidor):
                        print("¡Has perdido!")
                        ClientConn.sendall(bytes("perdiste","utf-8"))
                        partida = False
                        TCPServerSocket.close()
            elif data == "2":
                if tableroLleno(tablero5x5):
                    print("¡Empate!")
                    ClientConn.sendall(bytes("empate", "utf-8"))
                    partida = False
                    TCPServerSocket.close()
                elif turno == "Cliente":
                    casilla = movimientoCliente(tablero5x5)
                    tablero5x5[casilla] = cliente
                    turno = "Servidor"
                    imprimirTablero5x5(tablero5x5)
                    if comprobarGanador5x5(tablero5x5, cliente):
                        print("¡Ganaste!")
                        ClientConn.sendall(bytes("ganaste", "utf-8"))
                        partida = False
                        TCPServerSocket.close()
                elif turno == "Servidor":
                    print("El servidor esta pensando...")
                    time.sleep(2)
                    casilla = movimientoServidor5x5(tablero5x5, servidor)
                    tablero5x5[casilla] = servidor
                    # Enviamos la posicion del servidor
                    movimiento_servidor = str(casilla + 1)
                    ClientConn.sendall(bytes(movimiento_servidor, "utf-8"))
                    turno = "Cliente"
                    imprimirTablero5x5(tablero5x5)
                    if comprobarGanador5x5(tablero5x5, servidor):
                        print("¡Gano el servidor!")
                        ClientConn.sendall(bytes("perdiste", "utf-8"))
                        partida = False
                        TCPServerSocket.close()
