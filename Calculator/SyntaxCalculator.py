import math
from Lexic import Lexic

class TokensCalc:
    #clases léxicas
    FIN = 0
    MAS = 10
    MENOS = 20
    POR = 30
    DIV = 40
    POT = 50
    PAR_I = 60
    PAR_D = 70
    SIN = 80
    COS = 90
    TAN = 100
    LN = 110
    LOG = 120
    NUM = 130

class SyntaxCalculator:
    def __init__(self, table, string):
        self.lexic = Lexic(table, string)
    
    def ini(self):
        v = 0
        boolean, v = self.E(v)
        if boolean:
            token = self.lexic.yylex()
            if token == TokensCalc.FIN:
                return True, v
        return False, v
    
    def E(self, v):
        boolean, v = self.T(v)

        if boolean:
            boolean, v = self.Ep(v)
            if boolean:
                return True, v
        return False, v
    
    def Ep(self, v):
        w = 0
        token = self.lexic.yylex()

        if token == TokensCalc.MAS:
            boolean, w = self.T(w)

            if boolean:
                v = v + w
                boolean = self.Ep(v)
                if boolean:
                    return True, v
            return False, v
        elif token == TokensCalc.MENOS:
            boolean, w = self.T(w)

            if boolean:
                v = v - w
                boolean = self.Ep(v)
                if boolean:
                    return True, v
            return False, v
        
        self.lexic.rewindToken()
        return True, v
    
    def T(self, v):
        boolean, v = self.P(v)

        if boolean:
            boolean, v = self.Tp(v)
            if boolean:
                return True, v
        return False, v
    
    def Tp(self, v):
        w = 0
        token = self.lexic.yylex()

        if token == TokensCalc.POR:
            boolean, w = self.P(w)

            if boolean:
                v = v * w
                boolean, v = self.Tp(v)
                if boolean:
                    return True, v
            return False, v
        elif token == TokensCalc.DIV:
            boolean, w = self.P(w)

            if boolean:
                v = v / w
                boolean, v = self.Tp(v)
                if boolean:
                    return True, v
            return False, v
        
        self.lexic.rewindToken()
        return True, v
    
    def P(self, v):
        boolean, v = self.F(v)

        if boolean:
            boolean, v = self.Pp(v)
            if boolean:
                return True, v
        return False, v

    def Pp(self, v):
        w = 0
        token = self.lexic.yylex()

        if token == TokensCalc.POT:
            boolean, w = self.F(w)

            if boolean:
                v = v ** w
                boolean, v = self.Pp(v)
                if boolean:
                    return True, v
            return False, v
        
        self.lexic.rewindToken()
        return True, v
    
    def F(self, v):
        lexem_1 = ""
        token = self.lexic.yylex()

        if token == TokensCalc.PAR_I:
            boolean, v = self.E(v)
            if boolean:
                token_1 = self.lexic.yylex()
                if token_1 == TokensCalc.PAR_D:
                    return True, v
            return False, v
        elif token == TokensCalc.SIN:
            token_1 = self.lexic.yylex()
            if token_1 == TokensCalc.PAR_I:
                boolean, v = self.E(v)
                if boolean:
                    token_1 = self.lexic.yylex()
                    if token_1 == TokensCalc.PAR_D:
                        v = math.sin(v)
                        return True, v
                return False, v
        elif token == TokensCalc.COS:
            token_1 = self.lexic.yylex()
            if token_1 == TokensCalc.PAR_I:
                boolean, v = self.E(v)
                if boolean:
                    token_1 = self.lexic.yylex()
                    if token_1 == TokensCalc.PAR_D:
                        v = math.cos(v)
                        return True, v
                return False, v
        elif token == TokensCalc.TAN:
            token_1 = self.lexic.yylex()
            if token_1 == TokensCalc.PAR_I:
                boolean, v = self.E(v)
                if boolean:
                    token_1 = self.lexic.yylex()
                    if token_1 == TokensCalc.PAR_D:
                        v = math.tan(v)
                        return True, v
                return False, v
        elif token == TokensCalc.LN:
            token_1 = self.lexic.yylex()
            if token_1 == TokensCalc.PAR_I:
                boolean, v = self.E(v)
                if boolean:
                    token_1 = self.lexic.yylex()
                    if token_1 == TokensCalc.PAR_D:
                        v = math.log(v)
                        return True, v
                return False, v
        elif token == TokensCalc.LOG:
            token_1 = self.lexic.yylex()
            if token_1 == TokensCalc.PAR_I:
                boolean, v = self.E(v)
                if boolean:
                    token_1 = self.lexic.yylex()
                    if token_1 == TokensCalc.PAR_D:
                        v = math.log(v, 10)
                        return True, v
                return False, v
        elif token == TokensCalc.NUM:
            num = float(self.lexic.yytext)
            return True, num
        
        return False, v
