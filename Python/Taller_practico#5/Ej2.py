
nombre_estudiante=[]

def main_function():
    while True:
        print("CRUD-NOMBRES-ESTUDIANTES")
        print("1.Agregar nombre")
        print("2.Ver nombres")
        print("3.Actualizar nombre")
        print("4.Eliminar nombre")
        opcion=input("-")

        match opcion:
            case "1":
                agregar_nombres()
            case "2":
                ver_nombres()
            case "3":
                actualizar_nombre()
            case "4":
                eliminar_nombre()
            case _:
                break

def agregar_nombres():  
    print("\033[92m--OPCION PARA AGREGAR UN NOMBRE--\033[0m")
    nombre=input("Ingrese el nombre que quiere agregar: ")
    nombre_estudiante.append(nombre)
    print("\n")

def ver_nombres():
    print("--OPCION PARA VER TODOS LOS NOMBRES--")
    
    print(f"Nombre totales: {len(nombre_estudiante)}")
    for i in nombre_estudiante:
        print(f"Estudiante: {i}")

def actualizar_nombre():
    print("--OPCION PARA ACTUALIZAR UN NOMBRE--")
    
    print(f"Nombre totales: {len(nombre_estudiante)}")
    for i in range(len(nombre_estudiante)):
        print(f"Indice {i} - Estudiante: {nombre_estudiante[i]}")
    
    print("Ingrese el indice del nombre que quiere cambiar")
    indice=int(input("- "))

    if nombre_estudiante[indice]:
        nombre=input("Ingrese el nuevo nombre")
        nombre_estudiante.pop(indice)
        nombre_estudiante.insert(indice,nombre)
        print("-LISTA DE NOMBRES ACTUALIZADA-")
        for i in nombre_estudiante:
            print(f"Indice {i} - Estudiante: {i}")
    else:
        print("Indice no seleccionado")

def eliminar_nombre():
    print("--OPCION PARA BORRAR UN NOMBRE--")
    
    print(f"Nombre totales: {len(nombre_estudiante)}")
    for i in range(len(nombre_estudiante)):
        print(f"Indice {i} - Estudiante: {nombre_estudiante[i]}")
    
    print("Ingrese el indice del nombre que quiere borrar")
    indice=int(input("- "))
    if nombre_estudiante[indice]:
        nombre_estudiante.pop(indice)
        print("-LISTA DE NOMBRES ACTUALIZADA-")
        for i in nombre_estudiante:
            print(f"Indice {i} - Estudiante: {i}")
    else:
        print("Indice no seleccionado")

main_function()