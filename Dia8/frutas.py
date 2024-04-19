Frutas = [("Mango",0.55,10),("Fresa",4.30,7),("Manzana Verde",0.49,5)]

Nombres_mayusculas = [fruta.upper() for fruta, precio, cantidad in Frutas] # Convertir a mayúsculas
print(Nombres_mayusculas)

frutas_baratas = [fruta for fruta, precio, cantidad in Frutas if precio < 0.50] # Filtrar frutas con precio menor a 0.50
print(frutas_baratas)

FrutaMax=max(Frutas, key=lambda x: x[2]); print(FrutaMax) # Fruta Maxima

Frutas.sort(key=lambda fruta: fruta[1] * fruta[2], reverse=True) # Ordenamos la lista de frutas por el valor en stock (precio * cantidad) en orden descendente
for fruta in Frutas:
    nombre, precio, cantidad = fruta
    print(f"Nombre: {nombre}, Precio: {precio}, Cantidad: {cantidad}, Valor en stock: {precio * cantidad}")