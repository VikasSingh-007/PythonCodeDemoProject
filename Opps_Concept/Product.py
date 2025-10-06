# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 12:47:42 2025

@author: mailt
"""

class Product:
    total_product_created=0
    
    def __init__(self,*args):
        if len(args)==2:
            self.name,self.price=args
            Product.total_product_created+=1
        else:
            self.product_id,self.nameproduct,self.price_inr=args
          
    
    def display_details(self):
        print(f"product_id : {self.product_id} ,name : {self.nameproduct},price : {self.price_inr}")
        
    @classmethod
    def from_string(cls,prodname):
        name,price=prodname.split(":")
        return cls(name.strip(),price)
    
class OrderUtils:
    @staticmethod
    def add(*args):
        sum_allnum=0
        for num in args:
           sum_allnum=sum_allnum+num
        return sum_allnum
    
    @staticmethod
    def sum_numbers(*args):
        return sum(args)
    
class Inventory:
    total_cost=0
    def __init__(self,name):
        self.name=name
        self.product=[]
    def add_product(self,product):
        self.product.append(product)
    def check_inventory(self):
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
            
    
    


    
        
