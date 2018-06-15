

elegir_numero= int(input("¿Cual es el numero que quieres que adivine tu compañero? "))

numero_adivinar = int(input("Adivina el numero: "))

numero_error = elegir_numero

while elegir_numero != numero_adivinar:

    int(input("Elige otro numero:" ))

    if numero_error == elegir_numero:
        print("Has ganado")




