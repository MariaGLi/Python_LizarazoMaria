from os import system
import json

lista1=[]

with open("C:/Users/USUARIO/Desktop/Python_LizarazoMaria/Dia11/large-file.json", encoding="utf-8") as file:
    datos = json.load(file)

lista2=[0,0,0,0,0,0,0,0,0,0,0,0,0,0]

for i in datos: 
    lista1.append(i["type"])
    if i["type"] == "MemberEvent":
        lista2[0]+=1
    elif i["type"] =="IssuesEvent":
        lista2[1]+=1
    elif i["type"] =="PushEvent":
        lista2[2]+=1
    elif i["type"] =="ReleaseEvent":
        lista2[3]+=1
    elif i["type"] =="CommitCommentEvent":
        lista2[4]+=1
    elif i["type"] =="DeleteEvent":
        lista2[5]+=1
    elif i["type"] =="PullRequestEvent":
        lista2[6]+=1
    elif i["type"] =="CreateEvent":
        lista2[7]+=1
    elif i["type"] =="IssueCommentEvent":
        lista2[8]+=1
    elif i["type"] =="GollumEvent":
        lista2[9]+=1
    elif i["type"] =="PublicEvent":
        lista2[10]+=1
    elif i["type"] =="WatchEvent":
        lista2[11]+=1
    elif i["type"] =="PullRequestReviewCommentEvent":
        lista2[12]+=1
    elif i["type"] =="ForkEvent":
        lista2[13]+=1

lista0=list(set(lista1))

sel=0 # le damos valor a nuestra variable sel-eccion para asi poder ejecutarla en nuestro while
while sel!=5:  # hacemos un while para hacer un bucle a nuestras tres opciones
    system("cls") # colocamos un limpiaar pantalla
    print("""
    ---------------REALIZA UN CRUD----------------
          
    ¿Que deseas hacer?
          
    1. Crear un evento.
    2. Eliminar un evento.
    3. Revisar la cantidad de eventos.
    4. Actualizar los eventos.
    5. Salir del programa.
          
    ----------------------------------------------
    """) #Creo un menú
    sel=int(input("Digita el numero de lo primero que deseas hacer:\n")) # Le pedimos al usuario que por favor ingrese el numero de alguna de nuestras opc.

    if sel == 1: # si nuestra opcion es uno, nos pedira agg productos al carrito.

        print("----------Agg un evento----------")

        nombEN=input("Ingrese el nombre del evento a crear\n")
        if nombEN in lista0:
            print("Ojo, ese evento ya existe solo actualice su cantidad")
        else:
            cantEN=input("Ingrese la cantidad de eventos que a crear\n")
            print("Has creado un nuevo evento con exito")
            lista0.append(nombEN)
            lista2.append(cantEN)

            input("Para continuar presione enter.")

    if sel == 2:

        print("----------Eliminar un evento----------")

        cont=0
        nombEE=input("Digite el nombre del evento que ya no desea hacer\n")
        if nombEE in lista0:
            while nombEE in lista0:
                if nombEE== lista0[cont]:
                    lista0.remove(nombEE)
                    lista2.pop(cont)
                    print("Ha eliminado el evento con exito")
                else:
                    cont+=1
        else:
            print("Ojo, no puede eliminar algo que no está creado.")

        input("Para continuar presione enter.")

    if sel == 3:

        print("----------Revisa la cantidad de eventos que tienes----------")

        for i in range(0,len(lista0)): 
            print("Evento:",lista0[i], "Cantidad:",lista2[i])

        input("Para continuar presione enter.")

    if sel == 4:

        print("----------Actualice la cantidad de eventos que tiene----------")

        cont1=0
        boleano=True
        nombEA=input("Nombre del evento a actualizar\n")
        if nombEA in lista0:
            cantEA=int(input("Ingrese la cantidad de eventos que desea añadir, de lo contrario, por favor digitar el numero en negativo\n"))
            while nombEA in lista0 and boleano==True:
                if nombEA== lista0[cont1]:
                    lista2[cont1]+=cantEA
                    print("Evento actualizado con exito")
                    boleano=False
                else:
                    cont1+=1
        else:
            print("Evento no encontrado, por favor revisar nuevamente la lista.") 
            input("Para continuar presione enter.")

else:
    print("El programa se ha cerrado.")
    input("Presione enter para finalizar.")

