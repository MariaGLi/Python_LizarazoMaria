numeros=[]
numeros1=int(input("digita la cantidad de numeros \n"))

for i in range (0, numeros1):
    numeros.append(input())

unicos=list(set(numeros))
print(unicos)

