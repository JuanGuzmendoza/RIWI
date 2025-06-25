

i=1
while i<=5:
    print(f"Intentos faltantes: {5-i}")
    numero=int(input("Ingrese el numero para adivinar: "))
    if numero ==5:
        print("ADIVINO EL NUMERO SECRETO EL CUAL ES 5")
        break
    i+=1
else:
    print("No adivno")
    
    