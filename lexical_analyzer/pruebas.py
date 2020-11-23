from SyntaxRE import SyntaxRE
import json

table = {}
with open(r"C:\Users\chistopher\OneDrive - Instituto Politecnico Nacional\SeptimoSemestre\Compiladores\Compiler\lexical_analyzer\afd13_table.json", 'r') as table_json:
    table = json.load(table_json)


syntax = SyntaxRE(table, "[a-z]")
ok, afn = syntax.ini()

print(ok)


