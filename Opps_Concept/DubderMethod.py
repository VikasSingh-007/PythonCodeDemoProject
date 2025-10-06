# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 20:42:54 2025

@author: mailt
"""

class DunderMethod:
    def __init__(self,customer,items,totalCost):
        self.customer=customer
        self.items=items
        self.totalCost=totalCost
    def __str__(self):
        return f"customer name {self.customer} and total ites is {self.items} total cost :{self.totalCost:>10.2f}"
    
    def __add__(self,other):
        if isinstance(other,DunderMethod):
            cobined_item=self.items.copy()
            for k,v in other.items.items():
                if k in cobined_item.keys():
                    cobined_item[k]=cobined_item[k]+v
                else:
                    cobined_item[k]=v
            cobined_total=self.totalCost+other.totalCost
            return DunderMethod(self.customer,cobined_item,cobined_total)
        else:
            return TypeError("not the istance")
    def __radd__(self,other):
        if isinstance(other, (int,float)):
            self.totalCost=self.totalCost+other
            return DunderMethod(self.customer,self.items,self.totalCost)
    def __rsub__(self,other):
        if isinstance(other, (int,float)):
            self.totalCost=self.totalCost-other
            return DunderMethod(self.customer,self.items,self.totalCost)
   
        
cust2=DunderMethod("priya",{"lime":25,"egg":40},500)
cust3=DunderMethod("priya",{"bread":25,"egg":40},300)

print(20+cust2+cust3)

class Inventory:
    # A class that represents a single item's stock in the inventory.
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock
    def __repr__(self):
        return f"Inventory(name='{self.name}', stock={self.stock})"
    # The __iadd__ method is called for the '+=' operator.
    # It takes the 'other' parameter (the value to be added).
    def __iadd__(self, other):
        # We first check if the 'other' is an integer, to avoid type errors.
        if isinstance(other, int):
            # We modify the 'stock' attribute of the object irectly.
            self.stock += other
            return self
        else:
            raise TypeError("In-place addition can only be performed with an integer.")
    # The __isub__ method for the '-=' operator.
    def __isub__(self, other):
        if isinstance(other, int):
            self.stock -= other
            return self
        else:
            raise TypeError("In-place subtraction can only be performed with an integer.")
            

Inven1=Inventory("Mik", 20)
Inven2=Inventory("Mik", 20)

falooda_stock = Inventory("Mango Falooda", 50)
print(f"Initial stock: {falooda_stock}")

        
    
     