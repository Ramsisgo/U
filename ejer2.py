def validarCedula(x):
	#La funcion valida el número de ceula y da la provincia
	#separa la lista de numeros en posciones pares e impares
	#luego los valores de las posiciones impares las multiplica por 2 
	#suma ambas listas creadas y saca su modulo de 10 y si es 0 el resultado es 0 sino 10- resultado
	impar = []
	par   = []
	for i in range(0,len(x)-1,2):
		impar.insert(i, x[i])
	for i in range(0,len(impar)):
		n = impar[i]*2
		if n>9:
			n= n-9
			impar[i] = n
		else:
			impar[i] = n
	sumaimp = sum(impar)
	for i in range(1,len(x)-1,2):
		par.insert(i,x[i])
	sumapar = sum(par)
	total = sumapar+sumaimp
	modu = total%10
	if modu == 0:
		verficador = 0
	else:
		verificador = 10 - modu
		if verificador == x[9]:
			resVerif= "Válida"
		else:
			resVerif= "Inválida"
	if x[1]== 0 and x[0]==0:
		resProv = "Su cédula es inválida."
	else:
		n1 = x[0]
		n2 = x[1]
		prov = str(n1) + str(n2)
		prov = int(prov)
		provincias = ["Azuay", "Bolivar","Cañar","Carchi","Cotopaxi","Chimborazo","El Oro","Esmeraldas","Guayas","Imbabura","Loja","Los Rios", "Manabí","Morona Santiago","Napo","Pastaza","Pichincha","Tungurahua","Zamora Chinchipe", "Galápagos", "Sucumbíos","Orellana","Santo Domingo de los Tsáchilas","Santa Elena","Fuera del país"]
		if prov == 30:
			return provincias[24]
		if prov <0 or prov >24:
			resProv = "Su cédula es inválida"
		else:
			resProv = provincias[prov-1]
	return f"Su cédula es: {resVerif} \nSu Provincia es: {resProv}"
def generarFibonacci(n):
	#con "N" genera la cantidad de numeros de la serie fibonacci deseada
	lista = []
	a = 0
	b = 1
	for i2 in range(n):
		c = b + a
		a = b
		b = c
		lista.insert(i2, a)
	lista = f"Los primeros {n} números de Fibonacci son:\n{lista}"
	return lista
def calcularFactorial(num):
	#Con un numero ingresado calcula un factoral de manera que el 1 se multiplica hasta llegar
	#al número deseado
	r = 1
	if num ==0:
		b = "El factorial de 0 es  1"
		return b
	else:
		for i in range(1,num+1):
			r = r*i
		r = str(r)
		r = f"El factorial de {num} es {r}"
		return r
def ejecutarFuncion(opt):
	#Valida todo lo que las ocupen para funcionar correctamente y las llama
	if   opt == 1:
		inic3 = True
		print("Has seleccionado validación de cédula")
		while inic3 ==True:
			try:
				ced = []
				cedV2 =[]
				while not len(cedV2) == 10:
					ced= input("Ingrese su cédula: ")
					cedV1 = list(ced)
					for i in range(0, len(cedV1)):
						tfnum = int(cedV1[i])
						cedV2.insert(i, tfnum)
					if not len(cedV2) == 10:
						cedV2.clear()
					if len(cedV2) ==10:
						inic3= False
						print(validarCedula(cedV2))
			except ValueError:
				print("Solo se permiten números.")
	elif opt == 2:
		inic2 = True
		print("Has seleccionado calcular Fibonacci")
		while inic2 == True:
			try:
				n = int(input("Numeros de Fibonacci deseados: "))
				if n > 0:
					print(generarFibonacci(n))
					inic2 = False
				else:
					print("Ese no es un número válido.")
			except ValueError:
				print("Eso no es un número.")
	elif opt == 3:
		print("Ha selecionado calcular un Factorial")
		inic4 = True
		while inic4  == True:
			try: 
				num = int(input("Ingrese un número: "))
				if num< 0:
					print("Solo se permiten números positivos")
				else:
					print(calcularFactorial(num))
					inic4= False
			except ValueError:
				print("Solo se permiten números.")
inic1 = True
print(f"A continuación selecione una herramienta:\n1.- Validar un cédula\n2.- Generar números de Fibonacci\n3.- Calcular el factorial de un número")
while inic1 == True:
	try:
		opt = int(input("Ingrese una opción: "))
		if type(opt) is int:
			if (opt==1 or opt==2 or opt==3):
				inic1 = False
				ejecutarFuncion(opt)
			else:
				print("Esa no es una opción!")
	except ValueError:
		print("Esa no es una opción!")
