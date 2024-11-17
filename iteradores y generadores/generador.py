def generador():
    yield 1     #Los generadores se definen con la funcion yield
    yield 2     #Permite devolver un objeto generador en lugar de un valor, similar a return
    yield 3

for valor in generador():
    print(valor)