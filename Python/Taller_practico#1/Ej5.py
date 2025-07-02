print("EDAD EN MESES")

edad=int(input("Ingrese su edad en años: "))
if edad < 1:
    print("No se pueden numeros negativos ")
else:
    print(f"La edad en meses: {edad*12}")