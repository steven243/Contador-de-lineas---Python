# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

def numLineasFichero(fichero):
 
    try:
        fichero.seek(0)
        return len(fichero.readlines())
    except AttributeError:
        print("Debes insertar un fichero")
        return -1
 
fichero = open('C:\\Users\\StevenE\\Desktop\\2019-2\\PSP\\Calculadora.py', 'r')
 
print('Lineas de código =', numLineasFichero(fichero))
 
fichero.close()

Lineas_vacias = 0

with open('C:\\Users\\StevenE\\Desktop\\2019-2\\PSP\\Calculadora.py') as Va:
    for line in Va:
       if line.strip():
          Lineas_vacias =+ 1

print ('lineas vacias o muertas =', Lineas_vacias)

"""def numLineasFicheroRuta(ruta):
    numLineas = -1
    try:
        fichero = open(ruta, 'r')
        numLineas = len(fichero.readlines())
        fichero.close()
    except AttributeError:
        print("Debes insertar un fichero")
    except FileNotFoundError:
        print("la ruta no es correcta")
    return numLineas
 
 
print(numLineasFichero('datos')) #Si la ruta no es correcta, da error"""