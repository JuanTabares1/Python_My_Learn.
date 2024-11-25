numbers = [1,2,3,4,5]

squares = []

for number in numbers:
    square = number ** 2
    squares.append(square)

print(squares)

#Programacion profesional y pythonista
squares = [x**2 for x in numbers] #Comprehension list
print(squares)