#SE ACTUALIZA A ARCHIVOS DE FUNCIONES

import numpy as np
import os
import msvcrt
import colorama as c

edificio=np.empty((10,4),object)
dueños={} #para almacenar información sobre los dueños de los departamentos.
ganancia=0
def limpiarpantalla():
    print("<<Presione una tecla para continuar>>")
    msvcrt.getch()  # Añade los paréntesis para invocar la función
    os.system("cls")  # Reemplaza "clear" con el comando apropiado para limpiar la pantalla según tu sistema operativo

def menu():
    print("""
    1) Ver edificio
    2) Comprar departamento
    3) Buscar Dueño
    4) Total ganancias
    5) Salir
    """)
def veredificio():
    print("Ver edificio")
    nro_piso=11 #Esta variable se utilizará para mostrar el número de piso mientras se itera sobre ellos.
    print("\t    A   B   C   D")
    for piso in range(10,0,-1): # itera desde 10 hasta 1 en orden descendente, iterando sobre cada piso del edificio.
        nro_piso-=1 #Resta 1 a nro_piso en cada iteración para actualizar el número de piso que se muestra.
        print(f"Nro Piso:{nro_piso}",end=" ") #Imprime piso actual / End añade espacio despues del cuadrado
        for letra in range (4):#: itera desde 0 hasta 3, representa A, B, C y D
            if edificio[piso-1,letra]==None: #En edificio [Piso-1 (porque parte del )]
                print("🟩",end=" ")
            else:
                print("🟥",end=" ")
        print(" ") # Imprime un espacio en blanco al final de cada línea para separar los pisos.
    print("Los departamentos de los pisos del 10 al 8 tienen un valor de 200 millones.")
    print("Los departamentos de los pisos del 1 al 7 tienen un valor de 150 millones.")

    print("Disponible=🟩")
    print("Vendido=🟥")

def comprardepartamento():
    global ganancia #IMPORTANTE PARA PODER ACTUALIZAR LAS GANANCIAS FUERA DE LA FUNCION
    print("Comprar departamento")
    piso=int(input("Ingrese el numero de piso:")) #Guardo piso (1-10)
    if piso>=1 and piso<=10: 
        letra=str(input("Ingrese el letra de depto A-B-C-D:")).upper()
        if len(letra)==1:
            if letra in["A","B","C","D"]:
                if edificio[piso-1,ord(letra)-65] is None: #Si es None
                    if piso>=1 and piso<=7:                 #PISO UNO AL 7
                        print("El valor del departamento tiene un valor de $150.000.000")
                        precio=150000000          
                    elif piso>=8 and piso<=10:              #PISO AL 8-10
                        print("El valor del departamento tiene un valor de $200.000.000")
                        precio=200000000
                    pago=int(input("Por favor ingrese monto de pago:$"))
                    if pago>=precio:
                        vuelto=pago-precio
                        print("Pago efectuado con exito")
                        if vuelto>0:
                            print(f"Su vuelto es:${vuelto}")
                    else:
                        print("Pago insuficiente")
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
                            print("Muchas gracias por su compra!!")
                            dueños[rut] = {     #Guardamos en diccionario dueños la ID de rut (y sus datos)
                                "nombre": nombre,
                                "piso": piso,
                                "letra": letra}
                        else:
                            print("Ingrese un nombre valido")
                    else:
                        print("Ingrese un rut valido") 
                else:
                    print("El departamento ya fue vendido")
            else:
                print("Por favor ingrese una letra valido")
        else:
            print("Depto solo puede tener una letra")
    else:
        print("Piso invalido")


def buscardueño():
    print("Buscar dueño")
    rut=int(input("Ingrese rut (sin puntos, ni digito verificador):"))
    if rut>11111111 and rut<99999999: #VALIDAMOS QUE TENGA 8 DIGITOS EJ: 12.345.678 or Len=8
        if rut in dueños: # si el rut esta en dueño
            dueño=dueños[rut] #sacamos quien es
            nombre=dueño["nombre"] #obtenemos el nombre
            print(f"El nombre del dueño es:{nombre}") # se muestra
            print("Departamentos asociados al rut:") # los departamentos asociados
            for piso in range(10,0,-1): #Recorremos el edificio por piso
                for depto in range(4):# y depto
                    if edificio[piso - 1, depto] is not None and edificio[piso - 1, depto]["rut"] == rut:
                        print(f"Piso: {piso} Letra: {chr(depto + 65)}")
        else:
            print("No se encontró ningún dueño con ese rut")
    else:
            print("Ingrese un rut valido") 
def ganancias():
    print("TOTAL GANANCIAS:")
    print(f"${ganancia}")
