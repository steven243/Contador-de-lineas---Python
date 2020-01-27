#tiempo de escritura de código --> "1hora(s)"

#Funcion que recibe una letra para analizarla
def getLetra(letra):
	"""
	Esta función recibe una letra y se confirma si está dentro de una lista \n de vocales, en cada caso, retorna un mensaje.
	"""
	if letra in ["a","e","i","o","u"]:

		return "¡Es una letra!"

	else:
		return "¡No es una letra!"


letra = str(input("Escriba una letra:"))
func = getLetra(letra)

print(func)
