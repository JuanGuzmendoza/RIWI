estudiantes=[]
notas_estudiante=[]
promedio_grupo=0
estudiante_nota_alta=()
estudiante_nota_baja=()
aprobados=0
reprobaron=0
pregunta="si"
nota_final_estudiante=0
while pregunta!="no":
    estudiante_nombre=input("Ingrese el nombre del estudiante: ")
    for i in range(3):
        print(f"Ingrese la nota {i+1} del estudiante {estudiante_nombre}")
        nota=float(input("-"))
        notas_estudiante.append(nota)
        nota_final_estudiante+=nota
        if len(estudiantes) <=0:
            estudiante_nota_alta=(estudiante_nombre,nota)
            estudiante_nota_baja=(estudiante_nombre,nota)
    nota_final_estudiante=nota_final_estudiante/3
    if nota_final_estudiante>estudiante_nota_alta[1]:
        estudiante_nota_alta=(estudiante_nombre,nota_final_estudiante)
    if nota_final_estudiante < estudiante_nota_baja[1]:
        estudiante_nota_baja=(estudiante_nombre,nota_final_estudiante)
    estudiantes.append([estudiante_nombre,notas_estudiante])
    if nota_final_estudiante >= 3:
        print("!Estudiante \033[92m Aprobado \033[0m!")
        aprobados+=1
    else:
        print("!Estudiante \033[31m Reprobado \033[0m!")
        reprobaron+=1
    notas_estudiante=[]
    nota_final_estudiante=0
    pregunta=input("Desea calificar otro estudiante? -si ,-no : ")

print(f'\033[92m'+"""
      
    --LISTA DE ESTUDIANTES CALIFICADOS--"""+'\033[0m')
for i1 in range(len(estudiantes)):
    print(f"-Estudiante: {estudiantes[i1][0]}")
    for i2 in range(len(estudiantes[i1][1])):
        nota_final_estudiante+=estudiantes[i1][1][i2]
        print(f"  Nota{i2+1}: {estudiantes[i1][1][i2]}")
    nota_final_estudiante=nota_final_estudiante/3
    if nota_final_estudiante >= 3:
        print('\033[92m'+f"APROBADO \033[0m - Nota final: {nota_final_estudiante}")
    else:
        print('\033[31m'+f"REPROBADO \033[0m - Nota final: {nota_final_estudiante}")
    print(""" 
    """)
    nota_final_estudiante=0
print(f'\033[92m'+"""
      
    -- ESTADISTICAS DEL GRUPO --"""+'\033[0m')
print(f"Total de estudiantes calificados: {len(estudiantes)}")
print("\n")
print("-Estudiante con la nota final mas \033[92m Alta \033[0m")
print(f"Estudiante: {estudiante_nota_alta[0]} \nNota Final: {estudiante_nota_alta[1]}")
print("\n")
print("-Estudiante con la nota final mas \033[31m Baja \033[0m")
print(f"Estudiante: {estudiante_nota_baja[0]} \nNota Final: {estudiante_nota_baja[1]}")
print("\n")
print(f"Estudiantes \033[92m APROBADOS \033[0m : {aprobados}")
print(f"Estudiantes \033[31m REPROBADOS \033[0m : {reprobaron}")



