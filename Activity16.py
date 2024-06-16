
class Car:
    def __init__(self, manufacturer, model, make, transmission, color):
        self.manufacturer = manufacturer
        self.model = model
        self.make = make
        self.transmission = transmission
        self.color = color

    def accelerate(self):
        print(f"{self.manufacturer} {self.model} is moving")

    def stop(self):
        print(f"{self.manufacturer} {self.model} has stopped")


# Create three different car objects
car1 = Car("Toyota", "Camry", 2022, "Automatic", "Silver")
car2 = Car("Ford", "Mustang", 2018, "Manual", "Red")
car3 = Car("Honda", "Civic", 2020, "CVT", "Blue")

# Test the methods
car1.accelerate()  # Output: Toyota Camry is moving
car1.stop()  # Output: Toyota Camry has stopped

car2.accelerate()  # Output: Ford Mustang is moving
car2.stop()  # Output: Ford Mustang has stopped

car3.accelerate()  # Output: Honda Civic is moving
car3.stop()  # Output: Honda Civic has stopped
