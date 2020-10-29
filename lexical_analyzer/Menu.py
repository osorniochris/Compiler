


opc1 = 0
afns = []
afds = []

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

	opc1 = input()

	if opc1 == 1:
		print("Ingrese el caractér de transición")
		char = input()

		print("Ingrese un número para el identificador")
		ident = input()

		#Crear un afn con los datos introducidos
		#Agregarlo a la lista de los afn

		print("AFN creado")
		print("¿Le gustaría ver el AFN?")
		print("   1. Sí")
		print("   2. No")
		opc2 = input()
		
		if opc2 == 1:
			#Mostrar el afn


	elif opc1 == 2:
		if len(afns) != 0:
			print("Seleccione el primer AFN a unir")
			#Mostrar lista de afns
			afn1 = input()

			print("Seleccione el segundo AFN a unir")
			#Mostrar lista de afns
			afn2 = input()

			# unirlos
			# agregar el afn resultante a la lista

			print("AFNs unidos")
			print("¿Le gustaría ver el AFN?")
			print("   1. Sí")
			print("   2. No")
			opc2 = input()

			if opc2 == 1:
				#Mostrar el afn

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 3:
		if len(afns) != 0:
			print("Seleccione el primer AFN a concatenar")
			#Mostrar lista de afns
			afn1 = input()

			print("Seleccione el segundo AFN a concatenar")
			#Mostrar lista de afns
			afn2 = input()

			# concatenarlos
			# agregar el afn resultante a la lista

			print("AFNs concatenados")
			print("¿Le gustaría ver el AFN?")
			print("   1. Sí")
			print("   2. No")
			opc2 = input()

			if opc2 == 1:
				#Mostrar el afn

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 4:
		if len(afns) != 0:
			print("¿Qué cerradura le gustaría aplicar?")
			print("   1. Cerradura Transitiva")
			print("   2. Cerradura de Kleene")
			cerr = input()

			print("¿A qué AFN le gustaría aplicar la cerradura?")
			#mostrar la lista de afns
			afn = input()

			if cerr == 1:
				#aplicar cerradura transitiva
				# agregar el afn resultante a la lista
			elif cerr == 2:
				#aplicar cerradura Kleene 
				# agregar el afn resultante a la lista

			print("Cerradura aplicada")
			print("¿Le gustaría ver el AFN?")
			print("   1. Sí")
			print("   2. No")
			opc2 = input()

			if opc2 == 1:
				#Mostrar el afn

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 5:
		if len(afns) != 0:
			print("¿A qué AFN le gustaría aplicar el operador?")
			#mostrar la lista de afns
			afn = input()

			#aplicar el operador opcional
			# agregar el afn resultante a la lista

			print("Cerradura aplicada")
			print("¿Le gustaría ver el AFN?")
			print("   1. Sí")
			print("   2. No")
			opc2 = input()

			if opc2 == 1:
				#Mostrar el afn

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 6:
		if len(afns) != 0:
			afnstojoin = []

			print("Elija uno de los AFN para el analizador Léxico")
			#mostrar la lista de afns
			afn = input()
			afnstojoin.add(afn)

			while afn != len(afns):
				print("¿Cuál otro?")
				#mostrar la lista de afns
				print("   " + str(len(afns)) + ". Ningún otro")

				afn = input()
				afnstojoin.add(afn)

			#unir los afns
			# agregar el afn resultante a la lista

			print("AFNs unidos")
			print("¿Le gustaría ver el AFN resultante?")
			print("   1. Sí")
			print("   2. No")
			opc2 = input()

			if opc2 == 1:
				#Mostrar el afn

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 7:
		if len(afns) != 0:
			print("¿Qué AFN le gustaría convertir?")
			#mostrar la lista de afns
			afn = input()

			# convertir afn
			# agregar el afd resultante a la lista

			print("AFD creado")
			print("¿Le gustaría ver el AFD?")
			print("   1. Sí")
			print("   2. No")
			opc2 = input()

			if opc2 == 1:
				#Mostrar el afn

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 8:
		if len(afns) != 0:
			print("Introduzca la cadena que quiera validar:")
			#mostrar la lista de afns
			cadena = input()

			print("¿Con qué autómata quieres validarla?")
			#mostrar la lista de afns y afds

			# validar cadena
			# dar veredicto de cadena


			print("AFD creado")
			print("¿Le gustaría ver el AFD?")
			print("   1. Sí")
			print("   2. No")
			opc2 = input()

			if opc2 == 1:
				#Mostrar el afn

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 9:
		if len(afns) != 0:
			print("¿Qué autómata quieres ver?")
			#mostrar la lista de afns y afds

			#Mostrar el afn

		else:
			print("Lo siento, aún no hay ningún AFN")

	elif opc1 == 10:
		print("¡Hasta Luego!")

	else:
		print("Opción inválida")
