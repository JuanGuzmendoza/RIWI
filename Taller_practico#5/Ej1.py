
cursos=("Python Basico","Javascript","Html/Css")

def listar_cursos(curso):
    for i in cursos:
        if curso==i.lower().replace(" ",""):
            print(f"El curso {i} si se encuentra en la lista de cursos")
            return True
while True:
    curso_buscar=input("Ingrese el nombre del curso que quiere buscar: ")
    curso_buscar=curso_buscar.lower().replace(" ","")
    respuesta=listar_cursos(curso_buscar)
    if respuesta==True:
        print("-FIN-")
        break
    else:
        print("Curso no encontrado")