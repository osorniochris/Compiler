#Clase Lexic
class Lexic:
	#Constructor
	def __init__(self, table, stringAn):
		self.table = table
		self.stringAn = stringAn
		self.lexema = ""
		self.inilexema = 0
		self.finlexema = 0

	#Funcion para validar cadena
	def yylex(self):
		flag_accept_state = False
		#Si solo es una caracter no hace nada
		if(len(self.stringAn) <= 1):
			return 0
		
		m = self.inilexema
		acceptStates = []
		acceptStatesN = 0
		#Recorrido de la cadena
		while self.finlexema < len(self.stringAn):
			#si hay alguna transicion
			if self.table[str(m)][self.stringAn[self.finlexema]] != -1:
				#Se guarda el caracter en el lexema
				self.lexema += self.stringAn[self.finlexema]
				#Se mueve al sigioente estado
				self.inilexema = self.table[str(m)][self.stringAn[self.finlexema]]
				m = self.inilexema
				#se recorre la cadena
				self.finlexema = self.finlexema + 1
				#Si este es un estado de aceptacion
				if self.table[str(m)]["token"] != -1:
					#se guarda la posicion
					acceptStates.append(acceptStatesN)
					acceptStatesN = acceptStatesN + 1
					#Se activa la bandera
					flag_accept_state = True
				else:
					#Si no, se apaga la bandera
					flag_accept_state = False	
			
		
			else:
				#Si no hay tranicion y no esta en edo de aceptacion 
				if flag_accept_state:
					#Si si se habia visitado se regresa el token del edo y el lexema
					return self.table[str(m)]["token"]
					

	def yytext(self):
		return self.lexema