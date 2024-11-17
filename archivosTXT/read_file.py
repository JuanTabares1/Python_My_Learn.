#Leer un archivo linea por linea
"""with open('archivosTXT/caperucita.txt', 'r') as file:   #'r' es read para leer
    for lineas in file:
        print(lineas.strip())  #strip() elimina los saltos de linea"""

#Leer todas las lineas en una lista
"""with open('archivosTXT/caperucita.txt', 'r') as file:
    lineas = file.readlines()
    print(lineas)"""

#Agregar texto
""" with open('archivosTXT/caperucita.txt', 'a') as file:   #La letra a hace referencia a append()
    file.write("\n\nBY:ChatGpt") """

#Sobreescribir el texto
""" with open('archivosTXT/caperucita.txt', 'w') as file:   #w es para sobreescribir
    file.write("\n\nBY:ChatGpt") """