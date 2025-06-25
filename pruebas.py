
# numero_buscar=input("Ingrese el numero que quiere buscar: ")
# contador_relaciones=0
# suma_acumulador_relaciones=0
# contador_coincidencia_unitaria=0
# for i in range(10):
#     numero=input(f"Ingrese el numero {i}: ")
#     if numero_buscar in numero:
#         suma_acumulador_relaciones+=int(numero)
#         contador_relaciones+=1

# print(f"Relaciones: {contador_relaciones}")
# print(f"Suma total: {suma_acumulador_relaciones}")





 
numero_buscar=input("Ingrese el numero que quiere buscar: ")
contador_relaciones=0
suma_acumulador_relaciones=0
contador_coincidencia_unitaria=0
for i in range(10):
    numero=input(f"Ingrese el numero {i}: ")
    for i2 in range(len(numero)):
        for i3 in range(len(numero_buscar)):
            print(f"{numero_buscar[i3]} == {numero[i2]}")
            if contador_coincidencia_unitaria ==len(numero_buscar):
                i3=len(numero_buscar)
                i2=len(numero)
                break
            if numero_buscar[i3]==numero[i2]:
                contador_coincidencia_unitaria+=1
                print("COINCIDEN")
                i2+=1
            else:
                contador_coincidencia_unitaria=0
                i3+=1
                print("NO COINCIDEN")
    print(f"Coincidencia unitarias encontradas: {contador_coincidencia_unitaria}")
    print(f"len {len(numero_buscar)}")
    if contador_coincidencia_unitaria==len(numero_buscar):
        contador_relaciones+=1
print(f"Relaciones: {contador_relaciones}")
