#Clase Lexic
class Lexic:
	#Constructor
	def _init_(self, id, table, stringAn):
		self.id = id
		self.table = table
		self.stringAn = stringAn
		self.lexema = ""
		self.inilexema = 0
		self.finlexema = 0

	#Funcion para validar cadena
	def yylex(self):
		flag_accept_state = False;
		#Si solo es una caracter no hace nada
		if(len(self.stringAn) <= 1):
			return 0
		
		m = self.inilexema
		acceptStates = { }
		acceptStatesN = 0
		#Recorrido de la cadena
		while self.finlexema < len(self.stringAn):
			#si hay alguna transicion
			if table[str(m)][self.stringAn[n]] != -1:
				#Se guarda el caracter en el lexema
				self.lexema.add(self.stringAn[n])
				#Se mueve al sigioente estado
				self.inilexema, m = table[str(m)][self.stringAn[n]]
				#se recorre la cadena
				self.finlexema = self.finlexema + 1
				#Si este es un estado de aceptacion
				if table[str(m)]["token"] != 0:
					#se guarda la posicion
					acceptStates.add(acceptStatesN)
					acceptStatesN = acceptStatesN + 1
					#Se activa la bandera
					flag_accept_state = True
				else 
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
