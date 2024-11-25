class Employee:
    name: str
    age: int
    salary: float

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def introduce(self) -> str:
        return f"Hola soy {self.name} y tengo {self.age}"
    
employee = Employee('juan', 18, 3500.00)
print(employee.introduce())