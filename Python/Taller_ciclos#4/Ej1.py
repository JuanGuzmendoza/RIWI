

cont=0
for i in range(0,10):
    numero=float(input(f"Ingrese el numero {i+1}: "))
    if numero > 0:
        cont+=1
print(f"Los numeros mayores a 0 son: {cont}")