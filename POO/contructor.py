class Person:
    def __init__(self, name, age):     #self para que se llame a si mismo, Esto es un constructor
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola mi nombre es {self.name} y tengo {self.age}")

person1 = Person("Juan", 18)   #Crear el objeto
person2 = Person("Jose", 20)

person1.greet()
person2.greet()