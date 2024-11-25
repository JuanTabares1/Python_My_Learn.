def add(n1: float, n2: float) -> float:
    return n1 + n2

def deduct(n1: float, n2: float) -> float:
    return n1 - n2

def multiply(n1: float, n2: float) -> float:
    return n1 * n2

def divide(n1: float, n2: float) -> float:
    if n2 == 0:
        raise ValueError('No se puede dividir entre 0')
    return n1 / n2

if __name__ == "__main__":
    print('Operaciones')
    res_1 = add(3,4)
    print(f'Suma: {res_1}')
    res_2 = divide(10,7)
    print(f'Division: {res_2}')