class Calculator:
    def add_number(self, first_number, second_number):
        result = first_number + second_number
        return result

calc = Calculator()
print(calc.add_number(1,4))