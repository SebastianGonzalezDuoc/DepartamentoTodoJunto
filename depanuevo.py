#SE ACTUALIZA A ARCHIVOS DE FUNCIONES

import numpy as np
import os
import msvcrt
import colorama as c

edificio=np.empty((10,4),object)
dueños={} #para almacenar información sobre los dueños de los departamentos.
ganancia=0

def printr(texto):
    print(f"{c.Fore.RED}{texto}{c.Fore.RESET}")
def printam(texto):
    print(f"{c.Fore.YELLOW}{texto}{c.Fore.RESET}")
def printv(texto):
    print(f"{c.Fore.GREEN}{texto}{c.Fore.RESET}")
def printcyan(texto):
    print(f"{c.Fore.CYAN}{texto}{c.Fore.RESET}")
def printtitulo(texto):
    print(f"{c.Fore.YELLOW}----------------------------------------------{c.Fore.RESET}")
    print(f"                {c.Fore.BLUE}{texto}{c.Fore.RESET}")
    print(f"{c.Fore.YELLOW}----------------------------------------------{c.Fore.RESET}")

def limpiarpantalla():
    printam("<<Presione una tecla para continuar>>")
    msvcrt.getch()  # Añade los paréntesis para invocar la función
    os.system("cls")  # Reemplaza "clear" con el comando apropiado para limpiar la pantalla según tu sistema operativo

def menu():
    printtitulo("MENU")
    printcyan("""
    1) Ver edificio
    2) Comprar departamento
    3) Buscar Dueño
    4) Total ganancias
    5) Salir
    """)
def veredificio():
    printtitulo("Ver edificio")
    nro_piso=11 #Esta variable se utilizará para mostrar el número de piso mientras se itera sobre ellos.
    printam("\t    A   B   C   D")
    for piso in range(10,0,-1): # itera desde 10 hasta 1 en orden descendente, iterando sobre cada piso del edificio.
        nro_piso-=1 #Resta 1 a nro_piso en cada iteración para actualizar el número de piso que se muestra.
        if piso == 10:
            print(f"Nro Piso:{nro_piso} ", end="")
        else:
            print(f"Nro Piso :{nro_piso}", end=" ")
        for letra in range (4):#: itera desde 0 hasta 3, representa A, B, C y D
            if edificio[piso-1,letra]==None: #En edificio [Piso-1 (porque parte del )]
                print("🟩",end=" ")
            else:
                print("🟥",end=" ")
        print(" ") # Imprime un espacio en blanco al final de cada línea para separar los pisos.
    printcyan("Los departamentos de los pisos del 10 al 8 tienen un valor de 200 millones.")
    printcyan("Los departamentos de los pisos del 1 al 7 tienen un valor de 150 millones.")

    printv("Disponible=🟩")
    printr("Vendido=🟥")

def comprardepartamento():
    global ganancia #IMPORTANTE PARA PODER ACTUALIZAR LAS GANANCIAS FUERA DE LA FUNCION
    printtitulo("Comprar departamento")
    piso=int(input("Ingrese el numero de piso:")) #Guardo piso (1-10)
    if piso>=1 and piso<=10: 
        letra=str(input("Ingrese el letra de depto A-B-C-D:")).upper()
        if len(letra)==1:
            if letra in["A","B","C","D"]:
                if edificio[piso-1,ord(letra)-65] is None: #Si es None
                    if piso>=1 and piso<=7:                 #PISO UNO AL 7
                        printam("El valor del departamento tiene un valor de $150.000.000")
                        precio=150000000          
                    elif piso>=8 and piso<=10:              #PISO AL 8-10
                        printam("El valor del departamento tiene un valor de $200.000.000")
                        precio=200000000
                    pago=int(input("Por favor ingrese monto de pago:$"))
                    if pago>=precio:
                        vuelto=pago-precio
                        printv("Pago efectuado con exito")
                        if vuelto>0:
                            printam(f"Su vuelto es:${vuelto}")
                    else:
                        printr("Pago insuficiente")
                    ganancia+=precio #Actualizamos las ganancias
                    

                    rut=int(input("Ingrese rut (sin puntos, ni digito verificador):"))
                    if rut>11111111 and rut<99999999: #VALIDAMOS QUE TENGA 8 DIGITOS EJ: 12.345.678 or Len=8
                        nombre=str(input("Ingrese nombre del comprador:"))
                        if len(nombre)>=3:
                            edificio[piso-1,ord(letra)-65] = { #Guardamos datos: Nombre ,rut , precio , pago
                            "nombre": nombre,
                            "rut": rut,
                            "precio": precio,
                            "pago": pago}
                            printam("Muchas gracias por su compra!!")
                            dueños[rut] = {     #Guardamos en diccionario dueños la ID de rut (y sus datos)
                                "nombre": nombre,
                                "piso": piso,
                                "letra": letra}
                        else:
                            printr("Ingrese un nombre valido")
                    else:
                        printr("Ingrese un rut valido") 
                else:
                    printr("El departamento ya fue vendido")
            else:
                printr("Por favor ingrese una letra valido")
        else:
            printr("Depto solo puede tener una letra")
    else:
        printr("Piso invalido")


def buscardueño():
    printtitulo("Buscar dueño")
    rut=int(input("Ingrese rut (sin puntos, ni digito verificador):"))
    if rut>11111111 and rut<99999999: #VALIDAMOS QUE TENGA 8 DIGITOS EJ: 12.345.678 or Len=8
        if rut in dueños: # si el rut esta en dueño
            dueño=dueños[rut] #sacamos quien es
            nombre=dueño["nombre"] #obtenemos el nombre
            printam(f"El nombre del dueño es:") 
            print(f"{nombre}") # se muestra
            printam("Departamentos asociados al rut:") # los departamentos asociados
            for piso in range(10,0,-1): #Recorremos el edificio por piso
                for depto in range(4):# y depto
                    if edificio[piso - 1, depto] is not None and edificio[piso - 1, depto]["rut"] == rut:
                          print(f"Piso: {piso} Letra: {chr(depto + 65)}")
        else:
            printr("No se encontró ningún dueño con ese rut")
    else:
            printr("Ingrese un rut valido") 
def ganancias():
    printtitulo("TOTAL GANANCIAS:")
    printv(f"${ganancia}")
