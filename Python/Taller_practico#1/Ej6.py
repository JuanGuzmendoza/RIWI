

print("SUMA DE NUMEROS ENTEROS HASTA EL NUMERO INDICADO")

final=int(input("Ingrese el numero final hasta que se contara: "))
suma=0
if final < 1:
    print("No se pueden numeros negativos")
else:
    for i in range(1,final+1):
        print(i)
        suma+=i

    print(f"La suma total es: {suma}")    

        