from os import system


def menu(): # Definimos el menu que deseamos

    print("""
    ---------------BIENVENIDO AL MENU-----------------
    ¿Que deseas hacer?
    1. Crea una contraseña segura.
    2. Deseo terminar el programa.
    ---------------------------------------------------
    """) #Escribimos las opciones que queremos dentro de nuestro menú
    
sel=0 # le damos valor a nuestra variable sel-eccion para asi poder ejecutarla en nuestro while
while sel!=2:  # hacemos un while para hacer un bucle a nuestras tres opciones
    system("cls") # colocamos un limpiaar pantalla
    print("""
    ---------------BIENVENIDO AL MENU-----------------
    ¿Que deseas hacer?
    1. Crea una contraseña segura.
    2. Deseo terminar el programa.
    ---------------------------------------------------
    """) #Escribimos nuevamente nuestro menú, pero esta ves dentro de nuestro while
    sel=int(input("Digita el numero de lo primero que deseas hacer:\n")) # Le pedimos al usuario que por favor ingrese el numero de alguna de nuestras opc.
    
    if sel==1: #si la seleccion del usuario es dos, nos dirigira a crear la clave segura
        import random # se importa la variable random, para que esta nos ayude a mezclar todos los caracteres
        import string
        def generarcontraseña(longitud): #Se crea la variable generarcontraseña con longitud infinita
            min=string.ascii_lowercase
            mayus=string.ascii_uppercase
            num=string.digits
            symb=string.punctuation
            print(symb)
            #se crea la variable caracteres
            contraseña = "" #se crea la variable contraseña, que es la que nos va a sevir para almacenar los datos
            
        longitud=int(input("¿Cual es el tamaño de la contraseña que usted desea?\n")) #en esta parte, le solicitamos al usuario la longitud que se necesita para la conttraseña    
        si=print(input("¿Desea añadir mayusculas a su contraseña? presione 1, de lo contrario, oprima 0"))
        if si ==1:
            
        


        
        for i in range(longitud): # se crea un for, con el fin e que este se repita las veces que el usuario indique en el tamaño de la contraseña
            #contraseña += random.choice() # la variable caracteres actuara de la mano con la variable random para asi, darnos la clave con la longitud de los caracteres solicitada po el usuario
            #return contraseña #aca, nos retorna la contraseña
        
        
        #nuevacontraseña = generarcontraseña(longitud) # se crea y pone en accion la variable nueva contaseña para que en esta quede guardada la contraseña final ddel usuario
        #print("La nueva contraseña es: ", nuevacontraseña) # acaa, mostramos la contraseña con la longitos solicitaa por el usuario

            input("Para continuar presiona enter.") #hacemos este continuar para que nos retorne al inicio del menu

    else:
        print("Ha finalizado el programa") #si el usuario llegase a seleccionar el numero tres, el programa se finalizara.
    
    