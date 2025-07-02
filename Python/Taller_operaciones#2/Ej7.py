n1=int(input("Ingrese el primero numero: "))
n2=int(input("Ingrese el segundo numero: "))

if n1 >10 and n2 >10:
    print("Los 2 numeros son mayores que 10")
elif n1 > 10 or n2 > 10:
    if n1 > 10:
        print(f"Solamente el {n1} es mayor que 10 ")
    else:
        print(f"Solamente el {n2} es maayor que 10")
else:
    print("Ninguno de los 2 numeros es mayor que 10")