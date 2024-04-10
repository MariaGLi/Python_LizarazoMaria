
print("Bienvenido a mi primer programa en python.")
print("A continuación mostraremos la secuencia Fibonacci.\n")

while True:
    g= int(input("Ingrese el numero que desea para la secuencia fibonacci\n"))

    a=1
    b=0
    c=1
    print("\n")
    while a <= g:

        if a%2==1:
            print(b)
            b=b+c
        else:
            print(c)
            c=c+b
        a=a+1

    j=int(input("Si quieres seguir en el programa, coloca 1\n"))
    if j==1:
        print("El programa empezara nuevamente.")
    else:
        print("El programa ha terminado")
        break