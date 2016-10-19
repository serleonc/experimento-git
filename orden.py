lista = list(map(int,input("dame una lista:").split(" ")))
print (lista)
def mayor(lista):
	aux = 0
	for numero in lista:
		if numero > aux:
			aux=numero
	return aux

may = mayor(lista)

def menor(lista):
	aux = lista[0]
	for numero in lista:
		if numero<aux:
			aux = numero
	return aux 

def suma(lista):
	aux = 0
	for numero in lista:
		aux += numero
	return aux

print("esta es la lista: ",lista)
print("El menor es: ",menor(lista))
print("El mayor es: ",mayor(lista))
print("La suma es: ",suma(lista))