from os import system

def menu(): # Definimos el menu que deseamos

    print("""
    ---------------BIENVENIDO AL MENU-----------------
    ¿Que deseas hacer?
    1. Digite un numero y vea si es primo o no.
    2. Crea una contraseña segura.
    3. Deseo terminar el programa.
    ---------------------------------------------------
    """) #Escribimos las opciones que queremos dentro de nuestro menú
    
sel=0 # le damos valor a nuestra variable sel-eccion para asi poder ejecutarla en nuestro while
while sel!=3:  # hacemos un while para hacer un bucle a nuestras tres opciones
    system("cls") # colocamos un limpiaar pantalla
    print("""
    ---------------BIENVENIDO AL MENU-----------------
    ¿Que deseas hacer?
    1. Digite un numero y vea si es primo o no.
    2. Crea una contraseña segura.
    3. Deseo terminar el programa.
    ---------------------------------------------------
    """) #Escribimos nuevamente nuestro menú, pero esta ves dentro de nuestro while
    sel=int(input("Digita el numero de lo primero que deseas hacer:\n")) # Le pedimos al usuario que por favor ingrese el numero de alguna de nuestras opc.
    
    if sel==1: # si nuestra opcion es uno, nos guiara a saber si el numero es primo o no.
        g=int(input("Ingresa el numero que deseas saber si es primo o no.\n")) # se solicita al usuario cualquier numero
        p=0 # se hace un contador
        for i in range (1, (1+g), 1): # se hace un for para que nos verifique las posibilidades de division o modulacion
            if g % i == 0: # aca hacemos la operacion para que si la diviion es cero, nos vote si es primo o no, mas adelante
                p=p+1 # el contador se ira sumando respectivamente
        if p==2: #si el contador nos da dos, nos mostrara que el numero es primo
            print(g, "Es un numero primo") # y nos imprimira el sgte mensaje
            
        else:
            print(g, "No es un numero primo") # de lo contrario nos imprimira este.

    if sel==2: #si la seleccion del usuario es dos, nos dirigira a crear la clave segura
        import random # se importa la variable random, para que esta nos ayude a mezclar todos los caracteres
        def generarcontraseña(longitud): #Se crea la variable generarcontraseña con longitud infinita
            caracteres = "1234567890abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ°!#$)%(&/\=?¡¿-_;}.,+{*"  #se crea la variable caracteres
            contraseña = "" #se crea la variable contraseña, que es la que nos va a sevir paa almacenar los datos
            for i in range(longitud): # se crea un for, con el fin e que este se repita las veces que el usuario indique en el tamaño de la contraseña
                contraseña += random.choice(caracteres) # la variable caracteres actuara de la mano con la variable random para asi, darnos la clave con la longitud de los caracteres solicitada po el usuario
            return contraseña #aca, nos retorna la contraseña
        
        longitud=int(input("¿Cual es el tamaño de la contraseña que usted desea?\n")) #en esta parte, le solicitamos al usuario la longitud que se necesita para la conttraseña
        nuevacontraseña = generarcontraseña(longitud) # se crea y pone en accion la variable nueva contaseña para que en esta quede guardada la contraseña final ddel usuario
        print("La nueva contraseña es: ", nuevacontraseña) # acaa, mostramos la contraseña con la longitos solicitaa por el usuario

    input("Para continuar presiona enter.") #hacemos este continuar para que nos retorne al inicio del menu

    if sel==3:
        print("Ha finalizado el programa") #si el usuario llegase a seleccionar el numero tres, el programa se finalizara.
    
    