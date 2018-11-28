#Implentar calse Futbolista NOMBRE APELLIDO EQUIPO POSICION DORSAL,metodos set y get constructores toString y 3 objetos.
class Futbolista():

	def __init__(self):
		self.nombre = " "
		self.apellido = " "
		self.equipo = Equipo()
		self.posicion = " "
		self.dorsal = 0

	def set_nombre(self, n):
		self.nombre=n

	def get_nombre (self):
		return self.nombre

	def set_apellido(self, a):
		self.apellido = a

	def get_apellido(self):
		return self.apellido

	def set_equipo(self, e):
		self.equipo = e

	def get_equipo(self):
		return self.equipo

	def set_posicion(self, p):
		self.posicion = p

	def get_posicion(self):
		return self.posicion

	def set_dorsal(self, d):
		self.dorsal = d

	def get_dorsal(self):
		return self.dorsal

	def presentar_datos(self):
		c = "Nombre : %s \n Apellido : %s \n Posicion: %s \n Dorsal: %s \nEquipo: %s \n Pais: %s "%(self.nombre,self.apellido,self.posicion,self.get_dorsal(),self.equipo.get_nombreq(),self.equipo.get_pais())
		return c

class Equipo():

	def __init__(self):
		self.nombreq = " "
		self.pais = " "

	def set_nombreq(self, n):
		self.nombreq =n

	def get_nombreq(self):
		return self.nombreq

	def set_pais(self, p):
		self.pais = p

	def get_pais(self):
		return self.pais
