#tributar

edad= int(input("Introduzca su edad"))
ingresos= int(input("Introduzca cuanto ingresa al mes"))

if edad >= 16:
    if ingresos >= 1000:
        print("Es necesario que tributes")
    else:
        print("No es necesario que tributes")
elif edad<16:
    print("No es necesario que tributes")
else:
   print("es necesario que tributes")