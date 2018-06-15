

salida = False

agenda = dict()


while not salida:

    accion = input("¿Qué quieres hacer? [Añadir múmero [A] / Consultar número [C] / Salir[S] ]: ")


    if accion == "A":
        print("Vamos a añadir un número de telefono")
        nombre = input("Nombre: ")
        numero = input("Número: ")
        agenda[nombre] =  numero

    elif accion == "C":
        print("Consultar número")
        nombre = input("De quien quieres saber el numero: ")
        print(agenda[nombre])

    elif accion == "S":
        salida = True
