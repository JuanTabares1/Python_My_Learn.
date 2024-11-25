def divide(a: int, b: int) -> float:
    #Validar que ambos parametros sean enteros
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError('Ambos parametros deben ser enteros.')
    
    if a == 0 or b == 0:
        raise TypeError('El divisor no puede ser cero')
    
    return a/b

#Ejemplo
try:
    res = divide(10, '2') #Error de tipo
    print(res)
except ValueError as e:
    print(f'Error: {e}')