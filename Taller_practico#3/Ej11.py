


numero=int(input("Ingrese un numero: "))

m3=numero%3
m5=numero%5

if m3==0 and m5==0:
    print("El numero es multiplo de 5 y 3")
elif m3==0:
    print("El numero es multiplo de 3")
elif m5==0:
    print("El numero es multiplo de 5")