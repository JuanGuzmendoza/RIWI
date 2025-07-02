numero1=int(input("Ingrese el numero 1: "))
numero2=int(input("Ingrese el numero 2: "))
numero3=int(input("Ingrese el numero 3: "))

if numero1  > numero2 and numero1  > numero3:
    print(f"El numero {numero1} es el mayor")
elif numero2  > numero1 and numero2  > numero3:
    print(f"El numero {numero2} es el mayor")
else:
    print(f"El numero {numero3} es el mayor")
