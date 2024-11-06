from abc import ABC, abstractmethod  # Import necessary components from abc module

# Abstract base class
class Animal(ABC): 
    @abstractmethod
    def speak(self): 
        pass

# Derived class Dog
class Dog(Animal): 
    def speak(self): 
        return "Woof!" 

# Derived class Cat
class Cat(Animal): 
    def speak(self): 
        return "Meow!" 

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the speak method on both objects
print(dog.speak())  # Output: Woof!
print(cat.speak())  # Output: Meow!
print("THIS PROGRAM IS WRITTEN BY SARVESH BHARDWAJ ERP :- 0221BCA062")