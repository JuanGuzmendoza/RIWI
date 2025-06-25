


estudiantes={}

def main_function():
    while True:
        print("--CRUD PARA AGREGAR NOMBRES Y EDADEs--")
        print("--1. Agregar estudiante con edad--")
        print("--2. Consultar la edad de un estudiante--")
        print("--3. Actualizar edad--")
        print("--4. Eliminar estudiante--")
        print("Ingrese la opcion que usara")
        opcion=input("-")
        match opcion:
            case"1":
                agregar_estudiante()
            case"2":
                consultar_edad()                
            case"3":
                actualizar_edad()
            case "4":
                eliminar_estudiante()
            case _:
                break

def agregar_estudiante():
    print("--AGREGAR ESTUDIANTES--")
    nombre_estudiante=input("Ingrese el nombre del estudiante: ")
    edad_estudiante=int(input("Ingrese la edad del estudiante: "))
    estudiantes[nombre_estudiante]=edad_estudiante
    print(estudiantes)
    print("\n")

def consultar_edad():
    print("--CONSULTAR EDAD--")
    print(f"Total estudiantes: {len(estudiantes)}")
    for i in estudiantes:
        print(f"Estudiante: {i}")
    print("Nombre del estudiante para saber la edad")
    nombre_buscar=input("-").lower().replace(" ","")
    for i in estudiantes:
        if nombre_buscar==i.lower().replace(" ",""):
            print(f"La edad del estudiante {i} es: {estudiantes.get(i)}")
            break

def actualizar_edad():
    print("--ACTUALIZAR EDAD--")
    print(f"Total estudiantes: {len(estudiantes)}")
    for i in estudiantes:
        print(f"Estudiante: {i}")
    print("Nombre del estudiante para actualizar la edad")
    nombre_buscar=input("-").lower().replace(" ","")
    for i in estudiantes:
        if nombre_buscar==i.lower().replace(" ",""):
            edad_nueva=int(input(f"Ingrese la nueva edad de {i}: "))
            estudiantes[i]=edad_nueva
            break
    print("--NUEVA LISTA--")
    for i in estudiantes:
        print(f"N: {i} - Edad: {estudiantes.get(i)}")
    print("Actualizar edad")

def eliminar_estudiante():
    print("--ELIMINAR ESTUDIANTE--")
    print(f"Total estudiantes: {len(estudiantes)}")
    for i in estudiantes:
        print(f"Estudiante: {i}")
    print("Nombre del estudiante que desea eliminar")
    nombre_buscar=input("-").lower().replace(" ","")
    for i in estudiantes:
        if nombre_buscar==i.lower().replace(" ",""):
            del estudiantes[i]
            break
    print("--NUEVA LISTA--")
    for i in estudiantes:
        print(f"N: {i} - Edad: {estudiantes.get(i)}")

main_function()
