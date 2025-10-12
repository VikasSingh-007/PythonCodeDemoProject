# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Defines the Product class.

Step-by-step Instructions:
1. Define a Product class with attributes:
   - product_id (int)
   - name (str)
   - price (float)
   - stock (int)
2. Add __init__ method to initialize attributes.
3. Add __str__ method to return a nice string representation.
4. Add update_stock method to increase or decrease stock.
   - Ensure stock cannot go below 0.
5. Add apply_discount method (optional extended scope).

TODO for Students:
- Implement Product class fully.
- Ensure validations (e.g., price >= 0, stock >= 0).
- Raise exceptions for invalid inputs.
"""

# Handles the Product class.
# TODO: Implement this file

# Product class represents a single store item.
# Each product has: id, name, price, stock, and category.
from inventory_students.exceptions import ProductNotFoundError
from inventory_students.exceptions import InvalidOperationError
class Product:
    def __init__(self, product_id, name, price, stock, category):
        self.proudct_id=product_id
        self.name=name
        self.price=price
        self.stock=stock
        self.category=category

    def update_stock(self, quantity):
       if self.stock+quantity<0:
           raise ProductNotFoundError("product is invalid")
       self.stock+=quantity
       return f" total stock is {self.stock}"
           
    def update_price(self, new_price):
       if self.price+new_price<0:
           raise InvalidOperationError("Enetred price is not suffiecient")
       self.price+=new_price
       return f"total price is{self.price}"
    def apply_discount(self, percent):
        price = self.price - (self.price * percent/100)
        return f"price after discuont {price}"
        
        # TODO: Reduce price by given percentage
        # Hint: price = price - (price * percent/100)
      

    def __str__(self):
        # TODO: Return formatted product details
        return f" product_id is:{self.product_id},product name is {self.name},total price is{self.price},total stock is {self.stock},category is{self.category}" 