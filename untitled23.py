class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"Brand: {self.brand}, Model: {self.model}"

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def display_engine(self):
        return f"Engine Type: {self.engine_type}"

class Car(Vehicle, Engine):
    def __init__(self, brand, model, engine_type, color):
        super().__init__(brand, model)
        Engine.__init__(self, engine_type)
        self.color = color

    def display_car_info(self):
        return f"{self.display_info()}, {self.display_engine()}, Color: {self.color}"

car1= Car(brand="Toyota", model="Corolla", engine_type="Hybrid", color="Blue")
car2= Car(brand="Toyota", model="Corolla", engine_type="Hybrid", color="Blue")

print(car1.display_car_info())
print(car2.display_car_info())

