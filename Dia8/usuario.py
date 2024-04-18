from os import system

Usuario=[]
Contraseña=[]

sel=0 # le damos valor a nuestra variable sel-eccion para asi poder ejecutarla en nuestro while
while sel!=4:  # hacemos un while para hacer un bucle a nuestras tres opciones
    system("cls") # colocamos un limpiaar pantalla
    print("""
    ---------------BIENVENIDO AL Q'HUBO TIBUYANO----------------
    ¿Que deseas hacer?
    1. Iniciar sesión.
    2. Comprar una credencial.
    3. Añadir dinero a la cuenta bancaria.
    4. ¿Desea terminar el programa?.
    ---------------------------------------------------
    """)
    sel=int(input("Digita el numero de lo primero que deseas hacer:\n")) # Le pedimos al usuario que por favor ingrese el numero de alguna de nuestras opc.

    if sel == 1:
        Us=input("Ingrese el usuario")
        if Us in Usuario:
            print("Usuario correcto.")
        else:
            print("No tienes credencial, compra una.")
        input("Para continuar presione enter.")
    
    if sel == 2:
        Usu = input("Agrega el usuario")
        Usuario.append(Usu)
        


    #if sel == 3:

    
else:
    print("El programa se ha cerrado.")
    input("Para continuar presione enter.")