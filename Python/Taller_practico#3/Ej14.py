

numero=int(input("Ingresa un numero: "))

d3=numero%3
d4=numero%4

if d3== 0 and d4==1:
    print("El numero es divisible por 3 pero no por 4")
elif d3==0 and d4==0:
    print("El numero es divisible por 3 y 4")
