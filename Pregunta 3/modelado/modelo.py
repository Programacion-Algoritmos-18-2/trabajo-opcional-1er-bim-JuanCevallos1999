class Garante(object):							
	def __init__(self):					
		self.nombre = " "
		self.apellido = " "
		self.sueldo = " "

	def set_nombre(self, n):							 
		self.nombre = n

	def set_apellido(self, a):
		self.apellido = a

	def set_sueldo(self, s):
		self.sueldo = s

	def get_nombre(self):							
		return self.nombre

	def get_apellido(self):
		return self.apellido

	def get_sueldo(self):
		return self.sueldo

	def presentar_datos(self):						
		c = "GARANTE:\nNombre: %s %s\nSueldo: %s"%(self.get_nombre(),self.get_apellido(),self.get_sueldo())
		return c

class Prestamo(object):							

	def __init__(self):			
		self.nombre_beneficiario = " "		
		self.sueldo = " "
		self.monto_prestamo = " "
		self.interes = " "
		self.tiempo = " "
		self.garante1 = Garante()

	def setnombre_beneficiario(self, nb):			
		self.nombreBeneficiario = nb
		
	def set_sueldo(self,s):
		self.sueldo = s

	def setmonto_prestamo(self, mp):
		self.montoPrestamo = mp

	def set_interes(self, i):
		self.interes = i

	def set_tiempo(self,t):
		self.tiempo = t

	def set_garante1(self,g1):
		self.garante1 = g1

	def get_nombre_beneficiario(self):		
		return self.nombreBeneficiario

	def get_sueldo(self):
		return	self.sueldo

	def get_monto_prestamos(self):
		return self.montoPrestamo

	def get_interes(self):
		return self.interes

	def get_tiempo(self):
		return self.tiempo

	def get_garante1(self):
		return self.garante1.presentar_datos()

	def presentar_datos(self):													
		c ="\nPrestamo\nBeneficiario: %s\nSueldo: %s\nMonto Prestamos: %s\nInteres: %s\nTiempo: %s\n%s"%(self.get_nombre_beneficiario(),self.get_sueldo(),self.get_monto_prestamos(),self.get_interes(),self.get_tiempo(),self.get_garante1())
		return c

class PrestamosAutomovil(Prestamo):									

	def __init__(self):						
		super(PrestamosAutomovil, self).__init__()			
		self.tipoVehiculo = " " 										
		self.marcaVehiculo = " "
		self.garante2 = Garante()

	def set_tipo_vehiculo(self, t):			
		self.tipoVehiculo= t

	def set_marca_vehiculo(self, mv):
		self.marcaVehiculo = mv

	def set_garante2(self, g2):
		self.garante2 = g2

	def get_tipo_vehiculo(self):				
		return self.tipoVehiculo

	def get_marca_vehiculo(self):
		return self.marcaVehiculo

	def get_garante2(self):
		return self.garante2.presentar_datos()

	def presentar_datos(self):				
		c = "\nPRESTAMO AUTOMOVIL\nBeneficiario: %s\nSueldo: %s\nMonto Prestamos: %s\nInteres: %s\nTiempo: %s\nTipo de Vehiculo: %s\nMarca Vehiculo: %s\n%s\n"%(self.get_nombre_beneficiario(),self.get_sueldo(),self.get_monto_prestamos(),self.get_interes(),self.get_tiempo(),self.get_tipo_vehiculo(),self.get_marca_vehiculo(),self.get_garante2())
		return c