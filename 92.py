# Base class Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    # Method to display vehicle info
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Derived class Car
class Car(Vehicle):
    def __init__(self, make, model, year, fuel_type):
        super().__init__(make, model, year)  # Call the base class constructor
        self.fuel_type = fuel_type  # Additional attribute specific to Car
    
    # Overriding the display_info method
    def display_info(self):
        super().display_info()  # Call the display_info method of the parent class (Vehicle)
        print(f"Fuel type: {self.fuel_type}")  # Print the fuel type for the car

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020, "Petrol")

# Displaying the car's information
my_car.display_info()
print("THIS PROGRAM IS WRITTEN BY SARVESH BHARDWAJ ERP :- 0221BCA062")
