numeros=[]
numeros1=int(input("digita la cantidad de numeros de la lista, no superior a 300 \n"))
assert 0< numeros1 <300 ,"¡OJO! compañero el numero de la lista no es el correcto."

for x in range (numeros1):
    numeros.append(input())

num= list(set(numeros))
num.sort()

print(num)