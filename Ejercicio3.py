opcion=100


print("1. ver el producto que selecciono ")
print("2. Ver todos los productos ")
print("3. Agregar producto nuevo")
print("4. Eliminar ultimo producto")
print("0. SALIR \n")


productos=[]
while opcion != 0:
    opcion=int(input("Digita una opcion: "))
    
    if opcion==1:
        for producto in productos:
            print (f'el producto que selecciono es: {producto}') 

    elif opcion==2:
         print(productos)
    
    elif opcion == 3:
        producto=input("Digite el nombre del producto: ")
        productos.append(producto)

    elif opcion==4: 
        productos.pop()
        print(productos)
        

    elif opcion==0:
        print("Gracias ...")
        break
    else:
        print("Selecionar opcion valida...")