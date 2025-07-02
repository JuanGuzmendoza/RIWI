


acumulacion=0
pregunta=""
while True:

    numero=float(input("ingrese el numero: "))
    acumulacion+=numero
    pregunta=input("Desea salir?: ")
    if pregunta=="salir":
        break
print(f"AcumulacioN: {acumulacion}")
