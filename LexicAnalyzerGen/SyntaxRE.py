from AFN import AFN
from Lexic import Lexic

class SyntaxRE:

    numAutomata = 0
    
    #clases léxicas
    FIN = 0
    OR = 10
    CONC = 20
    CERR_POS = 30
    CERR_KLEEN = 40
    OPC = 50
    PAR_I = 60
    PAR_D = 70
    COR_I = 80
    COR_D = 90
    GUION = 100
    SIMB = 110

    def __init__(self, table, string, numEdo):
        self.lexic = Lexic(table, string)
        self.numEdo = numEdo

    def ini(self):
        afn = None

        boolean, afn = self.E(afn)
        if boolean:
            token = self.lexic.yylex()
            if token == self.FIN:
                return True, afn, self.numEdo
        return False, afn

    #E -> TE'
    def E(self, afn):
        boolean, afn = self.T(afn)
        if boolean:
            boolean, afn = self.Ep(afn)
            if boolean:
                return True, afn
        return False, afn
    
    #E' -> orTE' | epsilon
    def Ep(self, afn):
        token = self.lexic.yylex()

        if token == self.OR:
            afn_2 = None
            boolean, afn_2 = self.T(afn_2)
            if boolean:
                afn = afn.join_afn(afn_2, self.numEdo, self.numAutomata, -1)
                self.numEdo += 2
                self.numAutomata += 1
                boolean, afn = self.Ep(afn)
                if boolean:
                    return True, afn
            return False, afn
        
        self.lexic.rewindToken()
        return True, afn
    
    #T -> CT'
    def T(self, afn):
        boolean, afn = self.C(afn)
        if boolean:
            boolean, afn = self.Tp(afn)
            if boolean:
                return True, afn
        return False, afn

    #T' -> &CT' | epsilon
    def Tp(self, afn):
        token = self.lexic.yylex()

        if token == self.CONC:
            afn_2 = None
            boolean, afn_2 = self.C(afn_2)
            if boolean:
                afn = afn.concatenate_afn(afn_2, self.numAutomata, -1)
                self.numAutomata += 1
                boolean, afn = self.Tp(afn)
                if boolean:
                    return True, afn
            return False, afn
        
        self.lexic.rewindToken()
        return True, afn
    
    #C -> FC'
    def C(self, afn):
        boolean, afn = self.F(afn)
        if boolean:
            boolean, afn = self.Cp(afn)
            if boolean:
                return True, afn
        return False, afn

    #C' -> +C' | *C' | ?C' | epsilon
    def Cp(self, afn):
        token = self.lexic.yylex()

        if token == self.CERR_POS:
            afn = afn.kleene_plus(self.numAutomata, self.numEdo, -1)
            self.numEdo += 2
            self.numAutomata += 1
            boolean, afn = self.Cp(afn)
            if boolean:
                return True, afn
            return False, afn
        elif token == self.CERR_KLEEN:
            afn = afn.kleene_star(self.numAutomata, self.numEdo, -1)
            self.numEdo += 2
            self.numAutomata += 1
            boolean, afn = self.Cp(afn)
            if boolean:
                return True, afn
            return False, afn
        elif token == self.OPC:
            afn = afn.optional_operator(self.numAutomata, self.numEdo, -1)
            self.numEdo += 2
            self.numAutomata += 1
            boolean, afn = self.Cp(afn)
            if boolean:
                return True, afn
            return False, afn
        
        self.lexic.rewindToken()
        return True, afn

    #F -> (E) | [SIMB-SIMB] | SIMB
    def F(self, afn):
        lexem_1 = ""
        lexem_2 = ""
        token = self.lexic.yylex()

        if token == self.PAR_I:
            boolean, afn = self.E(afn)
            if boolean:
                token_1 = self.lexic.yylex()
                if token_1 == self.PAR_D:
                    return True, afn
            return False, afn
        elif token == self.COR_I:
            token_1 = self.lexic.yylex()
            if token_1 == self.SIMB:
                lexem_1 = self.lexic.yytext
                token_1 = self.lexic.yylex()
                if token_1 == self.GUION:
                    token_1 = self.lexic.yylex()
                    if token_1 == self.SIMB:
                        lexem_2 = self.lexic.yytext
                        token_1 = self.lexic.yylex()
                        if token_1 == self.COR_D:
                            char_1 = lexem_1[0]
                            char_2 = lexem_2[0]
                            afn = AFN.create_basic(self.numEdo, self.numAutomata, -1, char_1, char_2)
                            self.numEdo += 2
                            self.numAutomata += 1
                            return True, afn
            return False, afn
        elif token == self.SIMB:
            char_1 = self.lexic.yytext[0]
            afn = AFN.create_basic(self.numEdo, self.numAutomata, -1, char_1, char_1)
            self.numEdo += 2
            self.numAutomata += 1
            return True, afn
        
        return False, afn

