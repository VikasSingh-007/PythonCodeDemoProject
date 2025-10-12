# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Defines the Store class.

Step-by-step Instructions:
1. Create Store class with attributes:
   - name (str)
   - products (dict → product_id: Product)
   - categories (dict → category_id: Category)
2. Methods:
   - add_product(product)
   - remove_product(product_id)
   - update_stock(product_id, qty)
   - get_product(product_id) → return Product object
   - list_all_products()
3. Ensure error handling:
   - Invalid product IDs
   - Negative stock updates

TODO for Students:
- Implement Store class methods.
- Maintain consistent product and category mappings.
- Use custom exceptions for errors.
"""


# Handles the Store class and product operations.
# TODO: Implement this file
# Store class manages all products and categories.
# Acts like a central manager.

from inventory_students.product import Product
from inventory_students.category import Category
from inventory_students.report import Report
from inventory_students.exceptions import ProductNotFoundError, InvalidOperationError, categoryNotFoundError


class Store:
    store_count = 0

    def __init__(self, name):
        self.name = name
        self.products = {}
        self.categories = {}
        Store.store_count+=1

    @classmethod
    def get_store_count(cls):
         return f"total store ={cls.store_count}"

    def _add_product(self, product):
        if isinstance(product, Product):
            product_id = product.proudct_id
            self.products[product_id] = product
        else:
            raise ProductNotFoundError("Error - Not a valid product!!!")

    def remove_product(self, product_id):
        if product_id in self.products.keys():
            self.products.pop(product_id)
        else:
           raise ProductNotFoundError("Error - Product Not Found !!!")

    def update_stock(self, product_name, qty):
        check_product=False
        for k in  self.categories.keys():
            for p in self.categories[k].products:
                if p.name==product_name:
                    if float(qty) > 0:
                        p.stock=float(qty)
                    else:
                        raise InvalidOperationError("Error-Quantity should be greater then Zero")
                    check_product=True
        if check_product==False:
            raise ProductNotFoundError("Error : Invalid product")

    def update_price(self, product_name, new_price):
        check_product=False
        for k in  self.categories.keys():
            for p in self.categories[k].products:
                if p.name==product_name:
                    if float(new_price) > 0:
                        p.price=float(new_price)
                    else:
                        raise InvalidOperationError("Error-Price should be greater then Zero")
                    check_product=True
        if check_product==False:
            raise ProductNotFoundError("Error : Invalid product")
            
    def add_category(self, category):
       if isinstance(category, Category):
           category_id = category.category_id
           self.categories[category_id] = category
           for product in category.products:
               self._add_product(product)
       else:
           raise categoryNotFoundError("Error - Not a valid Category!!!")

    

    def apply_discount_to_category(self, category_name, percent):
        for k in self.categories.keys():
            if self.categories[k].name == category_name:
                category_all_product = self.categories[k].products
                for product in category_all_product:
                    discounted_price = float(product.price) - (float(product.price) * float(percent) / 100)
                    self.update_price(product.name, discounted_price)

    def list_all_products(self):
        print(f'ProductID:          Name:          Price:          Stock:         Category:')
        for k in self.products.keys():
            print(f'{self.products[k].proudct_id:<10}          {self.products[k].name:<8}          {self.products[k].price:<8}       {self.products[k].stock:<4}          {self.products[k].category:<10}')

    def find_product(self, product_id):
        if product_id in self.products.keys():
            return self.products[product_id]
        else:
            raise ProductNotFoundError("Error - Product Not Found !!!")
