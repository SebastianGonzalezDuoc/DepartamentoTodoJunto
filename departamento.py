import depanuevo as f

while True:
    f.limpiarpantalla()
    f.menu()
    try:
        opcion = int(input("Ingrese una opcion:"))
        if opcion == 1:
            f.veredificio()
        elif opcion == 2:
            f.comprardepartamento()
        elif opcion == 3:
            f.buscardueño()
        elif opcion == 4:
            f.ganancias()
        elif opcion == 5:
            print("Saliendo del sistema")
            break
        else:
            raise ValueError
    except ValueError:
        f.printr("Has ingresado una opcion no valida")