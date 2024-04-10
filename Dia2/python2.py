import random
j=random.randint(1,100)

print("Acompañenme a probar mi primer juego en python :)")
print("El juego trata de adivinar un numero en la menor cantidad de intentos posibles.")

while True:
    a=int(input("Digita el número con el que probar suerte.\n"))
    if a==j:
        print("Has acertado el número")
        break
    else:
        if a<j:
            print("Paila compañero, el número es mas alto")

        if a>j:
            print("Nooo compañero, se subio mucho.")