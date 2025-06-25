

precio_producto=int(input("Ingrese el precio del producto: "))

if precio_producto > 100:
    print(f"Precio menos un 20 porciento de descuento: {precio_producto+(precio_producto*0.20)}")
else:
    print(f"El precio del producto se mantiene en: {precio_producto}")