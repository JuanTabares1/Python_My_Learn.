try:
    divisor = int(input("Ingresa un numero divisor: "))
    result = 100 / divisor
    print(result)
except ZeroDivisionError as e:
    print("Error, numero divisor erroneo.")
    print("Error: ", e)
except ValueError as e:
    print("Error, debes digitar un numero valido")
    print("Error: ", e)