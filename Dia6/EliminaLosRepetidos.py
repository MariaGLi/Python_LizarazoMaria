numeros=[]
<<<<<<< HEAD
numeros1=int(input("digita la cantidad de numeros de la lista, no superior a 300 \n"))
assert 0< numeros1 <300 ,"¡OJO! compañero el numero de la lista no es el correcto."

for x in range (numeros1):
    numeros.append(input())

num= list(set(numeros))
num.sort()

print(num)
=======
numeros1=int(input("digita la cantidad de numeros \n"))

for i in range (0, numeros1):
    numeros.append(input())

unicos=list(set(numeros))
print(unicos)

>>>>>>> ead614e7079ca569ea97a450ae41b558d533ca4c
