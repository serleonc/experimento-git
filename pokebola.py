class Pokemon(object):
	def __init__(self, nombre, poder=10):
		self.nombre = nombre
		self.vida = 100
		self.poder = poder

	def sayName(self):
		print(self.nombre*2)

class Fuego(Pokemon):
	tipo = 'Fuego'
	
	def ataquePrincipal(self, objeto):
		objeto.vida -=10
		print(self.sayName(),'Puto')
		objeto.checkVida()

	def checkVida(self):
		if self.vida <=0:
			print('Ya vali .$.@#',self,sayName())
		else:
			print("hay te voy perro",self.sayName())