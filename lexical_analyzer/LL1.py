class LL1:

	def __init__(self, arregloListas, simbNoTerm):
		self.arregloListas = arregloListas
		self.simbNoTerm = simbNoTerm
		self.arregloListas = self.validarNoTer()
		
	def validarNoTer(self):
		aux = self.arregloListas
		for i in self.simbNoTerm:
			for j in range(len(aux)):
				for k in range(len(aux[j][1])):
					if i == ((aux[j][1])[k])[0]:
						((aux[j][1])[k])[1] = False
		return aux							

	def First(self, l):
		aux = l
		r = set()
		if aux[0][1] or aux[0][0] == ' epsilon':
			r.add(aux[0][0])	
			return set(r)	
		
		for i in range(len(self.arregloListas)):
			if str(aux[0][0]) == str(self.arregloListas[i][0]):
				if str(aux[0][0]) == str(self.arregloListas[i][1][0]):
					continue
				r.update(self.First(self.arregloListas[i][1]))
				
		if ' epsilon' in r and len(aux) != 1:
			r.remove(' epsilon')
			r.update(self.First(aux[1:]))
			return set(r)
				
		return r	

	def Follow(self, string):
		r = set()

		#si string es el símbolo inicial de la gramática
		if string == str(self.arregloListas[0][0]): 
			r.add(" $")
		
		for i in range(len(self.arregloListas)):
			n = self.find_symbol(string, i) # se busca el símbolo del lado derecho

			if len(n) == 0: #no se encontró en la regla i
				continue
			if len(n) == 1: #ya no hay símbolos delante 
				if string == str(self.arregloListas[i][0]): 
					#evitar ciclos cuando string = lado izquierdo de la regla
					continue
				r.update(self.Follow(self.arregloListas[i][0]))
			else:
				aux_first = self.First(n[1:])
				if ' epsilon' in aux_first:
					aux_first.remove(' epsilon')
					r.update(aux_first)

					if string != str(self.arregloListas[i][0]):
						r.update(self.Follow(str(self.arregloListas[i][0])))
				else:
					r.update(aux_first)
			
		return r
	
	def find_symbol(self, string, i):
		aux = []
		for j in range(len(self.arregloListas[i][1])):
			if str(self.arregloListas[i][1][j][0]) == string:
				aux = self.arregloListas[i][1][j:]
		
		return aux

