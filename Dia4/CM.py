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
    -------------------------------------------------------------------------
    """)
    opc=int(input("Indique lo que desea hacer:\n"))
    print("")

    cambio=(10, 5, 1)
    residuo=0
    residuo1=0

    if opc==1:
        plata=int(input("Ingrese el dinero que desea retirar\n"))
        
        if plata>=10:
            entrega1=int(plata/cambio[0])
            residuo=(plata%cambio[0])

            if residuo>=5:       
                entrega2=int(residuo/cambio[1])
                residuo1=residuo%cambio[1]

                if residuo1>=1:
                    entrega3=int(residuo1/cambio[2])
                else: 
                    entrega3=0

            else:
                entrega2=0
                if residuo1>=1:
                    entrega3=residuo1/cambio[2]
                else:
                    entrega3=0

        else:
            entrega1=0
            if residuo>=5:       
                entrega2=residuo/cambio[1]
                residuo1=residuo%cambio[1]

                if residuo1>=1:
                    entrega3=residuo1/cambio[2]
                else: 
                    entrega3=0

            else:
            
                entrega2=0
                if residuo1>=1:
                    entrega3=residuo1/cambio[2]
                else: 
                    entrega3=0

        print("monedas de 10 ", entrega1)
        print("monedas de 5 ", entrega2)
        print("monedas de 1 ", entrega3)
       


        input("Para continuar presiona enter.")    

    else: 
        print("el programa ha terminado")
        input("Para continuar presiona enter.") 

        