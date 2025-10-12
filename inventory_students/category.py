# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Defines the Category class.

Step-by-step Instructions:
1. Create Category class with attributes:
   - category_id (int)
   - name (str)
   - products (list of Product objects)
2. Add methods:
   - add_product(product)
   - remove_product(product_id)
   - list_products() → return all products in this category
3. Ensure duplicate products are not added.

TODO for Students:
- Implement Category class.
- Link products properly.
- Use exceptions for invalid operations.
"""


# Handles product categories.
# TODO: Implement this file

# Category class groups products (e.g., Electronics, Clothing).
# It can track all products under that category.
from inventory_students.product import Product
from inventory_students.exceptions import  categoryNotFoundError
from inventory_students.exceptions import ProductNotFoundError
class Category:
    def __init__(self, name,category_id):
        self.name=name
        self.category_id=category_id        
        self.products=[]
        
        
    def add_product(self, product):
        if not isinstance(product, Product):
            raise  ProductNotFoundError('This product not valid !!!')
        self.products.append(product)
        
        return f"total products are{self.products}"
     
    def remove_product(self, product_id):
        check_product=False
        for p in self.products:
            if p.proudct_id==product_id:
                self.products.remove(p)
                check_product=True
           
        if check_product==False:
            raise ProductNotFoundError("product not in list")
        return f"The remaining product is{self.products}"
    
      

    def list_products(self):
       list_products =[x for x in self.products]
       return f"list of thr products are{list_products}"
    def __str__(self):
       return f"name the product{self.name},category of the product{self.category_id},the products are{self.products}"
