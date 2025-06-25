

num=int(input("Ingrese el numero con el cual comenzara: "))

if num < 0 or num == 0:
    print("Ingrese un  numero mayor que 0")
else:
    for i in range(num,-1,-1):
        print(i)