from SyntaxRE import SyntaxRE
import json
from Lexic import Lexic
from AFN import AFN
import FileTo2DArray as f2d

table = {}
list_of_afns = []
with open(r"RE_table.json", 'r') as table_json:
    table = json.load(table_json)

afns = f2d.fileTo2DArray(r"prueba1.txt")

id_ = 0

for a in afns:
    syntax = SyntaxRE(table, a[0], id_)
    ok, afn, id_ = syntax.ini()
    afn.set_token(int(a[1]))
    list_of_afns.append(afn)

    print(ok)

union = AFN.union_to_afd(list_of_afns, 100, 1)
union.show()
afd = union.to_afd(1)





