from personal_academico.Docente import *
class Alumno():

	def __init__(self):
		self.nombrea = " "
		self.docente_matematica = Docente()
		self.docente_sociales = Docente()

	def set_nombrea(self, n):
		self.nombrea = n
	
	def get_nombrea(self):
		return self.nombrea

	def set_docente_matematica(self, d):
		self.docente_matematica = d

	def get_docente_matematica(self):
		return self.docente_matematica

	def set_docente_sociales(self, ds):
		self.docente_sociales = ds

	def get_docente_sociales(self):
		return self.docente_sociales

	def presentar_datos(self):	
		c = "Alumno\n Nombre: %s \n Docentes \n Docente Matematica \n Nombre: %s \nApellido : %s Titulo : %s \n Docente Sociales \nNombre : %s  \nApellido : %s Titulo : %s"%(self.nombrea, self.docente_matematica.get_nombre(),self.docente_matematica.get_apellido(), self.docente_matematica.get_titulo(),self.docente_sociales.get_nombre(),self.docente_sociales.get_apellido(),self.docente_sociales.get_titulo())
		return c