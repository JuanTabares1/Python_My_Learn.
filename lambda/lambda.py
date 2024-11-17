add = lambda a, b: a + b
print(add(10, 4))

multiply = lambda a, b: a * b
print(multiply(10, 4))

#Cuadrado de cada numero
numbers = range(0,11)
squared = list(map(lambda x: x**2, numbers))
print(squared)

#obtener numeros pares con filter
pairs = list(filter(lambda x: x%2 == 0, numbers))
print(pairs)