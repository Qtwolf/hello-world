

valores_sustituir = [1, 2, "hola", "adios"]
string_cambiar = "Hola, numero {}, numero {}, {} y {}"

for valor in valores_sustituir:
    string_cambiar = string_cambiar.replace("{}", str(valor), 1)

print(string_cambiar)
