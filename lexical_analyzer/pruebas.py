from SyntaxRE import SyntaxRE
import json
from Lexic import Lexic
import FileTo2DArray as f2d

table = {}
with open(r"C:\Users\chistopher\OneDrive - Instituto Politecnico Nacional\SeptimoSemestre\Compiladores\Compiler\lexical_analyzer\afd13_table.json", 'r') as table_json:
    table = json.load(table_json)


"""syntax = SyntaxRE(table, "(a&b)?")
ok, afn = syntax.ini()
afn.set_token(10)

print(ok)

afn.show()
for s in afn.accept_states:
    print(s.token)"""

afns = f2d.fileTo2DArray(r"C:\Users\chistopher\OneDrive - Instituto Politecnico Nacional\SeptimoSemestre\Compiladores\Compiler\lexical_analyzer\archivo.txt")

for a in afns:
    syntax = SyntaxRE(table, a[0])
    ok, afn = syntax.ini()
    afn.set_token(int(a[1]))

    print(ok)

    afn.show()



