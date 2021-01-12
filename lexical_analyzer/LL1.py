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
		r = []
		if l[0][1] or l[0][0] == 'epsilon':
			r.append(l[0][0])
			return r
			
		for i in range(len(l)):
			for j in range(len(self.arregloListas)):
				if str(l[i][0]) == str(self.arregloListas[j][0]):
					c = []
					c = self.First(self.arregloListas[j][1])
					if ' epsilon' in c and l[i+1] != None:
						c.remove(' epsilon')
						c.append(self.First(l[i+1]))
					r.append(c)
		return r		
