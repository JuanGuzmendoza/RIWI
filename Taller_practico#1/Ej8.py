print("--DIAS A SEGUNDOS--")

dias=int(input("Ingrese el numero de dias: "))
if dias < 1 :
    print("No se permiten numeros negativos ")
else:
    print(f"El numero de segundos en esos dias es: {dias*86400}")