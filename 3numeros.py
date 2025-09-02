num1=float(input("Ingresa el valor del numero: "))
num2=float(input("Ingresa el valor del numero: "))
num3=float(input("Ingresa el valor del numero: "))
if num1 > num2 and num1 > num3:
    mayor=num1
elif num2 > num1 and num2 > num3:
    mayor=num2
elif num3 > num2 and num3 > num1:
    mayor=num3

if num1 < num2 and num1 < num3:
    menor=num1
elif num2 < num1 and num2 < num3:
    menor=num2
elif num3 < num2 and num3 < num1:
    menor=num3

print("El numero mayor es: ", mayor)
print("El numero menor es: ", menor)