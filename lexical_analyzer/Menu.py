from AFN import AFN
from AFD import AFD

opc1 = 0
afns = []
afds = []
stateNum = 0

while opc1 != 10:

	print("")
	print("¿Qué le gustaría realizar?")
	print("   1. Crear un AFN básico")
	print("   2. Unir dos AFNs")
	print("   3. Concatenar dos AFNs")
	print("   4. Aplicar alguna cerradura a un AFN")
	print("   5. Aplicar el operador opcional a un AFN")
	print("   6. Unir AFNs para el analizador léxico")
	print("   7. Convertir un AFN a AFD")
	print("   8. Validar alguna cadena")
	print("   9. Ver algún autómata")
	print("")
	print("   10. Salir")

	opc1 = int(input())

	if opc1 == 1:
		afn = None

		print("Ingrese el caractér de transición")
		char = input()

		print("Ingrese un número para el identificador")
		ident = input()

		print("¿Tiene estado de aceptación?")
		print("   1. Sí")
		print("   2. No")
		opc2 = int(input())

		if opc2 == 1:
			print("¿Cuál sería el token del estado de aceptación?")
			token = input()

			#Crear un afn con los datos introducidos
			afn = AFN.create_basic(stateNum, ident, token, char)

		else:
			#Crear un afn con los datos introducidos
			afn = AFN.create_basic(stateNum, ident, 0, char)

		stateNum += 2

		#Agregarlo a la lista de los afn
		afns.append(afn)

		print("AFN creado")
		print("¿Le gustaría ver el AFN?")
		print("   1. Sí")
		print("   2. No")
		opc2 = int(input())
		
		if opc2 == 1:
			afn.show()


	elif opc1 == 2:
		if len(afns) != 0:
			union = None

			print("Seleccione el primer AFN a unir")
			#Mostrar lista de afns
			for i in range(0, len(afns)):
				print("   " + str(i + 1) + ". AFN ID: " + str(afns[i].id_))

			index1 = int(input()) - 1

			afn1 = afns[index1]
			afns.pop(index1)

			print("Seleccione el segundo AFN a unir")
			#Mostrar lista de afns
			for i in range(0, len(afns)):
				print("   " + str(i + 1) + ". AFN ID: " + str(afns[i].id_))

			index2 = int(input()) - 1

			afn2 = afns[index2]
			afns.pop(index2)

			print("Ingrese un número para el identificador del AFN resultante")
			ident = input()

			print("¿El estado final de esta unión es un estado de aceptación?")
			print("   1. Sí")
			print("   2. No")
			opc2 = int(input())

			if opc2 == 1:
				print("¿Cuál sería el token del estado de aceptación?")
				token = input()

				union = afn1.join_afn(afn2, stateNum, ident, token)

			else:
				union = afn1.join_afn(afn2, stateNum, ident, 0)


			stateNum += 2

			# agregar el afn resultante a la lista
			afns.append(union)

			print("AFNs unidos")
			print("¿Le gustaría ver el AFN?")
			print("   1. Sí")
			print("   2. No")
			opc2 = int(input())

			if opc2 == 1:
				union.show()

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 3:
		if len(afns) != 0:
			print("Seleccione el primer AFN a concatenar")
			#Mostrar lista de afns
			for i in range(0, len(afns)):
				print("   " + str(i + 1) + ". AFN ID: " + str(afns[i].id_))

			index1 = int(input()) - 1

			afn1 = afns[index1]
			afns.pop(index1)

			print("Seleccione el segundo AFN a concatenar")
			#Mostrar lista de afns
			for i in range(0, len(afns)):
				print("   " + str(i + 1) + ". AFN ID: " + str(afns[i].id_))

			index2 = int(input()) - 1

			afn2 = afns[index2]
			afns.pop(index2)

			print("Ingrese un número para el identificador del AFN resultante")
			ident = input()

			print("¿El estado final de esta concatenación es un estado de aceptación?")
			print("   1. Sí")
			print("   2. No")
			opc2 = int(input())

			if opc2 == 1:
				print("¿Cuál sería el token del estado de aceptación?")
				token = input()

				concat = afn1.concatenate_afn(afn2, ident, token)

			else:
				concat = afn1.concatenate_afn(afn2, ident, 0)

			# agregar el afn resultante a la lista
			afns.append(concat)

			print("AFNs concatenados")
			print("¿Le gustaría ver el AFN?")
			print("   1. Sí")
			print("   2. No")
			opc2 = int(input())

			if opc2 == 1:
				concat.show()

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 4:
		if len(afns) != 0:
			afn_cerr = None

			print("¿Qué cerradura le gustaría aplicar?")
			print("   1. Cerradura Transitiva")
			print("   2. Cerradura de Kleene")
			cerr = int(input())

			print("¿A qué AFN le gustaría aplicar la cerradura?")
			#mostrar la lista de afns
			for i in range(0, len(afns)):
				print("   " + str(i + 1) + ". AFN ID: " + str(afns[i].id_))

			index = int(input()) - 1

			afn = afns[index]
			afns.pop(index)

			print("Ingrese un número para el identificador del AFN resultante")
			ident = input()

			print("¿El estado final de esta concatenación es un estado de aceptación?")
			print("   1. Sí")
			print("   2. No")
			opc2 = int(input())

			if opc2 == 1:
				print("¿Cuál sería el token del estado de aceptación?")
				token = input()

				if cerr == 1:
					#aplicar cerradura transitiva
					afn_cerr = afn.kleene_plus(ident, stateNum, token)

				elif cerr == 2:
					#aplicar cerradura Kleene 
					afn_cerr = afn.kleene_star(ident, stateNum, token)

			else:
				if cerr == 1:
					#aplicar cerradura transitiva
					afn_cerr = afn.kleene_plus(ident, stateNum, 0)

				elif cerr == 2:
					#aplicar cerradura Kleene 
					afn_cerr = afn.kleene_star(ident, stateNum, 0)


			# agregar el afn resultante a la lista
			afns.append(afn_cerr)

			stateNum += 2

			print("Cerradura aplicada")
			print("¿Le gustaría ver el AFN?")
			print("   1. Sí")
			print("   2. No")
			opc2 = int(input())

			if opc2 == 1:
				afn_cerr.show()

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 5:
		if len(afns) != 0:
			afn_opc = None

			print("¿A qué AFN le gustaría aplicar el operador?")
			#mostrar la lista de afns
			for i in range(0, len(afns)):
				print("   " + str(i + 1) + ". AFN ID: " + str(afns[i].id_))

			index = int(input()) - 1

			afn = afns[index]
			afns.pop(index)

			print("Ingrese un número para el identificador del AFN resultante")
			ident = input()

			print("¿El estado final de esta concatenación es un estado de aceptación?")
			print("   1. Sí")
			print("   2. No")
			opc2 = int(input())

			if opc2 == 1:
				print("¿Cuál sería el token del estado de aceptación?")
				token = input()

				#aplicar el operador opcional
				afn_opc = afn.optional_operator(ident, stateNum, token)

			else:
				#aplicar el operador opcional
				afn_opc = afn.optional_operator(ident, stateNum, 0)

			# agregar el afn resultante a la lista
			afns.append(afn_opc)

			stateNum += 2

			print("Operador aplicado")
			print("¿Le gustaría ver el AFN?")
			print("   1. Sí")
			print("   2. No")
			opc2 = int(input())

			if opc2 == 1:
				afn_opc.show()

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 6:
		if len(afns) != 0:
			afnstojoin = []
			union = None

			print("Elija uno de los AFN para el analizador Léxico")
			#mostrar la lista de afns
			for i in range(0, len(afns)):
				print("   " + str(i + 1) + ". AFN ID: " + str(afns[i].id_))

			afn = int(input()) - 1
			afnstojoin.append(afns[afn])
			afns.pop(afn)

			while afn != len(afns) and len(afns) != 0:
				print("¿Cuál otro?")
				#mostrar la lista de afns
				for i in range(0, len(afns)):
					print("   " + str(i + 1) + ". AFN ID: " + str(afns[i].id_))

				print("   " + str(len(afns) + 1) + ". Ningún otro")

				afn = int(input()) - 1

				if afn != len(afns):
					afnstojoin.append(afns[afn])

			print("Ingrese un número para el identificador del AFN resultante")
			ident = input()

			#unir los afns
			union = AFN.union_to_afd(afnstojoin, stateNum, ident)

			# agregar el afn resultante a la lista
			afns.append(union)

			stateNum += 1

			print("AFNs unidos")
			print("¿Le gustaría ver el AFN resultante?")
			print("   1. Sí")
			print("   2. No")
			opc2 = int(input())

			if opc2 == 1:
				union.show()

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 7:
		if len(afns) != 0:
			print("¿Qué AFN le gustaría convertir?")
			#mostrar la lista de afns
			for i in range(0, len(afns)):
				print("   " + str(i + 1) + ". AFN ID: " + str(afns[i].id_))

			afn = int(input()) - 1

			print("Ingrese un número para el identificador del AFD resultante")
			ident = input()

			# convertir afn
			afd = afns[afn].to_afd(ident, stateNum)

			# agregar el afd resultante a la lista
			afds.append(afd)

			print("AFD creado")
			print("¿Le gustaría ver el AFD?")
			print("   1. Sí")
			print("   2. No")
			opc2 = int(input())

			if opc2 == 1:
				afd.show()

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 8:
		if len(afns) != 0:
			print("Introduzca la cadena que quiera validar:")
			cadena = input()

			print("¿Con qué autómata quieres validarla?")
			#mostrar la lista de afns
			for i in range(0, len(afns)):
				print("   " + str(i + 1) + ". AFN ID: " + str(afns[i].id_))

			for i in range(0, len(afds)):
				print("   " + str(i + 1 + len(afns)) + ". AFD ID: " + str(afds[i].id_))

			af = int(input()) - 1

			# validar cadena
			# dar veredicto de cadena
			validate = afns[af].check_string(cadena)
			print(validate)

		else:
			print("Lo siento, aún no hay ningún AFN para validar una cadena")

	elif opc1 == 9:
		if len(afns) != 0:
			print("¿Qué autómata quieres ver?")
			#mostrar la lista de afns y afds
			for i in range(0, len(afns)):
				print("   " + str(i + 1) + ". AFN ID: " + str(afns[i].id_))

			for i in range(0, len(afds)):
				print("   " + str(i + 1 + len(afns)) + ". AFD ID: " + str(afds[i].id_))

			af = int(input()) - 1

			#Mostrar el afn o afd
			if af < len(afns):
				afns[af].show()
			else:
				afds[af - len(afns)].show()

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 10:
		print("¡Hasta Luego!")

	else:
		print("Opción inválida")
