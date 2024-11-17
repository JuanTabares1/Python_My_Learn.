import random

print("Bienvenido a piedra, papel o tijera. Elije una de las opciones para jugar")
eleccion = int(input("1-papel  2-piedra  3-tijera"))

bot = random.randint(1,4)

if eleccion == 1 and bot == 1:
    print("Elegiste papel y empataste!!. El bot eligio papel")
elif eleccion == 2 and bot == 1:
    print("Elegiste piedra y perdiste. El bot eligio papel")
elif eleccion == 3 and bot ==1:
    print("Elegiste tijera y ganaste!!. El bot eligio papel")
elif eleccion == 1 and bot == 2:
    print("Elegiste papel y ganaste!!. El bot eligio piedra")
elif eleccion == 2 and bot == 2:
    print("Elegiste piedra y empataste. El bot eligio piedra")
elif eleccion == 3 and bot ==2:
    print("Elegiste tijera y perdiste!!. El bot eligio piedra")
elif eleccion == 1 and bot == 3:
    print("Elegiste papel y perdiste!!. El bot eligio tijera")
elif eleccion == 2 and bot == 3:
    print("Elegiste piedra y ganaste. El bot eligio tijera")
else:
    print("Elegiste tijera y empataste!!. El bot eligio tijera")
