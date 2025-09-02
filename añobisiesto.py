año=int(input("Ingresa el año: "))
if (año %4 == 0 and año %100 != 0) or (año %400 == 0):
    print("El año es Bisiesto")
else:
    print("El año no es Bisiesto")
