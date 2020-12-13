from SyntaxGrammar import SyntaxGrammar
import json
from Lexic import Lexic

def read_file(file_path):
    file = open(file_path, 'r')

    string = ""

    file_lines = file.readlines()

    for line in file_lines:
        string += line.replace('\n', '')

    return string

table = {}
with open(r"C:\Users\chistopher\OneDrive - Instituto Politecnico Nacional\SeptimoSemestre\Compiladores\Compiler\lexical_analyzer\Grammar_table.json", 'r') as table_json:
    table = json.load(table_json)

gramatica = read_file(r"C:\Users\chistopher\OneDrive - Instituto Politecnico Nacional\SeptimoSemestre\Compiladores\Compiler\lexical_analyzer\grammarExample1.txt")

syntax = SyntaxGrammar(table, gramatica)

ok = syntax.ini()

print(ok)
print("Símbolos no terminales")
for simb in syntax.simbNoTer:
    print(simb)
print('\nArreglo de Listas')
for regla in syntax.arregloListas:
    print(regla)