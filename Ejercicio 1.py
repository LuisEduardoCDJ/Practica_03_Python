#1Crear un programa que pida números positivos al usuario, y vaya calculandola suma de todos ellos (terminará cuando se teclea un número negativo o cero).
numpositivo = int(input('Ingrese un numero '))
arreglo = []
arreglo.append(numpositivo)
while numpositivo > 0 :
  numpositivo = int(input('Ingrese un numero a sumar'))
  arreglo.append(numpositivo)


if numpositivo <= 0:
  print(arreglo)
  print(sum(arreglo))