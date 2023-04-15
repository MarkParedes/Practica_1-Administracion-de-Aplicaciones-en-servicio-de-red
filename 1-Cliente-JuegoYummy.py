#!/usr/bin python3
import socket

# El cliente creara una copia del tablero ya sea de 3x3 o de 5x5
def imprimirTablero3x3(tablero3x3):
    print("\n")
    print("1", " | ", "2", " | ", "3")
    print("-------------")
    print("4", " | ", "5", " | ", "6")
    print("-------------")
    print("7", " | ", "8", " | ", "9")
    print("\n")

# Imprime el tablero de 5x5 en modo avanzado
def imprimirTablero5x5(tablero5x5):
    print("\n")
    print(" 1", " | ", " 2", " | ", " 3", " | ", " 4", " | ", "5")
    print("--------------------------------")
    print(" 6", " | ", " 7", " | ", " 8", " | ", " 9", " | ", "10")
    print("--------------------------------")
    print("11", " | ", "12", " | ", "13", " | ", "14", " | ", "15")
    print("--------------------------------")
    print("16", " | ", "17", " | ", "18", " | ", "19", " | ", "20")
    print("--------------------------------")
    print("21", " | ", "22", " | ", "23", " | ", "24", " | ", "25")
    print("\n")

def casillaLibre(tablero3x3, casilla):
    return tablero3x3[casilla] == " "

#Se verifican los movimientos del cliente 3x3
def movimientoCliente(tablero3x3):
    posiciones=["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    posicion=None
    while True:
        if posicion not in posiciones:
            posicion=input("Elige una posicion del 1 al 9:\n")
        else:
            posicion=int(posicion)
            if not casillaLibre(tablero3x3, posicion-1):
                print("Posicion ocupada.")
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


# Variables para el cliente
HOST = "127.0.0.1"
PORT = 65432
buffer_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as TCPClientSocket:
    TCPClientSocket.connect((HOST, PORT))

    print("Bienvenido, estas conectado a servidor.")
    # El usuario manda la dificultad del juego
    print("Juego Gato Yummy")
    print("1. Principiante")
    print("2. Avanzado")

    # Enviamos la dificultad
    data = input("-> ")
    TCPClientSocket.sendall(bytes(data, "utf-8"))

    # Recibimos un mensaje de confirmación del servidor
    mensaje = TCPClientSocket.recv(1024)
    print(mensaje.decode())

    # inicializamos el tablero
    tablero3x3 = [" "] * 9
    tablero5x5 = [" "] * 25

    if data == "1":
        imprimirTablero3x3(tablero3x3)
    if data == "2":
        imprimirTablero5x5(tablero5x5)

    jugando = True
    while jugando:
        if data == "1":
            posicion_cliente = input("Elige una posicion del 1 al 9: ")
            # Enviamos la posicion
            TCPClientSocket.sendall(bytes(posicion_cliente, "utf-8"))
            # Recibimos la posicion del servidor
            posicion_servidor = str(TCPClientSocket.recv(buffer_size), "utf-8")
            print(f"Servidor: {posicion_servidor}")
            if posicion_servidor == "empate":
                print("!Empate!")
                jugando = False
                TCPClientSocket.close()
            elif posicion_servidor == "ganaste":
                print("¡Ganaste!")
                jugando = False
                TCPClientSocket.close()
            elif posicion_servidor == "perdiste":
                print("¡Perdiste!")
                jugando = False
                TCPClientSocket.close()
        elif data == "2":
            posicion_cliente = input("Elige una posicion del 1 al 25: ")
            # Enviamos la posicion
            TCPClientSocket.sendall(bytes(posicion_cliente, "utf-8"))
            # Recibimos la posicion del servidor
            posicion_servidor = str(TCPClientSocket.recv(buffer_size), "utf-8")
            print(f"El servidor eligio la posicion {posicion_servidor}")
            if posicion_servidor == "empate":
                print("!Empate!")
                jugando = False
                TCPClientSocket.close()
            elif posicion_servidor == "ganaste":
                print("¡Ganaste!")
                jugando = False
                TCPClientSocket.close()
            elif posicion_servidor == "perdiste":
                print("¡Gano el servidor! ")
                jugando = False
                TCPClientSocket.close()



