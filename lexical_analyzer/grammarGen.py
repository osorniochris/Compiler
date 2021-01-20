from SyntaxGrammar import SyntaxGrammar
import json
from Lexic import Lexic
from LL1 import LL1

def read_file(file_path):
    file = open(file_path, 'r')

    string = ""

    file_lines = file.readlines()

    for line in file_lines:
        string += line.replace('\n', '')

    return string

table = {}
#with open(r"C:\Users\chistopher\OneDrive - Instituto Politecnico Nacional\SeptimoSemestre\Compiladores\Compiler\lexical_analyzer\Grammar_table.json", 'r') as table_json:
with open(r"D:\Documents\Poli\7mo Semestre\Compiladores\Compiler\lexical_analyzer\Grammar_table.json", 'r') as table_json:
    table = json.load(table_json)

#gramatica = read_file(r"C:\Users\chistopher\OneDrive - Instituto Politecnico Nacional\SeptimoSemestre\Compiladores\Compiler\lexical_analyzer\grammarExample1.txt")
gramatica = read_file(r"D:\Documents\Poli\7mo Semestre\Compiladores\Compiler\lexical_analyzer\grammarExample1.txt")

syntax = SyntaxGrammar(table, gramatica)

ok = syntax.ini()
print(ok)

ll1 = LL1(syntax.arregloListas, syntax.simbNoTer)

for regla in ll1.arregloListas:
    print(regla)

print('--------')

print(' ', end='\t')
for y in ll1.table[' $']:
	print(y, end='\t')
print('')

for x in ll1.table:
	print(x, end='\t')
	for y in ll1.table[x]:
		print(ll1.table[x][y], end='\t')
	print('')