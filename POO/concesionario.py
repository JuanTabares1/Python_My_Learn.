from typing import Any


class Auto:
    def __init__(self, marca, modelo, precio):
        self.marca = marca
        self.modelo = modelo
        self. precio = precio
        self.auto_disponible = True
    
    def no_disponible(self):
        if self.auto_disponible:
            self.auto_disponible = False
            print(f"El auto {self.modelo} ya no esa disponible")
        else:
            print(f"El auto {self.modelo} no esta disponible")

    def disponible(self):
        if self.auto_disponible:
            print(f"El auto {self.modelo} ya esta disponible para la venta")
        else:
            self.auto_disponible = True
            print(f"El auto {self.modelo} ya esta disponible de nuevo para la venta")

    def vender_auto(self):
        if self.auto_disponible:
            self.auto_disponible = False
            print(f"El auto {self.modelo} fue vendido y ya no esta disponible")
        else:
            print(f"El auto {self.modelo} no esta disponible en este momento")

    def revisar_disponibilidad(self):
        return self.auto_disponible

    def get_precio(self):
        return self.precio

class Cliente:
    def __init__ (self, nombre, id):
        self.nombre = nombre
        self.id = id
        self.autos_comprados = []

    def comprar_auto(self, auto):
        if auto.disponible:
            auto.vender_auto()
            self.autos_comprados.append(auto)
            print(f"El modelo {auto.modelo} fue comprado por {self.nombre}")
        else:
            print(f"El modelo {auto.modelo} no esta disponible")
    
    def vender_auto(self, auto, concesionario):
        if auto in self.autos_comprados:
            auto.disponible()
            self.autos_comprados.remove(auto)
            concesionario.agregar_auto(auto)
        else:
            print(f"El cliente {self.nombre} vendio el auto con el modelo {auto.modelo}")

class Concecionario:
    def __init__ (self, nombre="Concesionario"):
        self.nombre = nombre
        self.autos = []
        self.clientes = []

    def agregar_auto(self, auto):
        self.autos.append(auto)
        print(f"El auto con el modelo {auto.modelo} fue agregado al concesionario {self.nombre}")

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"El cliente {cliente.nombre} fue agregado al concesionario {self.nombre}")

    def mostrar_autos_disponibles(self):
        print("Autos Disponibles")
        for auto in self.autos:
            if auto.disponible:
                print(f"{auto.modelo} de {auto.marca} con un precio de {auto.precio}")

#Crear los autos
auto1 = Auto("Chevrolet", "Camaro", 200.000)
auto2 = Auto("Ford", "Mustang", 190.000)

#Crear cliente
cliente1 = Cliente("Juan", "001")

#Crear concesionario
concesionario1 = Concecionario("TuCarro")
concesionario1.agregar_auto(auto1)
concesionario1.agregar_auto(auto2)
concesionario1.agregar_cliente(cliente1)

#Mostrar disponibles
concesionario1.mostrar_autos_disponibles()