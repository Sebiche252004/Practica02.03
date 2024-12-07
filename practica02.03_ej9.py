#triangulo impar

n=int(input("Introduce un numero"))
for j in range(1,n+1,1):
    print("")
    for i in range(1,2*j,2):
        print(i, end=" ")
print("\n")