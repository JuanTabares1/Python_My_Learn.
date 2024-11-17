class Vehicle:
    def __init__(self, brand, model, price):
        #Encapsulacion
        self.brand = brand
        self.model = model
        self.price = price
        self.is_available = True

    def sell(self):
        if self.is_available:
            self.is_available = False
            print(f"El vehiculo {self.brand} ha sido vendido")
        else:
            print(f"El vehiculo {self.brand} no esta disponible")

    #Abstraccion
    def check_available(self):
        return self.is_available
    
    def get_price(self):
        return self.price
    
    def start_engine(self):
        raise NotImplementedError("Este metodo sebe ser implementado por la subclase")

    def stop_engine(self):
        raise NotImplementedError("Este metodo sebe ser implementado por la subclase")
    
#Herencia
class Car(Vehicle):
    #Polimorfismo
    def start_engine(self):
        if not self.is_available:
            return f"El motor del coche {self.brand} esta en marcha"
        else:
            return f"El coche {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del coche {self.brand} se detuvo"
        else:
            return f"El coche {self.brand} no esta disponible"
        
class Truck(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor del camion {self.brand} esta en marcha"
        else:
            return f"El camion {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor del camion {self.brand} se detuvo"
        else:
            return f"El camion {self.brand} no esta disponible"
        
class Motorcycle(Vehicle):
    def start_engine(self):
        if not self.is_available:
            return f"El motor de la motocicleta {self.brand} esta en marcha"
        else:
            return f"La motocicleta {self.brand} no esta disponible"
        
    def stop_engine(self):
        if self.is_available:
            return f"El motor de la motocicleta {self.brand} se detuvo"
        else:
            return f"La motocicleta {self.brand} no esta disponible"
        
class Customer:
    def __init__(self, name):
        self.name = name
        self.purchased_vehicles = []

    def buy_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            vehicle.sell()
            self.purchased_vehicles.append(vehicle)
        else:
            print("El vehiculo no esta disponible")

    def inquire_vehicle(self, vehicle: Vehicle):
        if vehicle.check_available():
            availability = "Esta disponible"
            print(f"El vehiculo {vehicle.brand} {availability} y cuesta {vehicle.get_price()}")
        else:
            availability = "No disponible"
            print(f"El vehiculo {vehicle.brand} {availability}")

class Dealership:
    def __init__(self):
        self.inventory = []
        self.customers = []

    def add_vehicle(self, vehicle: Vehicle):
        self.inventory.append(vehicle)
        print(f"El vehiculo {vehicle.brand} se agrego con exito")

    def register_customer(self, customer: Customer):
        self.customers.append(customer)
        print(f"El cliente {customer.name} de registro con exito")

    def show_available_vehicle(self):
        print("Vehiculos disponibles en la tienda")
        for vehicle in self.inventory:
            if vehicle.check_available():
                print(f"- {vehicle.brand} por {vehicle.price}")

car1 = Car("Toyota", "Corolla", 20000)
truck1 = Truck("VOLVO", "FH16", 60000)
motorcycle1 = Motorcycle("yamaha", "MT09", 30000)

customer1 = Customer("Juan")

dealership1 = Dealership()
dealership1.add_vehicle(car1)
dealership1.add_vehicle(truck1)
dealership1.add_vehicle(motorcycle1)

#Mostrar vehiculos disponibles
dealership1.show_available_vehicle()

#Cliente consulta un vehiculo
customer1.inquire_vehicle(car1)

#CLiente compra un vehiculo
customer1.buy_vehicle(car1)

#Mostrar vehiculos disponibles
dealership1.show_available_vehicle()