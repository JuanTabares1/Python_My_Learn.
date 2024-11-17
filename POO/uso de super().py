class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello!! I'm a person")

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        print(f"Hello, my student id is {self.student_id}")

student1 = Student("Juan", 18, "S123")
student1.greet()