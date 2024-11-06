# Define the Car class
class Car:
    # Constructor to initialize the car's attributes
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    # Method to display the car's information
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Call the display_info method to print the car details
my_car.display_info()
print("THIS PROGRAM IS WRITTEN BY SARVESH BHARDWAJ ERP :- 0221BCA062")