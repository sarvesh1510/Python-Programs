import importlib

# Dynamically define a math_utils module as if it were a separate module
math_utils_code = """
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
"""

# Save the code to a new module dynamically
with open("math_utils.py", "w") as f:
    f.write(math_utils_code)

# Use importlib to import the math_utils module
math_utils = importlib.import_module("math_utils")

# Call the add function from math_utils
result = math_utils.add(5, 3)

# Print the result
print(result)  # This will print 8

# Optionally, you can delete the file if you don't want it to persist
import os
os.remove("math_utils.py")
 
print("THIS PROGRAM IS WRITTEN BY SARVESH BHARDWAJ ERP :- 0221BCA062")