import os
from hash_tabla import HashTable
tablaRouter = HashTable()

detenerse = False
while detenerse == False:
    os.system("cls")
    print("--- SISTEMA DE ROUTER ABC ---")
    print("Ingrese la opción que desee ejecutar.")
    print("1. Inicializar enrutamiento de IP's.")
    print("2. Buscar direcciones IP ingresadas.")
    print("3. Salir.")
    opcion = int(input("Opción: "))
    
    if opcion == 1:
        os.system("cls")
        print("--- INICIALIZAR ENRUTAMIENTO DE IP'S ---")
        print("Se iniciará el enrutamiento de IPs.")
        ipNueva = input("IP nueva (Por ejemplo: 192.168.0.0): ")
        puertoNuevo = input("Indique el nuevo puerto (Por ejemplo: eth0): ")
        tablaRouter.add_route(ipNueva, puertoNuevo)
        print("IP agregada al sistema.")
        input("Presione cualquier tecla para continuar.")

    elif opcion == 2:
        os.system("cls")
        print("--- BUSCAR DIRECCIONES IP INGRESADAS ---")
        print("A continuación se mostrarán las direcciones IP ingresadas.")
        ipBuscador = input("IP a buscar: ")
        tablaRouter.find_router(ipBuscador)
        input("Presione cualquier tecla para continuar.")

    elif opcion == 3:
        print("--- CERRANDO PROGRAMA ---")
        detenerse = True

    else:
        input("Ingrese una opción válida.")
