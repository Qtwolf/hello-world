
elegir_operacion = input("Que operacion quieres hacer? ( Sumar / Restar / Multiplicar / Dividir :")

primer_numero = int(input("Dimer el primer numero para {}.".format(elegir_operacion)))
segundo_numero = int(input("Dime el segundo numero para {}.".format(elegir_operacion)))

if elegir_operacion == "Sumar":
    suma = primer_numero + segundo_numero
    print("El resultado es {}".format(suma))

elif elegir_operacion == "Restar":
    resta = primer_numero - segundo_numero
    print("El resultado es {}".format(resta))

elif elegir_operacion == "Multiplicar":
    multiplica = primer_numero * segundo_numero
    print("El resultado es {}".format(multiplica))

elif elegir_operacion == "Dividir":
    divide = primer_numero / segundo_numero
    print("El resultado es {}".format(divide))

