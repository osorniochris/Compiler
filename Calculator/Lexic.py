#Clase Lexic
class Lexic:
	#Constructor
	def __init__(self, table, stringAn):
		self.table = table
		self.stringAn = stringAn
		self.inilexema = 0
		self.finlexema = -1
		self.caracterActual = 0
		self.index = []
		self.currentState = 0
		self.flag_accept_state = False
		self.yytext = ""

	#Funcion para validar cadena
	def yylex(self):
		#Token auxiliar
		tokenAct = 0
		#se ubica el auxiliar en el estado actual
		self.currentState = 0
		self.flag_accept_state = False
		m = self.currentState
		self.index.append(self.caracterActual)
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
					self.finlexema = self.caracterActual - 1
					#Se cambia la bandera a True
					self.flag_accept_state = True
					#Se cambia el valor del token nuevo
					tokenAct = self.table[str(m)]["token"]
					
			else:
				#Si no hay tranicion y no esta en edo de aceptacion 
				if self.flag_accept_state:
					#Si si se habia visitado se regresa el token del edo y el lexema
					self.yytext = self.stringAn[self.inilexema:self.finlexema+1]
					if self.yytext.find("\\\\") != -1:
						self.yytext = self.yytext.replace("\\", "", 1)
					else:
						if self.yytext.find("\\") != -1:
							self.yytext = self.yytext.replace("\\", "")
					self.caracterActual = self.finlexema + 1
					self.inilexema = self.caracterActual
					self.finlexema = self.inilexema - 1
					print(tokenAct)
					return tokenAct	
				else:
					#Regresa error
					return -1
		self.yytext = self.stringAn[self.inilexema:self.finlexema+1]
		if self.yytext.find("\\\\") != -1:
			self.yytext = self.yytext.replace("\\", "", 1)
		else:
			if self.yytext.find("\\") != -1:
				self.yytext = self.yytext.replace("\\", "")
				
		print(tokenAct)
		return tokenAct

	#def yytext(self):
	#	return self.stringAn[self.inilexema:self.finlexema+1]
	
	def rewindToken(self):
		self.caracterActual = self.index.pop()
		self.inilexema = self.caracterActual
		self.finlexema = self.inilexema - 1
	
	def getState(self):
		return self.inilexema, self.finlexema, self.caracterActual, self.index, self.currentState, self.flag_accept_state, self.yytext

	def setState(self, state):
		self.inilexema, self.finlexema, self.caracterActual, self.index, self.currentState, self.flag_accept_state, self.yytext = state