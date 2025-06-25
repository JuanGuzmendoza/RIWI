
#==== Forma con WHILE ====

i=1
numeros_positivos=0
while i <=5:
    numero=int(input(f"Ingrese el {i} numero:  "))
    if numero>0:
        numeros_positivos+=1
    i+=1
print(f"Cantidad de numeros positivos: {numeros_positivos}")



#==== Forma con FOR ====
numeros_positivos=0
for i in range(1,6):
    numero=int(input(f"Ingrese el {i} numero:  "))
    if numero>0:
        numeros_positivos+=1
print(f"Cantidad de numeros positivos: {numeros_positivos}")