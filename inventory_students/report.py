# Instructions for Students
# Fill in the missing code as per the instructions provided in comments.
# Follow OOP principles and ensure proper use of classes, methods, and error handling.

"""
Handles reports and data export.

Step-by-step Instructions:
1. Define Report class with methods:
   - generate_inventory_summary(store)
     → Show all products, stock, total value
   - generate_category_summary(store)
     → Group products by category
2. Export options (optional extended scope):
   - Export to JSON
   - Export to CSV

TODO for Students:
- Implement Report class.
- Write clean tabular output using print.
- Optionally, add export to a file.
"""


# Generates reports for inventory.
# TODO: Implement this file
# Reporting functions to analyze inventory.
# Also include file export for CSV/JSON.

import json
import csv
from inventory_students.utils import save_to_json
import os

class Report:
    def __init__(self, store):
        self.store = store

    def total_inventory_value(self):
        total_stock=0
        total_price=0
        print("--------------------Inventory Report----------------------------------------------------------------")
        print(f'ProductID:          Name:          Price:          Stock:         Category:        InventoryValue:')
        for k in  self.store.categories.keys():
            for p in self.store.categories[k].products:
                total_stock=int(p.stock)+total_stock
                total_Inventory_value=int(p.stock)*int(p.price)
                total_price=total_Inventory_value+total_price
                print(f'{p.proudct_id:<10}          {p.name:<8}          {p.price:<8}       {p.stock:<4}          {p.category:<10}        {total_Inventory_value:<10}')
        print(f"Total Inventory: {total_stock}")
        print(f"Total Price: {total_price}")
       
            
            

    def low_stock_items(self, threshold=5):
        lowInventory=False
        print("--------------------Low Inventory Report----------------------------------------------------------------")
        print(f'ProductID:          Name:          Price:          Stock:         Category:        MinimunInventoryRequired:')
        for k in  self.store.categories.keys():
            for p in self.store.categories[k].products:
                if int(p.stock)<=threshold:
                    lowInventory=True
                    print(f'{p.proudct_id:<10}          {p.name:<8}          {p.price:<8}       {p.stock:<4}          {p.category:<10}        {threshold:<10}')
        if lowInventory==False:
            print(f'None                None             None            None            None             {threshold}')
            
           
       

    def category_summary(self):
        print("--------------------Category Summary Report----------------------------------------------------------------")
        for k in  self.store.categories.keys():
            print(f"Category: {self.store.categories[k].name:>5} -------------------------------------")
            print(f'ProductID:          Name:          Price:          Stock:      InventoryValue:')
            for p in self.store.categories[k].products:
                total_Inventory_value=int(p.stock)*int(p.price)
                print(f'{p.proudct_id:<10}          {p.name:<8}          {p.price:<8}       {p.stock:<4}       {total_Inventory_value:<10}')
                

    def export_to_json(self, filename):
        alldata=[]
        for k in  self.store.categories.keys():
            for p in self.store.categories[k].products:
                data={"product_Id":p.proudct_id,
                  "product":[f"name : {p.name}",f"price : {p.price}",f"stock : {p.stock}",f"category : {p.category}"]
                  }
                alldata.append(data)
        save_to_json(alldata,filename)

    def export_to_csv(self, filename):
        file_exists = os.path.isfile(filename)
        os.remove(filename)
        with open(filename, mode="a", newline="") as file:
            fieldnames = ["proudct_id", "name", "price","stock","category"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()
            
            for k in  self.store.categories.keys():
               for p in self.store.categories[k].products:
                   writer.writerow({"proudct_id": p.proudct_id, "name":  p.name, "price": p.price,"stock": p.stock,"category": p.category})
   
    
