from os import system

Usuario=[]
Contraseña=[]
Cuenta=[]
PM=10
Regalo=["Jerxon", "Fernanda", "Valentina"]

sel=0 # le damos valor a nuestra variable sel-eccion para asi poder ejecutarla en nuestro while
while sel!=4:  # hacemos un while para hacer un bucle a nuestras tres opciones
    system("cls") # colocamos un limpiaar pantalla
    print("""
    ---------------BIENVENIDO AL Q'HUBO TIBUYANO----------------
    ¿Que deseas hacer?
    1. Iniciar sesión.
    2. Comprar una credencial o añadir dinero a la cuenta bancaria.
    3. ¿Deseas comprar una credencial para regalar?
    4. ¿Desea terminar el programa?.
    ---------------------------------------------------
    """)
    sel=int(input("Digita el numero de lo primero que deseas hacer:\n")) # Le pedimos al usuario que por favor ingrese el numero de alguna de nuestras opc.

    if sel == 1:
        Us=input("Ingrese el usuario\n")
        if Us in Usuario:
            print("Usuario correcto.")

            Con=input("Ingrese su contraseña\n")
            if Con in Contraseña:
                print("Contraseña correcta.")
            else:
                print("Contraseña incorrecta, verifique nuevamente.")
        else:
            print("No tienes credencial, compra una.")
        input("Para continuar presione enter.")
    
    if sel == 2:
        sele=0
        while sele!=3:  # hacemos un while para hacer un bucle a nuestras tres opciones
            system("cls") # colocamos un limpiaar pantalla
            print("""
            ---------------------------------------------------------------
            Quieres comprar la membresía anual o añadir plata a la cuenta.
            1. Quiero comprar mi membresía.
            2. Quiero añadir plata a mi cuenta.
            3. Volver al  menú principal.
            ---------------------------------------------------------------
            """)

            sele=int(input("¿Que deseas hacer?\n"))

            if sele == 1:

                print("Ingresa tus datos para hacer el registro.")
                Usu = input("Agrega el usuario\n")
                Usuario.append(Usu)
                Contra=input("Que contraseña desea agg a su usuario\n")
                Contraseña.append(Contra)
                cm=int(input("Cuantos años de membresía deseas comprar.\n"))
                total=cm*PM
                print("El total a pagar de su membresía es:", total)
                
                total = float(input("Digita el total a pagar por tu membresía\n"))  # Convertir a float
                if total>sum(Cuenta):
                    print("Paila, estas sin plata, por favor ve e ingresa fondos a tu cuenta.")
                else:
                    Cuenta.append(-total)
                    print("Pago realizado.")
                    print("La plata restante es: ", sum(Cuenta))
                    print("Has comprado la membresía con exito.")
                input("Para continuar presione enter.")

            if sele == 2:
                money = float(input("Cuanta plata vas a añadir a tu cuenta\n"))  # Convertir a float
                Cuenta.append(money)
                print("La plata añadida a tu cuenta es: ", sum(Cuenta))  # Sumar todos los valores en la lista

                input("Para continuar presione enter.")

        else:
            input("Para continuar al menú principal presione enter.")   

    if sel == 3:
        pendejadita=input("ingresa el nombre del usuario al que le vas a regalar la membresia.\n")
        if pendejadita in Regalo:
            cm=int(input("Cuantos años de membresía deseas comprar para el regalo.\n"))
            total=cm*PM
            print("El total a pagar de la membresía para el regalo es:", total)
            total = float(input("Digita el total a pagar por la membresía del regalo\n"))  # Convertir a float

            if total>sum(Cuenta):
                print("Paila, estas sin plata, por favor ve e ingresa fondos a tu cuenta para que vuelvas a quedar sin nada.")
            else:
                Cuenta.append(-total)
                print("Pago realizado.")
                print("La plata restante es: ", sum(Cuenta))
                print("Has comprado la membresía para regalar con exito.")
        else:
            print("Paila compañero, el usuario al que le vas a regalar la membresía no existe.")
        input("Para continuar presione enter.")

else:
    print("El programa se ha cerrado.")
    input("Para continuar presione enter.")