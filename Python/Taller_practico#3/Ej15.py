

sexo=int(input("Seleccione su sexo- 1.HOMBRE - 2.MUJER "))
edad=int(input("Ingrese la edad de la persona: "))


if edad >= 18:
    if sexo==1:
        print(" Es un hombre adulto")
    elif sexo==2:
        print(" Es una mujer adulta ")
    else:
        print("No selecciono ninguna de la 2 opciones solicitadas")
else:
    print("La persona es menor de edad")
