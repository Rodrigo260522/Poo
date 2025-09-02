cal=int(input("Ingresa la calificacion (0-100): "))
if (cal > 100) and (cal < 0) or (cal != (0-100)):
    print("Esa no es una calificaion")
elif cal >= 90 and cal <= 100:
    print("La calificacion es: A")
elif cal >= 80 and cal < 90:
    print("La calificacion es: B")
elif cal >= 70 and cal < 80:
    print("La calificacion es C")
elif cal >= 60 and cal < 70:
    print("La calificacion es: D")
else:
    print("La calificacion es: F")
