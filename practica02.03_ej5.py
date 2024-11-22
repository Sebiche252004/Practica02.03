#hogwarts

nombre=input("introduzca su nombre").capitalize()
sexo= input("introduzca su sexo")

if sexo == "mujer":
    if nombre < "m":
        casa= "gryffindor"
    else:
        casa= "slytherine"
elif sexo == "hombre":
    if nombre > "n":
        casa= "gryffindor"
    else:
        casa= "slytherine"

print("perteneces a", casa)