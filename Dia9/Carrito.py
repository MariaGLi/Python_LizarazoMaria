from os import system

NProducto=[] #Creo un arreglo para guardar los nombres de los productos
PProducto=[] #Creo un arreglo para guardar los precios de los productos
CProducto=[] #Creo un arreglo para guardar las cantidades de los productos

sel=0 # le damos valor a nuestra variable sel-eccion para asi poder ejecutarla en nuestro while
while sel!=3:  # hacemos un while para hacer un bucle a nuestras tres opciones
    system("cls") # colocamos un limpiaar pantalla
    print("""
    ---------------BIENVENIDO AL CARRITO TIBUYANO----------------
    ¿Que deseas hacer?
    1. agg productos al carrito.                                            
    2. Mira que agregaste al carrito
    3. ¿Desea terminar el programa?.
    ---------------------------------------------------
    """) #Creo un menú
    sel=int(input("Digita el numero de lo primero que deseas hacer:\n")) # Le pedimos al usuario que por favor ingrese el numero de alguna de nuestras opc.

    if sel == 1: # si nuestra opcion es uno, nos pedira agg productos al carrito
        carrito = int(input("ingrese la cantidad de articulos desea al carrito\n")) # Creo la variable carrito que nos permitira saber cuantos productos agg el usuario

        for i in range(carrito):   # Creamos un for para que nos pase la cantidad de veces que el usuario haya dicho.
            nombre = str(input("Cual es el nombre del articulo que desea ingresar\n")) # el usuario ingresara el nombre del producto que desea
            precio = int(input("Cual es el precio del articulo que desea ingresar\n")) # el usuario ingresara el precio al producto ingresado
            cantidad = int(input("La cantidad de los articulos que va a ingresar es:\n")) # el usuario ingresara la cantidad de productos que desea
            NProducto.append(nombre) # usamos la función append para que nos organice lo ingresado en el arreglo vacio
            PProducto.append(precio) # usamos la función append para que nos organice lo ingresado en el arreglo vacio
            CProducto.append(cantidad) # usamos la función append para que nos organice lo ingresado en el arreglo vacio

        input("Para continuar presione enter.") # este input nos ayuda con el limpiar pantalla

    if sel == 2:  # si nuestra opcion es dos, nos mostrará lo agg al carrito
        for i in range (0, len(NProducto)):  # Creamos un for para que nos organice la informacion de maner mas "bonita"
            print("Nombre del producto: ", NProducto[i], " Cantidad del producto: ", CProducto[i], " Precio del producto: ", PProducto[i])

        input("Para continuar presione enter.") # este input nos ayuda con el limpiar pantalla

else:  # si nuestra opcion es =! 3, nos cerrara el programa...
    print("El programa se ha cerrado.")
    input("Presione enter para finalizar.")

# Realizado por María Lizarazo.