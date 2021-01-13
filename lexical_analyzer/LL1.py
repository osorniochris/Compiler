class LL1:

	def __init__(self, arregloListas, simbNoTerm):
		self.arregloListas = arregloListas
		self.simbNoTerm = simbNoTerm
		self.arregloListas = self.validarNoTer()
		#for i in range(len(self.arregloListas)):
			#print(self.arregloListas[i])
		
	def validarNoTer(self):
		aux = self.arregloListas
		#print(self.simbNoTerm)
		for i in range(len(self.simbNoTerm)):
			for j in range(len(aux)):
				for k in range(len(aux[j][1])):
					if self.simbNoTerm[i] == ((aux[j][1])[k])[0]:
						((aux[j][1])[k])[1] = False
		return aux							

	def First(self, l):
		aux = l
		r = list()
		if aux[0][1] or aux[0][0] == "{' epsilon'}":
			r.append(str(aux[0][0]))
			return set(r)
			
		for i in range(len(self.arregloListas)):
			if str(aux[0][0]) == str(self.arregloListas[i][0]):
				r.append(str(self.First(self.arregloListas[i][1])))

		if "{' epsilon'}" in r and len(aux) != 1:
			r.remove("{' epsilon'}")
			r.append(str(self.First(aux[1])))
			return set(r)
				
		return set(r)		
