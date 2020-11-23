#Clase Lexic
class Lexic:
	#Constructor
	def __init__(self, table, stringAn):
		self.table = table
		self.stringAn = stringAn
		self.lexema = ""
		self.inilexema = 0
		self.finlexema = -1
		self.caracterActual = 0
		self.acceptStates = []
		self.acceptStatesN = 0
		self.currentState = 0

	#Funcion para validar cadena
	def yylex(self):
		#Se inicializa la bandera en Falso
		flag_accept_state = False
		#Si la cadena es solo 1 caracter
		if(len(self.stringAn) <= 1):
			#No regresa nada
			return 0
		#Token auxiliar
		tokenAct = 0
		#se ubica el auxiliar en el estado actual
		m = self.currentState
		#Recorrido de la cadena
		while self.caracterActual < len(self.stringAn):
			#si hay alguna transicion
			if self.table[str(m)][self.stringAn[self.caracterActual]] != -1:
				#Se mueve al sigioente estado
				m = self.table[str(m)][self.stringAn[self.caracterActual]]
				#Se cambia el current State al nuevo
				self.currentState = str(m)
				#se recorre la cadena
				self.caracterActual += 1
				#Si este es un estado de aceptacion
				if self.table[str(m)]["token"] != -1:
					#Se mueve el Lexema
					self.finlexema = self.finlexema + 1
					#Se cambia la bandera a True
					flag_accept_state = True
					#Se añade el estado de aceptacion al arreglo
					self.acceptStates.append(str(m))
					#Se añade uno a la cuenta de edos de acept
					self.acceptStatesN += 1		
					#Se cambia el valor del token nuevo
					tokenAct = self.table[str(m)]["token"]
				elif !flag_accept_state:
					#Si no ha pasado por edo de acept se cambia a falso
					flag_accept_state = False	
			else:
				#Si no hay tranicion y no esta en edo de aceptacion 
				if flag_accept_state:
					#Si si se habia visitado se regresa el token del edo y el lexema
					return tokenAct	
				else:
					#Regresa error
					return -1	

	def yytext(self):
		return self.stringAn[self.inilexema:self.finlexema]
