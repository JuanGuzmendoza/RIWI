

numero=int(input("Ingrese un numero: "))

residuo=numero%2

if residuo == 0 and numero > 10:
    print("El numero es par y es mayor que 10")
elif residuo == 0:
    print("El numero NO es mayor que 10 y es par")
elif numero >10:
    print("El numero solamente es mayor que 10 y NO es par")
else:
    print("El numero NO es mayor que 10 y tampoco es par")

