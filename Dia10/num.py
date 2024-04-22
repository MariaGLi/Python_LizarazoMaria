#Lista
num=input("Numeros: ") #solicitamos al usuario ingresar los numeros que desea enlistar
Lista=list(sorted(set(map(int, num.split(","))))) # creamos la variable que nos permitira guardar los numeros en la lista

#Variable
cont=0 # creamos la variable contador para usarla en el for

numero=int(input("")) # el usuario ingresara el numero que desea saber en que posicion esta

#Ciclo
for i in Lista: 
    cont+=1 # el contador me va a ayudar a que passe por todos los numeros de la lista y me de la posicion
    if numero == i: # se realiza un if para verificar si el numero esta o no en la lista
        print(cont-1) # imprimira el numero
        break # break para cerrar el ciclo

Lista.append(numero) # se hace la lista .append para que me organice los numeros en la ultima posicion
Lista.sort() # .sort me organiza los numeros de menor a mayor
nlist=list(set(Lista)) # set me elimina los numeros repetidos
print(nlist) # me imprime la lista 

con1=0 # se crea un 2do contador 
#Ciclo
for i in Lista: 
    con1+=1 # el contador me va a ayudar a que si el numero escrito por el usuario se encuentra va a llamar la posicion donde se encuentra el numero
    if numero == i: # se realiza un if para verificar si el numero esta o no en la lista
        print(con1-1) # imprimira el numero
        break # break para cerrar el ciclo