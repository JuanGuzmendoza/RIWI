
print("CONTANDO HASTA EL NUMERO SELECCIONADO")
final=int(input("Numero hasta el cual se contara: "))
if final < 1:
    print("No se puede numeros negativos")
else:
    for i in range(1,final+1):
        print(i)
    