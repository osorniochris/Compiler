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
		current _state = self.table[0]
		flag_accept_state = False;
		#Si solo es una caracter no hace nada
		if(len(self.stringAn) <= 1):
			return 0
		
		n = 0
		m = 0
		acceptStates = { }
		acceptStatesN = 0
		#Recorrido de la cadena
		while n < len(self.stringAn):
			#si hay alguna transicion
			if table[m][self.stringAn[n]] != -1:
				#Se guarda el caracter en el lexema
				self.lexema.add(self.stringAn[n])
				#Se mueve al sigioente estado
				m = table[m][self.stringAn[n]]
				#se recorre la cadena
				n = n + 1
				#Si este es un estado de aceptacion
				if table[m][len(table[m])] != 0:
					#se guarda la posicion
					acceptStates.add(acceptStatesN)
					acceptStatesN = acceptStatesN + 1
					#Se activa la bandera
					flag_accept_state = True
				else 
					#Si no, se apaga la bandera
					flag_accept_state = False	
			
			else
				#Si no hay tranicion y no esta en edo de aceptacion 
				if flag_accept_state == False :
					#Si no se habia visitado se regresa al inicio
					current_state = self.table[0]
				else
					#Si si se habia visitado se regresa el token del edo y el lexema
					return table[m][len(table[m])]

	def yytext(self):
		return self.lexema				
