
# Estructura de datos para almacenar productos y ventas
# Estructura de datos para almacenar productos y ventas
class Producto:
    def __init__(self, titulo, autor, categoria, precio, cantidad):
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

class Venta:
    def __init__(self, cliente, producto, cantidad, fecha, descuento):
        self.cliente = cliente
        self.producto = producto
        self.cantidad = cantidad
        self.fecha = fecha
        self.descuento = descuento

class Sistema:
    def __init__(self):
        self.productos = []
        self.ventas = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def registrar_venta(self, venta):
        if venta.producto.cantidad >= venta.cantidad:
            self.ventas.append(venta)
            venta.producto.cantidad -= venta.cantidad
        else:
            print("No hay suficiente stock.")

    def generar_reporte_top_3(self):
        top_3 = sorted(self.ventas, key=lambda x: x.cantidad, reverse=True)[:3]
        return top_3

    def generar_reporte_ventas_autor(self):
        ventas_autor = {}
        for venta in self.ventas:
            autor = venta.producto.autor
            if autor in ventas_autor:
                ventas_autor[autor] += venta.cantidad
            else:
                ventas_autor[autor] = venta.cantidad
        return ventas_autor

    def calcular_ingreso_neto(self):
        total = 0
        for venta in self.ventas:
            precio = venta.producto.precio
            cantidad = venta.cantidad
            descuento = venta.descuento
            if descuento:
                precio *= (1 - descuento / 100)
            total += precio * cantidad
        return total

# Inicializar sistema con 5 productos pre-cargados
sistema = Sistema()
sistema.agregar_producto(Producto("Libro 1", "Autor 1", "Categoría 1", 10, 10))
sistema.agregar_producto(Producto("Libro 2", "Autor 2", "Categoría 2", 20, 20))
sistema.agregar_producto(Producto("Libro 3", "Autor 3", "Categoría 3", 30, 30))
sistema.agregar_producto(Producto("Libro 4", "Autor 4", "Categoría 4", 40, 40))
sistema.agregar_producto(Producto("Libro 5", "Autor 5", "Categoría 5", 50, 50))

# Menú interactivo
while True:
    print("1. Agregar producto")
    print("2. Registrar venta")
    print("3. Generar reporte top 3")
    print("4. Generar reporte ventas autor")
    print("5. Calcular ingreso neto")
    print("6. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        titulo = input("Ingrese título del libro: ")
        autor = input("Ingrese autor del libro: ")
        categoria = input("Ingrese categoría del libro: ")
        precio = float(input("Ingrese precio del libro: "))
        cantidad = int(input("Ingrese cantidad del libro: "))
        producto = Producto(titulo, autor, categoria, precio, cantidad)
        sistema.agregar_producto(producto)
    elif opcion == "2":
        cliente = input("Ingrese nombre del cliente: ")
        producto = input("Ingrese título del libro: ")
        cantidad = int(input("Ingrese cantidad del libro: "))
        fecha = input("Ingrese fecha de la venta: ")
        descuento = float(input("Ingrese descuento (0-100): "))
        venta = Venta(cliente, producto, cantidad, fecha, descuento)
        sistema.registrar_venta(venta)
    elif opcion == "3":
        top_3 = sistema.generar_reporte_top_3()
        for venta in top_3:
            print(f"Cliente: {venta.cliente}, Libro: {venta.producto.titulo}, Cantidad: {venta.cantidad}")
    elif opcion == "4":
        ventas_autor = sistema.generar_reporte_ventas_autor()
        for autor, cantidad in ventas_autor.items():
            print(f"Autor: {autor}, Cantidad: {cantidad}")
    elif opcion == "5":
        ingreso_neto = sistema.calcular_ingreso_neto()
        print(f"Ingreso neto: {ingreso_neto}")
    elif opcion == "6":
        break
    else:
        print("Opción inválida.")
        # Necesito que no utilices el while true y tampoco el self