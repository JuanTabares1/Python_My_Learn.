square = [x**2 for x in range(1,11)]
#print('Cuadrados: ', square)

celsius = [0, 10, 20, 30, 40]
farenheit = [(temp * 9/5) * 32 for temp in celsius]
#print('Temperatura en F: ',farenheit)

evens = [x for x in range(1,20) if x%2 == 0]
#print(evens)

matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matriz] for i in range(len(matriz[0]))]
print(matriz)
print(transposed)

transposed = []
for i in range(len(matriz[0])):
    transposed_row = []
    for row in matriz:
        transposed_row.append(row[i]) #esto es igual a la linea 15, pero la linea 15 es mas optimzada
    transposed.append(transposed_row)
