

sueldo=float(input("Ingrese el sueldo actual: "))
porcentaje=float(input("Ingrese porcentaje de aumento: "))
print(f"""Nueva cantidad de aumento: {((sueldo*porcentaje)/100)}
Sueldo mas el aumento: {sueldo+((sueldo*porcentaje)/100)}""")