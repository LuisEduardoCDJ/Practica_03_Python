#3-Crear un programa que muestre los primeros 10 números pares a partir del producto de (10 x 10).
print("los primeros 10 numeros pares del producto 10x10 es: \n")
for x in range(100,122):
 if x % 2 == 0:
    print(x, end = " ")