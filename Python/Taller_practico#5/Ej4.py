
cursos=["Matematicas","Ingles","Español"]

estudiantes_cursos=[("Juan","Ingles"),("Mendozza","Español")]


def agregar_estudiante_curso():
    print("--PARTE PARA AGREGAR ESTUDIANTES A CURSOS--")
    nombre_estudiante=input("Ingrese nombre del estudiante")
    print("--CURSOS PARA INCRIBIR --")
    for i in range(len(cursos)):
        print(f"{i}- {cursos[i]}")
    print(f"Seleccione Curso en el cual ingresara {nombre_estudiante}")
    curso_seleccionado=int(input("--"))
    estudiantes_cursos.append((nombre_estudiante,cursos[curso_seleccionado]))

def listar_estudiantes():
    print("--OPCION PARA MOSTRAR TODOS LOS ESTUDIANTES--")
    for i in estudiantes_cursos:
        print(f"Estudiante: {i[0]} Curso:{i[1]}")


def buscar_estudiantexcurso():
    print("--MOSTRAR ESTUDIANTES DE UN CURSO--")
    print("-CURSOS-")
    for i in range(len(cursos)):
        print(f"{i} - {cursos[i]}")

    print(f"Seleccione el curso el cual quiere ver los estudiantes")
    curso_seleccionado=int(input("--"))
    print(f"-ESTUDIANTES DEL CURSO {cursos[curso_seleccionado]}")
    for i in estudiantes_cursos:
        if i[1]==cursos[curso_seleccionado]:
            print(i[0])

def eliminar_tupla():
    print("--OPCION PARA ELIMINAR ESTUDIANTE--")
    print("-ESTUDIANTES-")
    for i in estudiantes_cursos:
     print(f" {i[0]}")
    print("Nombre del estudainte el cual desea eliminar")
    estudiante_seleccionado=input("--")
    
    for i in range(len(estudiantes_cursos)):
        if estudiantes_cursos[i][0]==estudiante_seleccionado:
            print(f"Estudainte {estudiantes_cursos[i][0]} fue borrado")
            estudiantes_cursos.pop(i)
            print("-NUEVA LISTA DE ESTUDIANTES-")
            for i in estudiantes_cursos:
                print(f"{i[0]} - {i[1]}")
            break
    

def main_function():
    while True:
        print("---CRUD ESTUDIANTES-CURSOS---")
        print("1.Agregar nuevo estudiante a curso")
        print("2.Mostrar todos los estudiantes")
        print("3.Buscar estudiantes por curso")
        print("4.Eliminar estudiante x nombre")
        print("Ingrese una opcion")
        opcion=input("--")
        match opcion:
            case"1":
                agregar_estudiante_curso()
            case"2":
                listar_estudiantes()
            case"3":
                buscar_estudiantexcurso()
            case"4":
                eliminar_tupla()
            case _:
                break

main_function()