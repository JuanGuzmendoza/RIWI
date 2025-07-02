print("--SUMA DE TODOS LOS DIGITOS DE UN NUMERO--")

numero=input("Ingrese el numero: ")
suma=0
if numero.isdigit():
    print("Es un numero")
    for i in range(len(numero)):
      suma+=int(numero[i])
      print(numero[i])
    print(f"Suma total de los digitos es: {suma}")
else:
    print("Porfavor ingrese bien el numero")

