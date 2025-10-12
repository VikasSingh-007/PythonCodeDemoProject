# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Utility functions (helper code).

Step-by-step Instructions:
1. Implement data validation helpers:
   - validate_price(price) → raise error if < 0
   - validate_stock(stock) → raise error if < 0
2. Implement file helpers (optional):
   - save_to_json(data, filename)
   - load_from_json(filename)

TODO for Students:
- Add at least 2 validation functions.
- Optionally, implement file handling for persistence.
"""
import json
from inventory_students.exceptions import InvalidOperationError

def validate_price(price):
    if int(price)<0:
        raise InvalidOperationError("Error - price should be greater then Zero") 
               
def validate_stock(stock):
    if int(stock)<0:
        raise InvalidOperationError("Error - Stock should be greater then Zero")

def save_to_json(data, filename):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Data saved successfully to '{filename}'")

    except TypeError as te:
        print(f" TypeError: Data is not in json format ({te})")

    except FileNotFoundError:
        print(f" Error: The file path '{filename}' is invalid.")

    except Exception as e:
        print(f"Unexpected error occurred: {e}")

def load_from_json(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
        print(f"Data loaded successfully from '{filename}'")
        return data

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None

    except Exception as e:
        print(f"Unexpected error occurred: {e}")
        return None
    







    
