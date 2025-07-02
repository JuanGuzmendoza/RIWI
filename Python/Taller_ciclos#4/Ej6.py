

inicio=int(input("Ingrese el numero con el cual iniciara: "))
fin=int(input("Ingrese el numero final: "))
residuo=0
pares=0
for i in range(inicio,fin+1):
    residuo= i % 2
    if residuo == 0:
        pares+=1
print(f"Numeros pares: {pares}")
