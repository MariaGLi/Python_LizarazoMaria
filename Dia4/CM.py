from os import system

def menu():
    print("""
    ----------------------BIENVENIDO A NUESTRO BANCO------------------------
    1. Veamos la manera de cambio de moneda
    2. Salir
    """)



opc=0 # le damos valor a nuestra variable sel-eccion para asi poder ejecutarla en nuestro while
while opc!=2:
    system("cls")

    print("""
    ----------------------BIENVENIDO A NUESTRO BANCO------------------------
    1. Veamos la manera de cambio de moneda
    2. Salir
    """)
    opc=int(input("Indique lo que desea hacer:\n"))
    print("")

    cambio=(10, 5, 1)
    entrega=("")

    plata=int(input("Ingrese el dinero que desea retirar\n"))

    if opc==1:
        p=0
        for x in cambio:
            entrega = plata//x

            if entrega >= 10:
                print("las monedas entregadas de ", x, " son: ", entrega)
                p=p+10
                

            elif entrega >= 5:
                print("las monedas entregadas de ", x, " son: ", entrega)
                p=p+5
                

            elif entrega >= 1:
                print("las monedas entregadas de ", x, " son: ", entrega)
                p=p-4
                
                    
        input("Para continuar presiona enter.")    

    if opc==2:
        print("el programa ha terminado")
        input("Para continuar presiona enter.") 

        