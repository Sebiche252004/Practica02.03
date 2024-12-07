
# Tablas de multiplicar

numero = int(input("Introduzca el numero del que quieras ver su tabla de multiplicar"))

for n in range(10):
    print(numero,"x",(n+1),"=",numero*(n+1))
