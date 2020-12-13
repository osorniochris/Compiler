#Equipo: Barajas Pérez Rafael Sahid, Osornio Sánchez Christopher, Sánchez Peña Axel
#Grupo: 3CM6

from Lexic import Lexic
class SyntaxGrammar: 
	def __init__(self, table, string):
		self.table = table
		self.strinG = strinG
		self.arregloListas = [] 
		self.simbTemp = []

	def ini(self):
		if G():
			token = Lexic.yylex()
			if token == FIN : 
				return True
		return False		

	def	G(self):
		if Reglas():
			return True
		return False
	
	def Reglas(self):
		if Regla():
			token = Lexic.yylex()
			if token == PYC:
				if Reglas_P():
					return True
		return False
		
	def Reglas_P(self):
		estado = Lexic.getEstado()
		if Regla():
			token = Lexic.yylex()
			if token == PYC:
				if Reglas_P():
					return True
			return False
		Lexic.setEstado(estado)	
	
	def Regla(self):
		if Lado_Izq():
			text = Lexic.yytext()
			token = Lexic.yylex()
			if token == FLECHA:
				if LadosDerechos(text):
					return True
		return False												

	def Lado_Izq(self):
		token = Lexic.yylex()
		if token == SIMB:
			return True
		return False
		
	def LadosDerechos(self, simbIzq):
		if Lado_Der(simbIzq):
			if LadosDerechos_p(simbIzq):
				return True
		return False					

	def LadosDerechos_p(self, simbIzq):
		token = Lexic.yylex()
		if token == OR:
			if Lado_Der(simbIzq):
				if LadosDerechos_p(simbIzq):
					return True
			return False
		
		Lexic.regresarToken()
		return True	
		
	def Lado_Der(self, simbIzq):
		self.simbTemp = []
		if ListaSimb():
			self.arregloListas.append([simbIzq, self.simbTemp])
			return True
		return False
		
	def ListaSimb(self):
		token = Lexic.yylex()
		if token == SIMB:
			self.simbTemp.append([Lexic.yytext(),False])
			if ListaSimb_p():
				return True
		return False
		
	def ListaSimb_p(self):
		token = Lexic.yylex()
		if token == SIMB:
			self.simbTemp.append([Lexic.yytext(),False])
			if ListaSimb_p():
				return True
			return False

		Lexic.regresarToken()
		return True	
		

		


