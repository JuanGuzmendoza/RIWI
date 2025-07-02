

sueldo=float(input("Ingrese el sueldo: "))

if sueldo > 3000 and sueldo <5000:
    print("!EL SUELDO SE GANO UNA BONIFICACION DEl 10 PORCIENTO!")
    print(f"Sueldo total: {sueldo+(sueldo*0.10)}")
elif sueldo > 5000:
    print("!EL SUELDO SE GANO UNA BONIFICACION DEl 15 PORCIENTO!")
    print(f"Sueldo total: {sueldo+(sueldo*0.15)}")