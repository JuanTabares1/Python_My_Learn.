numbers = [1,2,3,4,5]

for i in numbers: #Bucle for
    print(i)

for i in range(4): #Bucle con rango, tambien hacerlo con (2,4) para elegir el rango
    print(i)

fruits = ["Manzana", "Pera", "Naranja", "Tomate", "Uva"]

for fruit in fruits: #Bucle con condicional
    print(fruit)
    if fruit == "Tomate":
        print("Fruta encontrada: ",fruit)

for i in numbers:   #continue reemplaza el valor que se va a imprimir por otra accion y continua el ciclo
    if i == 3:
        continue
    print("Aqui es igual a: ",i)