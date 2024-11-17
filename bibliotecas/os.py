import os  #os te permite utilizar los archivos del sistema desde python

#Obtener el directorio actual
"""cwd = os.getcwd() #cwd = current working directory
print(cwd)"""

#Listar los archivos txt
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print(f"Archivos .txt: {txt_files}")