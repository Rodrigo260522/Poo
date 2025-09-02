lado1=float(input("Ingresa la longitud del primer lado: "))
lado2=float(input("Ingresa la longitud del segundo lado: "))
lado3=float(input("Ingresa la longitud del tercer lado: "))
if lado1==lado2 and lado2==lado3:
    print("El triangulo es equilatero")
elif (lado1 == lado2 and lado1 != lado3) or (lado1 == lado3 and lado1 != lado2) or (lado2 == lado3 and lado2 != lado1):
    print("El triangulo es isosceles")
else:
    print("El triangulo es escaleno")
