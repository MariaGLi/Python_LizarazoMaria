import random
g=random.randint(1,100)

print("Este juego se trata de adivinar un numero aleatorio en 10 intentos...")

for i in range (1,11,1):
        z=int(input("Digita el número con el que deseas probar suerte.\n"))
        if z==g:
            print("Felicitaciones, has acertado el número, en el intento # ",i)
            break
        else:
            if z<g:
                print("Paila compañero, el número es mas alto")

            if z>g:
                print("Nooo compañero, se subio mucho.")
