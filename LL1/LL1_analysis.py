import json
from Lexic import Lexic

tokens = {
	0 : " $",
	10 : " +",
	20 : " -",
	30 : " *",
	40 : " /",
	50 : " ^",
	60 : " (",
	70 : " )",
	80 : " sin",
	90 : " cos",
	100 : " tan",
	110 : " num",
	120 : " ln",
	130 : " log",
}

ll1_table = {}
with open(r"LL1_table.json", 'r') as table_json:
	ll1_table = json.load(table_json)

lexic_table = {}
with open(r"lexic_table.json", 'r') as table_json:
	lexic_table = json.load(table_json)

with open(r"cadenas.txt", 'r') as archivo:
	lines = archivo.readlines()

	tokens_values = []
	for item in list(tokens.items()):
		num, cadena = item
		tokens_values.append(cadena)
	tokens_values.append(' epsilon')

	for line in lines:
		line = line.replace('\n', '')

		lexic = Lexic(lexic_table, line)

		tokens_seq = []

		token = -1
		while token != 0:
			token = lexic.yylex()
			tokens_seq.append(token)

		pila = [" $"]
		pila.append(list(ll1_table.keys())[0])

		while len(tokens_seq) > 0:
			
			print("{}	{}".format(pila, tokens_seq))

			if pila[-1] not in tokens_values:
				action = ll1_table[pila[-1]][tokens[tokens_seq[0]]]
				
				action_list = action[0].split()

				pila.pop()
				action_list.reverse()

				for act in action_list:
					act = ' ' + act
					pila.append(act)
			else:
				if pila[-1] == tokens[tokens_seq[0]]:
					pila.pop()
					tokens_seq.pop(0)

				elif pila[-1] == ' epsilon': 
					pila.pop()

				else:
					print("Cadena Inválida.")
					break

		if len(pila) == 0:
			print('Cadena Válida!')


