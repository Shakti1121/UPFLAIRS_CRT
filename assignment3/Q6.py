# 6. Car Rental System using OOP
class Vehicle:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"

class Car(Vehicle):
    def __init__(self, brand, model, year, seats):
        super().__init__(brand, model, year)
        self.seats = seats

    def display_info(self):
        return super().display_info() + f", Seats: {self.seats}"

class Bike(Vehicle):
    def __init__(self, brand, model, year, type):
        super().__init__(brand, model, year)
        self.type = type  # Type can be "Sports" or "Cruiser"

    def display_info(self):
        return super().display_info() + f", Type: {self.type}"

car = Car("Toyota", "Corolla", 2022, 5)
bike = Bike("Yamaha", "R15", 2021, "Sports")
print(car.display_info())  
print(bike.display_info())  
