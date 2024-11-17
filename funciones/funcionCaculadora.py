def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calcular():
    while True:
        print("Elije una opcion:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")   

        res = int(input("Opcion: "))

        if res == 5:
            print("Saliendo...")
            break

        if res in [1,2,3,4]:
            a = float("Ingrese el numero 1: ")
            b = float("Ingrese el numero 2: ")

            if res == 1:
                print("La suma es: ",suma(a, b))
            elif res == 2:
                print("La resta es: ",resta(a, b))
            elif res == 3:
                print("La multiplicacion es: ",multiplicar(a, b))
            elif res == 4:
                print("La division es: ",dividir(a, b))

        else:
            print("Opcion no valida")

calcular()