#-------------------------------------------
#---------Day cheat sheet python------------

# Imprimir hola mundo
print("Hola mundo.")

#Datos primitivos

#Numero
numerito=7*5 #Nombre valor=valor
print(numerito) #imprimir(variable)
print(type(numerito)) #imprimir (tipo(variable))

#Numero decimal
numerodecimal=5.2*2.3 
print(numerodecimal)
print(type(numerodecimal))

#Booleano
Booleano=True
print(Booleano)
print(type(Booleano))

#Cadena de texto
texto= "Mi hermoso Tibú"
print(texto)
print (type(texto))

#Desarrollado por Maria Guadalupe Lizarazo Leal c.c 1.000.000.000

# 1. ingresa por teclado información
edad = int(input("Ingrese su edad: "))
altura = float(input("Ingrese su altura en metros: "))

print("---------------------------")

# 2. CONVERTIR VARIABLE
m=24
g=24.27
jj=32.05
j=32
print(float(m))
print(int(g))
print(int(jj))
print(float(j))

print("-----------------------")

# 3. bucles for and while

a= int(input("Ingrese un valor: "))
for i in range(1,(1+a)) :
    print (i*a)

print ("-------------------------")

c=1
while c<10 :
    print(c*2)
    c=c+1

print("---------------------------")

# 4. 4 tipos de funciones

sum([1, 2, 3, 4, 5])
print(sum)
