class Car:
    # Constructor to initialize the car's attributes
    def __init__(self, make, model, year):
        self._make = make  # Private attribute
        self._model = model
        self._year = year
    
    # Method to display the car's information
    def display_info(self):
        print(f"{self._year} {self._make} {self._model}")
    
    # Setter method to set the year with validation
    def set_year(self, year):
        if year > 1885:  # The first car was invented around 1885
            self._year = year
        else:
            print("Invalid year")

# Create an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Call the display_info method to print the car details
my_car.display_info()

# Try setting a valid year
my_car.set_year(2025)
my_car.display_info()  # This should now show the updated year

# Try setting an invalid year
my_car.set_year(1800)  # This should print "Invalid year"
print("THIS PROGRAM IS WRITTEN BY SARVESH BHARDWAJ ERP :- 0221BCA062")
