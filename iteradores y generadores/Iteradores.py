#Ejemplo de iterador

#Crear una lista
list = [1,2,3,4,5]

#Obtener iterador
iter = iter(list)

#Usar el iterador
#print(next(iter)) #La funcion nexte permite ver cuales valores se van guardando en memoria

for i in list:
    print(next(iter)) #bucle para imprimir los numeros porque print(next(iter)) solo imprime uno a la vez

