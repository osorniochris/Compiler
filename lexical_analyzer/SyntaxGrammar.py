from Lexic import Lexic
class SyntaxGrammar: 
	def __init__(self, table, string):
		self.table = table
		self.strinG = strinG 

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
		if Regla():
			token = Lexic.yylex()
			if token == PYC:
				if Reglas_P():
					return True
		return False
	
	def Regla(self):
		if Lado_Izq():
			token = Lexic.yylex()
			if token == FLECHA:
				if LadosDerechos():
					return True
		return False												

	def Lado_Izq(self):
		token = Lexic.yylex()
		if token == SIMB:
			return True
		return False
		
	def LadosDerechos(self):
		if Lado_Der():
			if LadosDerechos_p():
				return True
		return False					

	def LadosDerechos_p(self):
		token = Lexic.yylex()
		if token == OR:
			if Lado_Der():
				if LadosDerechos_p():
					return True
			return False
		
		Lexic.regresarToken()
		return True	
		
	def Lado_Der(self):
		if ListaSimb():
			return True
		return False
		
	def ListaSimb(self):
		token = Lexic.yylex()
		if token == SIMB:
			token_1 = Lexic.yylex()
			if token_1 == SPACE:
				if ListaSimb_p():
					return True
		return False
		
	def ListaSimb_p(self):
		token = Lexic.yylex()
		if token == SIMB:
			token_1 = Lexic.yylex()
			if token_1 == SPACE:
				if ListaSimb_p():
					return True
		return False
		

