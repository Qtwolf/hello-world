
quieres_helado_input = input("¿Quieres un helado? (Si / No): ").upper()

if quieres_helado_input == "SI":
    quieres_helado = True
elif quieres_helado_input == "NO":
    quieres_helado = False
else:
    print("Te he dicho que me digas si o no, no se que has dicho pero cuento como que no")
    quieres_helado = False

tiene_dinero_input = input("¿Tienes dinero para un helado? (Si / No): ").upper()

if tiene_dinero_input == "SI":
    tiene_dinero = True
elif tiene_dinero_input == "NO":
    tiene_dinero = False
else:
    print("Te he dicho que me digas si o no, no se que has dicho pero cuento como que no")
    tiene_dinero = False

esta_el_senor_helados_input = input("¿Esta el señor de los helados? (Si / No): ").upper()
esta_tu_tia_input = input("¿Estas con tu tia?  (Si / No): ").upper()

esta_tu_tia = esta_tu_tia_input == "SI"
puede_permitirselo = tiene_dinero or esta_tu_tia
esta_el_senor_helados = esta_el_senor_helados_input == "SI"

if quieres_helado  and puede_permitirselo and esta_el_senor_helados:
    print("Entonces comete un helado")
else:
    print("Lo siento no puedo venderte un helado")