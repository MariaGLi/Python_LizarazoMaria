numeros = [2,7,11,15]
num = len(numeros)
print(numeros)

if num:
    for x in range (0,num,1):
            y=x+1
            if numeros[x]+numeros[y]==26:
                print("[",x,",",y,"]")
                break