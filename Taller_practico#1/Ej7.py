print("CALCULAR INDICE DE MASA CORPORAL (IMC)")

peso =float(input("Ingrese su peso en kg: "))
altura=float(input("Ingrese su altura en metros: "))
imc=(peso//altura**2)
print(f"El IMC calculado es: {imc}")