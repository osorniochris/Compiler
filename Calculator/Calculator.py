from SyntaxCalculator import SyntaxCalculator
import json
from Lexic import Lexic

def get_table(filepath):
    table = {}
    with open(filepath, 'r') as table_json:
        table = json.load(table_json)
    
    return table

def check_operations_in_file(table, filepath):
    with open(filepath, 'r') as archivo:
        lines = archivo.readlines()

    for line in lines:
        syntax = SyntaxCalculator(table, line.replace('\n', ''))
        ok, result = syntax.ini()

        print(ok)
        print(line.replace('\n', '') + " = " + str(result))


table =  get_table(r"calc_table.json")
check_operations_in_file(table, r"operaciones.txt")
