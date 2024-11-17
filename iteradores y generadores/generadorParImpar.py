#Generador numeros pares
print("Numeros pares")
def pares(limit):
    a=0
    while a < limit:
        yield a
        a = a + 2

for par in pares(11):
    print(par)

print("------------------------------------------------------")

print("Numeros impares")
def impares(limit):
    b = 1
    while b < limit:
        yield b
        b = b + 2

for impar in impares(11):
    print(impar)    