
# -*- coding: utf-8 -*-
"""Created on Tue Oct 15 19:58:08 2019 \n@author: StevenE 186.117.181.74"""
print('------------------CONTADOR DE LÍNEAS DE CÓDIGO------------------')

def numLineasFichero(fichero): #Método para contar todas la líneas del archivo
 
    try:
        fichero.seek(0) #para que se ponga en posición o en el archivo
        return len(fichero.readlines())
    except AttributeError: 
        print("Debes insertar un fichero") #Imprimira esto si la ruta es incorrecta 
        return -1
 
fichero = open('C:\\Users\\StevenE\\Desktop\\2019-2\\PSP\\Calculadora.py', 'r') #ruta del archivo
 
print('Líneas de código =', numLineasFichero(fichero)) # Impresión de las líneas totales del archivo


class contadorLineas: #Método para contar métodos, líneas vacias, líneas de documentación, atributos y suma de métodos y atributos del archivo
    archivo = open('C:\\Users\\StevenE\\Desktop\\2019-2\\PSP\\Calculadora.py', "r") #ruta del archivo
    linea = archivo.readline() #Comando para leer el archivo línea por línea
    
    contadorLineasMetodos = 0
    contadorLineasVacias = 0
    contadorLineasDocumentación = 0
    líneasVacias = 0
    contadorAtributos = 0
    comparar = 0
    igual = 0
    sumaTotal = 0
    
    with open('C:\\Users\\StevenE\\Desktop\\2019-2\\PSP\\Calculadora.py') as Nombre: #insertamos la ruta, le damos un nombre al archivo
        for linea in Nombre:
            if linea.strip(): #Eliminamos las lienas vacias del archivo
                líneasVacias += 1

    print ('Número de lineas de código sin líneas vacias =', líneasVacias) #Imprimimos el numero de líneas de código, sin líneas vacias
    
    contadorLineasVacias = numLineasFichero(fichero) - líneasVacias # Calculamos el número de líneas vacias

    while linea:
        linea = archivo.readline()


        if linea.strip().startswith("def") or linea.strip().startswith('class'): # Hallamos los métodos del código, si la linea empieza con def o class
            contadorLineasMetodos = contadorLineasMetodos + 1


        if linea.strip().startswith('"""') or linea.strip().startswith('#'): # Hallamos las líneas de documentación del código, si la linea empieza con """ o #
            contadorLineasDocumentación = contadorLineasDocumentación + 1
            
            
        if '=' in linea:
            igual = igual + 1
            
        if '==' in linea:
            comparar = comparar + 1
            
        contadorAtributos = igual - comparar # Calculamos el número de atributos hallando un '=' en la línea y restando las comparaciones '=='

                
        contadorLineasEjecucción = numLineasFichero(fichero) - (contadorLineasVacias + contadorLineasDocumentación) # Hallamos el número de líneas de ejecucción, restandole al total de líneas, las líneas vacias y de documentación
        sumaTotal = contadorAtributos + contadorLineasMetodos
            
    print("Líneas Vacias =", contadorLineasVacias,
          "\nDocumentación =", contadorLineasDocumentación,
          "\nEjecucción =", contadorLineasEjecucción,
          "\nAtributos =", contadorAtributos,
          "\nMétodos =", contadorLineasMetodos,
          "\nSuma de métodos y atributos =", sumaTotal)
    archivo.close() # Cerramos el archivo