
numero=int(input("Ingrese un numero: "))
d2=numero%2
d3=numero%3
d5=numero%5
if d2 == 0 and d3 ==0 and d5 ==0:
    print("El numero es divisible por 2,3,5")
else:
    print("El numero no es divisible por los 3 numeros")
