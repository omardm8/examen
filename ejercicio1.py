numeros=0
for f in range(10):
    valor=int(input("ingrese un valor "))
    if valor!= 0:
        if valor%3==0:
            numeros=numeros+1
print(" La cantidad de números ingresados múltiplos de 3 es: ")
print(numeros)
