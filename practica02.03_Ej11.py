#Palabra

palabra=input("Introduzca una palabra")

palabra2=int(len(palabra))

for i in range (0,palabra2,1):
    print(palabra[::-1][i])