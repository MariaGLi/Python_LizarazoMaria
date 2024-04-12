
print("""
---------------BIENVENIDO AL MENU-----------------
¿Que deseas hacer?
1. Digite un numero y vea si es primo o no.
2. Crea una contraseña segura.
3. Deseo terminar el programa.
---------------------------------------------------
      """)

sel=1
sel=2
sel=3

sel=int(input("Digita el numero de lo primero que deseas hacer:\n"))

if sel==1:
    g=int(input("Ingresa el numero que deseas saber si es primo o no.\n"))
    p=0
    for i in range (1, (1+g), 1):
        if g % i == 0:
            p=p+1
    if p==2:
        print(g, "Es un numero primo")
        
    else:
        print(g, "No es un numero primo")

if sel==2:
    import random
    def generarcontraseña(longitud):
        caracteres = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ°!#$%&/\=?¡¿-_;}.,+{*"
        contraseña = ""
        for i in range(longitud):
            contraseña += random.choice(caracteres)
        return contraseña
    
    longitud=int(input("¿Cual es el tamaño de la contraseña que usted desea?"))
    nuevacontraseña = generarcontraseña(longitud)
    print("La nueva contraseña es: ", nuevacontraseña)
    
if sel==3:
    print("Ha finalizado el programa")