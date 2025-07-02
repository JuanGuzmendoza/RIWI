
#-Funcion que determina el estado de la aprobacion de varios estudiantes y dando analisis respecto al grupo analisado
def determinar_estado_aprobacion():
    #Definicion de variables y array que se usaran:
    estudiantes=[]
    notas_estudiante=[]
    aprobados=0
    reprobaron=0
    pregunta=""
    #While el cual manejara las preguntas para ingresar las notas de los estudiantes
    while pregunta!="no":
        estudiante_nombre=input("Ingrese el nombre del estudiante: ")
        print(f"Ingrese la nota del estudiante {estudiante_nombre}")
        while True:
            try:
                nota=float(input("-"))
                if nota > -1 and nota <= 100:
                    break
                else:
                    print("Solo se pueden valores de 0-100")
            except:
                print("Ingrese solamente numeros.")
        notas_estudiante.append(nota)
        #Se guarda los estudiantes con su nombre y nota 
        estudiantes.append([estudiante_nombre,notas_estudiante])
        if nota >= 60:
            print("!Estudiante \033[92m Aprobado \033[0m!")
            aprobados+=1
        else:
            print("!Estudiante \033[31m Reprobado \033[0m!")
            reprobaron+=1
        notas_estudiante=[]
        #Se hace la pregunta de que si se quiere agregar otro estudiante
        pregunta=input("Desea calificar otro estudiante? -si ,-no : ")

    print(f'\033[92m'+"""

        --LISTA DE ESTUDIANTES CALIFICADOS--"""+'\033[0m')
    for i1 in range(len(estudiantes)):
        print(f"-Estudiante: {estudiantes[i1][0]}")
        for i2 in range(len(estudiantes[i1][1])):
            print(f"  Nota: {estudiantes[i1][1][i2]}")
        if estudiantes[i1][1][i2] >= 60:
            print('\033[92m'+f"APROBADO \033[0m")
        else:
            print('\033[31m'+f"REPROBADO \033[0m")
    print(f'\033[92m'+"""
        -- ESTADISTICAS DEL GRUPO --"""+'\033[0m')
    print(f"Total de estudiantes calificados: {len(estudiantes)}")
    print(f"Estudiantes \033[92m APROBADOS \033[0m : {aprobados}")
    print(f"Estudiantes \033[31m REPROBADOS \033[0m : {reprobaron}")


#Funciona la cual permite calcular el promedio de un estudiante por una lista separada por (,)
def Calcular_el_promedio():
    acum_notas=0
    while True:
        try:
            estudiante=input("Ingrese nombre de estudiante: ")
            lista_ca=llenar_lista_comas()
            for i in lista_ca:
                    acum_notas+=i
        except:
            print("Solo valores numericos del 0-100")
        promedio=acum_notas/len(lista_ca)
        print(f'\033[92m'+"""
            -- ANALISIS FINAL --"""+'\033[0m')
        print(f"\033[33m--ESTUDIANTE--\033[0m\n  {estudiante}")
        print(f"\033[33m--NOTAS--\033[0m")
        for i in lista_ca:
            print(f"  -{i}")
        print(f"\033[33m--PROMEDIO FINAL--\033[0m\n  {promedio}")
        print(f"\033[33m--ESTADO--\033[0m")
        if promedio > 60:
            print("\033[92m APROBADO \033[0m")
        else:
            print("\033[31m REPROBADO \033[0m ")
        while True:
            #Menu el cual solo se mostrara luego de terminar la ejecucion de mostar el promedio de la lista de notas
            print("""
            \033[92m--OPCIONES EXTRAS--\033[0m""")
            print("1.Volver a sacar el promedio de una lista de notas")#Permitira volver a sacar otro promedio de notas
            print("2.Contar calificaciones mayores a un numero")#Permitira hacer la funcion de mostrar los numeros mayores a otro numero
            print("3.Verificar y contar una calificacion en especifica")#Permitira hacer la funcion de contar los numeros iguales en una lista
            print("4.Salir al menu principal")#Permite salir del programa directamente

            op=input("-")
            print("-"*40)
            if op=="1":
                break
            elif op=="2":
                Contar_calificaciones_mayores(lista_ca)
                continue
            elif op=="3":
                Verificar_contar_calificaciones_específicas(lista_ca)
                continue
            elif op=="4":
                break
        if op=="4":
            break

#Funcion la cual permitira buscar calificaciones mayores dependiendo del numero agregado
#Defino en los parametros la lista=[] porque la funcion se podra llamar desde otros lados ya con una nueva lista 
#y cuando se llame sin pasarle lista en la primera condicion de la funcion evalua si esta vacia o no
def Contar_calificaciones_mayores(lista=[]):
    if len(lista)<=0:
       lista=llenar_lista_comas()
    print("\n\033[92m--CONTAR CALIFICACIONES MAYORES A--\033[0m")
    while True:
        try:
            numero_mayor_buscar=float(input("Numero el cual se buscaran los mayores: "))
            break
        except:
            print("Solamente se permiten digitos numericos")
    cont=0
    print(f"\033[33m--NUMERO MAYORES A {numero_mayor_buscar}--\033[0m")
    for i in lista:
        if i >numero_mayor_buscar:
            cont+=1
            print(f"Numero: {i}")
    print(f"Cantidad de numeros mayores a {numero_mayor_buscar}: {cont}")
    print("-"*40)

#Funcion la cual encuentra notas iguales en una lista de notas
#Defino en los parametros la lista=[] porque la funcion se podra llamar desde otros lados ya con una nueva lista 
#y cuando se llame sin pasarle lista en la primera condicion de la funcion evalua si esta vacia o no
def Verificar_contar_calificaciones_específicas(lista=[]):
    if len(lista)<=0:
        lista=llenar_lista_comas()
    print("\n\033[92m--VERIFICAR CALIFICACIONES ESPECIFICAS--\033[0m")
    while True:
        try:
            numero_igual_buscar=float(input("Numero el cual se buscaran la igualdad: "))
            break
        except:
            print("Solamente se permiten digitos numericos")
    cont=0
    print(f"\033[33m--NUMERO IGUALES A {numero_igual_buscar}--\033[0m")
    for i in lista:
        if i ==numero_igual_buscar:
            cont+=1
    print(f"Cantidad de numeros iguales a {numero_igual_buscar}: {cont}")
    print("-"*40)


#Funcion la cual ayuda a pedir notas anidadas por (,) y hacer las verificaciones de valor
def llenar_lista_comas():
    while True:
        try:
            lista=input("Ingrese las notas separas por (,): ")
            lista=lista.split(",")
            for i in range(len(lista)):
                lista[i]=float(lista[i])
            sum(lista)
            c=0
            for i in lista:
                if i < 0 or i >100:
                    print(f"El valor {i} no esta entre el rango 0-100")
                    break
                else:
                    c+=1
            if c==len(lista):
                break
        except:
            print("Solo valores numericos del 0-100")
    return lista


#Funcion principal(Menu principal)
def funcion_inicio():
    while True:
        print("-"*40)
        print("CALIFICACIONES Y ESTADISTICAS DE NOTAS") 
        print("-"*40)

        #Prints para el menu
        print("\033[92m--OPCIONES--\033[0m".center(50))
        print("\033[92m--1 \033[0m Determinar el estado de aprobación")
        print("\033[92m--2 \033io[0m Calcular el promed")
        print("\033[92m--3 \033[0m Contar calificaciones mayores")
        print("\033[92m--4 \033[0m Verificar y contar calificaciones específicas")
        print("\033[92m--5 \033[0m Salir del programa")

        opcion=input("\nIngrese la opcion que quiere usar(1-5): ".center(40))
        #Parte donde se llaman las funciones dependiendo de la opcion usada
        match opcion:
            case "1":
                determinar_estado_aprobacion()
            case "2":
                Calcular_el_promedio()
            case "3":
                Contar_calificaciones_mayores()
            case "4":
                Verificar_contar_calificaciones_específicas()
            case "5":
                break
        opcion=input("Desea \033[31m 1.SALIR \033[0m o  \033[92m 2.VOLVER_MENU : \033[0m ")
        if opcion=="1":
            break
        else:
            continue



#Llamada a la funcion principal la cual ejecuta el menu principal en donde se podran seleccionar las funciones principales
funcion_inicio()