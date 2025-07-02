mes=int(input("Ingrese el mes de manera numerica 1-12: "))

if mes < 0:
    print("--NO SE ACEPTAN NUMEROS NEGATIVOS--")
elif mes >=1 and mes <=3:
    print("--INVIERNO--")
elif mes >=4 and mes <=6:
    print("--PRIMAVERA--")
elif mes >=7 and mes <=9:
    print("--VERANO--")
elif mes >=10 and mes <=12:
    print("--OTOÑO--")
else:
    print("El valor esta fuera del rango ")