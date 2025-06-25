#Solicitud de nombre
nombre_comprador=input("Ingrese el nombre del comprador: ")
#Definicion de variables
respuesta=0
total_pagar=0
descuento_pagar=0
cant_productos=0
validacion=0
noms_productos=[]
cantides_productos=[]
precios_productos=[]
#Inputs(Recoleccion de productos)
while respuesta!=2:
    cant_productos+=1#Variable que lleva la cantidad de productos(Solo productos diferentes no cantidades de todos los productos juntos)
    
    nombre_producto=input(f"Ingrese el nombre del producto {cant_productos}: ")
    noms_productos.append(nombre_producto)

    #While el cual terminara hasta que las validaciones entren y cambien el valor de la variable -Validacion a 1 
    while validacion==0:
        cantidad_unitaria=input(f"Ingrese la cantidad que comprara de {nombre_producto}: ")
        if cantidad_unitaria.isdigit():
            cantides_productos.append(int(cantidad_unitaria))
            validacion=1
        else:
            print("--INGRESE SOLAMENTE NUMEROS--")
    #Se reinicia el valor de la variable de validacion por 0 para el siguiente bucle
    validacion=0
    
    while validacion==0:
        precio_unitario=input(f"Precio unitario para el producto {nombre_producto} (sin comas): ")
        if precio_unitario.isdecimal():
            precios_productos.append(float(precio_unitario))
            validacion=1
        else:
            print("--INGRESE SOLAMENTE NUMEROS--")
    validacion=0
    
    #Se concatena toda la suma de los demas productos pasados mas los recien colocados
    total_pagar+=(float(precio_unitario)*int(cantidad_unitaria))

    while validacion==0:
        #Se pregunta si quiere hacer la compra de otro producto
        respuesta=int(input("""................
        Desea hacer otra compra?
        1.Si - 2.No
        -"""))
        if respuesta==1 or respuesta ==2:
            validacion=1
        else:
            print("Porfavor seleccione alguna de las 2 opciones: 1.Si - 2.No (Solamente el numero 1 o 2)")
    validacion=0
    

#Parte final (IMPRIMIR FACTURA)
print(f'\033[92m'+"""
      
    --FACTURA FINAL--"""+'\033[0m')
#Parte de la informacion general que nunca necesita un cambio al momento de mostrarse finalmente
print(f"""Cliente: {nombre_comprador}
Cantidad de productos comprados: {cant_productos}
Total a pagar sin descuento: {total_pagar}
""")
    
#Parte donde se imprimen los productos de manera unitaria    
print(f'\033[92m'+"""    --PRODUCTOS COMPRADOS--"""+'\033[0m')
for i in range(len(noms_productos)):#Se sacara la longitud del primer array rellenado al momento de entrar al while
        print(f"""--Producto #{i+1}
nombre: {noms_productos[i]}
cantidad: {cantides_productos[i]}
precio_unitario: {precios_productos[i]}
**Precio total por producto**
{cantides_productos[i]*precios_productos[i]}
""")

#Parte final de la factura
print(f'\033[92m'+"""
    --TOTAL A PAGAR--"""+'\033[0m')
if total_pagar >= 2000:#Descuando del 20% cuando sea msa de 2k la compra final
    print(f"""Valor del descuento del 20%: {total_pagar*0.20}
Total a pagar con el descuento: {total_pagar-(total_pagar*0.20)}""")
else:
    print(f"""Valor del descuento: *NO APLICA*
Total a pagar: {total_pagar}""")
