#Clase Lexic
class Lexic:
	#Constructor
	def _init_(self, id, table, stringAn):
		self.id = id
		self.table = table
		self.stringAn = stringAn
		self.lexema = ""

	#Funcion para validar cadena
	def yylex(self):
		current_state = self.table[0]
		flag_accept_state = False
		#Si solo es una caracter no hace nada
		if(len(self.stringAn) <= 1):
			return 0

		n = 0
		m = 0
		acceptStates = set()
		acceptStatesN = 0
		#Recorrido de la cadena
		while n < len(self.stringAn):
			#si hay alguna transicion
			if self.table[m][self.stringAn[n]] != -1:
				#Se guarda el caracter en el lexema
				self.lexema += self.stringAn[n]
				#Se mueve al sigioente estado
				m = self.table[m][self.stringAn[n]]
				#se recorre la cadena
				n = n + 1
				#Si este es un estado de aceptacion
				if self.table[m][len(self.table[m])] != 0:
					#se guarda la posicion
					acceptStates.add(acceptStatesN)
					acceptStatesN = acceptStatesN + 1
					#Se activa la bandera
					flag_accept_state = True
				else:
					#Si no, se apaga la bandera
					flag_accept_state = False	

			else:
				#Si no hay tranicion y no esta en edo de aceptacion 
				if flag_accept_state == False :
					#Si no se habia visitado se regresa al inicio
					current_state = self.table[0]
				else:
					#Si si se habia visitado se regresa el token del edo y el lexema
					return self.table[m][len(self.table[m])]

	def yytext(self):
		return self.lexema
