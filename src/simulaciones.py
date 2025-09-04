import os

detenerse = False
while detenerse == False:
    os.system("cls")
    print("--- SISTEMA DE ROUTER ABC ---")
    print("Ingrese la opción que desee ejecutar.")
    print("1. Inicializar enrutamiento de IP's.")
    print("2. Mostrar direcciones IP ingresadas.")
    print("3. Salir.")
    opcion = int(input("Opción: "))
    
    if opcion == 1:
        os.system("cls")
        print("--- INICIALIZAR ENRUTAMIENTO DE IP'S ---")
        print("Se iniciará el enrutamiento de IPs.")
        # Por implementar.
        input("Presione cualquier tecla para continuar.")

    elif opcion == 2:
        os.system("cls")
        print("--- MOSTRAR DIRECCIONES IP INGRESADAS ---")
        print("A continuación se mostrarán las direcciones IP ingresadas.")
        # Por implementar.
        input("Presione cualquier tecla para continuar.")

    elif opcion == 3:
        print("--- CERRANDO PROGRAMA ---")
        detenerse = True

    else:
        input("Ingrese una opción válida.")