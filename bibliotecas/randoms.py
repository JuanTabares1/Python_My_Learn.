import random

#Generar un numero entero aleatorio
random_number = random.randint(1,10)
print(random_number)

#Elegir colores aleatorios
colors = ['rojo', 'azul', 'verde']
random_color = random.choice(colors)
print(random_color)

#Barajar una lista de cartas
cards = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
random.shuffle(cards)
print(cards)