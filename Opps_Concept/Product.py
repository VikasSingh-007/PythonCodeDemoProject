# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 12:47:42 2025

@author: mailt

This module defines classes for managing products, inventory, and order utilities.

Classes:
    Product: Represents a product with name, price, and optional product ID.
    OrderUtils: Provides static utility methods for order calculations.
    Inventory: Manages a collection of products and calculates total cost.
"""

class Product:
    """
    Represents a product with name, price, and optional product ID.

    Attributes:
        total_product_created (int): Number of products created with two arguments.
        name (str): Name of the product.
        price (str): Price of the product.
        product_id (str): Product ID (if provided).
        nameproduct (str): Name of the product (if product_id is provided).
        price_inr (str): Price in INR (if product_id is provided).
    """
    total_product_created=0
    
    def __init__(self,*args):
        """
        Initializes a Product instance.

        Args:
            *args: Can be (name, price) or (product_id, nameproduct, price_inr).
        """
        if len(args)==2:
            self.name,self.price=args
            Product.total_product_created+=1
        else:
            self.product_id,self.nameproduct,self.price_inr=args
          
    
    def display_details(self):
        """
        Prints the product details.
        """
        print(f"product_id : {self.product_id} ,name : {self.nameproduct},price : {self.price_inr}")
        
    @classmethod
    def from_string(cls,prodname):
        """
        Creates a Product instance from a string.

        Args:
            prodname (str): String in the format "name:price".

        Returns:
            Product: A new Product instance.
        """
        name,price=prodname.split(":")
        return cls(name.strip(),price)
    
class OrderUtils:
    """
    Provides static utility methods for order calculations.
    """
    @staticmethod
    def add(*args):
        """
        Returns the sum of all arguments.

        Args:
            *args: Numbers to sum.

        Returns:
            int: Sum of all arguments.
        """
        sum_allnum=0
        for num in args:
           sum_allnum=sum_allnum+num
        return sum_allnum
    
    @staticmethod
    def sum_numbers(*args):
        """
        Returns the sum of all arguments using Python's built-in sum.

        Args:
            *args: Numbers to sum.

        Returns:
            int: Sum of all arguments.
        """
        return sum(args)
    
class Inventory:
    """
    Manages a collection of products and calculates total cost.

    Attributes:
        total_cost (int): Total cost of all products.
        name (str): Name of the inventory.
        product (list): List of Product objects.
    """
    total_cost=0
    def __init__(self,name):
        """
        Initializes an Inventory instance.

        Args:
            name (str): Name of the inventory.
        """
        self.name=name
        self.product=[]
    def add_product(self,product):
        """
        Adds a product to the inventory.

        Args:
            product (Product): Product to add.
        """
        self.product.append(product)
    def check_inventory(self):
        """
        Prints a summary of products and their total cost.
        """
        item={}
        for p in self.product:
            item_id=p.product_id
            item_name=p.nameproduct
            item_price=p.price_inr
            if item_id not in item.keys():
                item[item_id]=[item_name,int(item_price)]
            else:
                item[item_id][1]=item[item_id][1]+int(item_price)
            Inventory.total_cost=Inventory.total_cost+int(item_price)
        item_counter=0
        for k,v in item.items():
            item_counter+=1
            print(f"{item_counter}. Name- {item[k][0]} -cost- {item[k][1]} ")
        print(f"total -- {Inventory.total_cost:.2f}")







