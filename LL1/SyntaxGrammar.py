from Lexic import Lexic

class Tokens:
	#clases léxicas
	FIN = 0
	PYC = 10 
	FLECHA = 20 
	SIMB = 30
	OR = 40
	
class SyntaxGrammar: 

	def __init__(self, table, string):
		self.lexic = Lexic(table, string)
		self.arregloListas = [] 
		self.simbTemp = []
		self.simbNoTer = []

	def ini(self):
		if self.G():
			token = self.lexic.yylex()
			if token == Tokens.FIN : 
				return True
		return False, None		

	def	G(self):
		if self.Reglas():
			return True
		return False
	
	def Reglas(self):
		if self.Regla():
			token = self.lexic.yylex()
			if token == Tokens.PYC:
				if self.Reglas_P():
					return True
		return False
		
	def Reglas_P(self):
		state = self.lexic.getState()
		if self.Regla():
			token = self.lexic.yylex()
			if token == Tokens.PYC:
				if self.Reglas_P():
					return True
			return False
		self.lexic.setState(state)	
		return True
	
	def Regla(self):
		if self.Lado_Izq():
			text = self.lexic.yytext
			token = self.lexic.yylex()
			if token == Tokens.FLECHA:
				if self.LadosDerechos(text):
					return True
		return False												

	def Lado_Izq(self):
		token = self.lexic.yylex()
		if token == Tokens.SIMB:
			return True
		return False
		
	def LadosDerechos(self, simbIzq):
		if self.Lado_Der(simbIzq):
			if self.LadosDerechos_p(simbIzq):
				return True
		return False					

	def LadosDerechos_p(self, simbIzq):
		token = self.lexic.yylex()
		if token == Tokens.OR:
			if self.Lado_Der(simbIzq):
				if self.LadosDerechos_p(simbIzq):
					return True
			return False
		
		self.lexic.rewindToken()
		return True	
		
	def Lado_Der(self, simbIzq):
		self.simbTemp = []
		if self.ListaSimb():
			if simbIzq not in self.simbNoTer:
				self.simbNoTer.append(simbIzq)
			self.arregloListas.append([simbIzq, self.simbTemp])
			return True
		return False
		
	def ListaSimb(self):
		token = self.lexic.yylex()
		if token == Tokens.SIMB:
			self.simbTemp.append([self.lexic.yytext, True])
			if self.ListaSimb_p():
				return True
		return False
		
	def ListaSimb_p(self):
		token = self.lexic.yylex()
		if token == Tokens.SIMB:
			self.simbTemp.append([self.lexic.yytext, True])
			if self.ListaSimb_p():
				return True
			return False

		self.lexic.rewindToken()
		return True	
		

		


