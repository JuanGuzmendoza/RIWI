
#----------
#Funciones para Logica de negocio
#----------
def modificar_curso_edad(lista,nombre_estudiante,valor,tipo):
    """
    Funcion la cual permite modificar los cursos y edad gracias a la variable tipo
    - si tipo == 2 : se modifica el curso - sino :se modifica edad
    """
    for i in lista:
        if i[0]==nombre_estudiante:
            i[tipo]=valor
    return True

def eliminar_registro(lista,nombre_estudiante):
    for i in range(len(lista)):
        if lista[i][0]==nombre_estudiante:
            lista.pop(i)
    return True


#----------
#Funciones de validacion
#----------

def validar_solo_numeros(valor):
    try:
        if int(valor) >0:
            return True
        else:
            print("Solamente valores positivos")
    except:
        print("Solamente ingrese numeros enteros positivos")
        return False

#----------
#Funciones de vistas
#----------
def menu():
    print("--Menu de opciones--")
    print("1.Agregar nuevo registro")
    print("2.Listar registros")
    print("3.Modificar curso de estudiante")
    print("4.Modificar edad de estudiante")
    print("5.Eliminar estudiante")
    print("6.Salir")
    opcion=input("Opcion a usar: ")
    return opcion

def litar_registros(lista):
    print("--LISTA ESTUDIANTES--")
    if lista:
        for i in lista:
            print(f"N: {i[0]}- E: {i[1]} - C: {i[2]}")
        return True
    else:
        print("No tiene estudiantes")
#----------
#Funcion principal
#----------
def main_function():
    estudiantes=[]
    
    while True: 
        match menu():
            case "1":
                nombre_estudiante=input("Ingrese el nombre de nuevo estudiante: ")
                while True:
                    edad=input("Ingrese la edad: ")
                    if validar_solo_numeros(edad):
                        break
                nombre_curso=input("Nombre del curso: ")
                estudiantes.append([nombre_estudiante,edad,nombre_curso])
                print("Estudiante agregado")
            case "2":
                litar_registros(estudiantes)
            case "3":
                print("-MODIFICAR EDAD DE ESTUDIANTE-")
                litar_registros(estudiantes)
                nombre_estudiante=input("Nombre del estudiante seleccionado: ")
                nombre_curso=input("Nombre del nuevo curso: ")
                modificar_curso_edad(estudiantes,nombre_estudiante,nombre_curso,2)
            case "4":
                print("-MODIFICAR CURSO DE ESTUDIANTE-")
                litar_registros(estudiantes)
                nombre_estudiante=input("Nombre del estudiante seleccionado: ")
                while True:
                    edad=input("Ingrese la edad: ")
                    if validar_solo_numeros(edad):
                        break
                modificar_curso_edad(estudiantes,nombre_estudiante,edad,1)
            case "5":
                print("-ELIMINAR ESTUDIANTE X NOMBRE-")
                litar_registros(estudiantes)
                nombre_estudiante=input("Nombre del estudiante que desea eliminar: ")
                eliminar_registro(estudiantes,nombre_estudiante)
            case "6":
                print("--SALIR--")
                break
        
main_function()

