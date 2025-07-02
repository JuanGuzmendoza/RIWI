

# diccionario={
#     "juan":{
#     "edad":18,
#     "curso":"Matematicas",
#     "notas":[1,2,3]
# },
# "david":{
#     "edad":18,
#     "curso":"Matematicas",
#     "notas":[1,2,3]
# }}





#----------
#Funciones para Logica de negocio
#----------
def agregar_estudiante(lista,nombre,edad,curso,notas):
    lista[nombre]={
        "edad":edad,
        "curso":curso,
        "notas":notas
    }
    return True

def modificar_curso_edad(lista,nombre_estudiante,valor,tipo):
    for i in lista:
        if i["nombre"]==nombre_estudiante:
            i[tipo]=valor
    return True

def eliminar_registro(lista,nombre_estudiante):
    for i in lista:
        if i==nombre_estudiante:
            lista.pop(i)
            print("----ELIMINADO----")
            break
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
           print(f"--{i}--")
           print(f"Edad: {lista[i]["edad"]}")
           print(f"Curso: {lista[i]["curso"]}")
           print(f"Notas: {lista[i]["notas"]}")
        return True
    else:
        print("No tiene estudiantes")
#----------
#Funcion principal
#----------
def main_function():
    estudiantes={}
    while True: 
        match menu():
            case "1":
                notas=[]

                nombre_estudiante=input("Ingrese el nombre de nuevo estudiante: ")
                for i in range(3):
                    while True:
                        nota=input("Ingrese nota: ")
                        if validar_solo_numeros(nota):
                            notas.append(nota)
                            break
                while True:
                    edad=input("Ingrese la edad: ")
                    if validar_solo_numeros(edad):
                        break
                nombre_curso=input("Nombre del curso: ")
                agregar_estudiante(estudiantes,nombre_estudiante,edad,nombre_curso,notas)
                print("Estudiante agregado")

            case "2":
                litar_registros(estudiantes)

            case "3":
                print("-MODIFICAR CURSO DE ESTUDIANTE-")
                litar_registros(estudiantes)
                nombre_estudiante=input("Nombre del estudiante seleccionado: ")
                nombre_curso=input("Nombre del nuevo curso: ")
                modificar_curso_edad(estudiantes,nombre_estudiante,nombre_curso,"curso")


            case "4":
                print("-MODIFICAR EDAD DE ESTUDIANTE-")
                litar_registros(estudiantes)
                nombre_estudiante=input("Nombre del estudiante seleccionado: ")
                while True:
                    edad=input("Ingrese la edad: ")
                    if validar_solo_numeros(edad):
                        break
                modificar_curso_edad(estudiantes,nombre_estudiante,edad,"edad")

            case "5":
                print("-ELIMINAR ESTUDIANTE X NOMBRE-")
                litar_registros(estudiantes)
                nombre_estudiante=input("Nombre del estudiante que desea eliminar: ")
                eliminar_registro(estudiantes,nombre_estudiante)
            case "6":
                print("--SALIR--")
                break
        
main_function()

