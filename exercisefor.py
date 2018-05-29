
frase_del_usurio = input("Introduce una frase:")

for letras in frase_del_usurio:
    if letras in "aeiou":
        print("vocales {}".format(letras))

