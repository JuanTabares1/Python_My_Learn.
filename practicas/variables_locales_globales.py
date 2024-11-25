def local_function():
    x = 10 #Variable local
    print(f"El valor de la variable local es: {x}")

y = 10 #Variable global
print(f"El valor de la variable global es: {y}")
local_function()