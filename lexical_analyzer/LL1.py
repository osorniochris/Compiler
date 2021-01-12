class LL1:


	def __init__(self, arregloListas, simbNoTerm):
		self.arregloListas = arregloListas
		self.simbNoTerm = simbNoTerm


	def First(self, l):
		print(l)
		r = set()
		aux = l
		if aux[0][1] or aux[0][0] == 'epsilon':
			r.add(aux[0][0])
			return r
		for i in range(len(aux)):
			if self.arregloListas[i][0] == aux[i][0]:
				c = First(arregloListas[i])
				if 'epsilon' in c and (i+1) < len(aux):
					c.remove('epsilon')
					c.union(First(aux[i+1]))
			r.union(c)		
		return r		
