

numero=int(input("Ingrese el numero: "))

factorial=1

for i in range(numero):
    factorial += (i)*factorial
    print(f"{factorial} X {i+2}")


print(f"Factorial: {factorial}")