def Insercion(numeros): 
  tama = len(numeros) 
  i=0
  for i in range(tama):
    indice = numeros[i]
    a = i-1
    while (a >= 0 and numeros[a] > indice):
      numeros[a+1] = numeros[a]
      a = a-1
    numeros[a+1] = indice
  print numeros 