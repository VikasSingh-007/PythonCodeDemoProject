# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 13:14:22 2025

@author: mailt
"""
from Opps_Concept.Product import Product
from Opps_Concept.Product import Inventory
from Opps_Concept.Transaction import Transaction
from Opps_Concept.Product import OrderUtils
from Opps_Concept.Vehicle import *
from Opps_Concept.Employee import *
from Opps_Concept.CustomException import *
if __name__ == "__main__":
    print("Running product.py directly...")
    Product.from_string("Milk:20")
    Product.from_string("Rice:60")
    Product.from_string("Banana:120")
    print(Product.total_product_created)
    t1=Transaction(1, "60000")
    t2=Transaction(1, "60000")
    print(t1==t2)
    print(t1)
    print(f"test --> {t1}")
    print(t1.get_company())
    print(OrderUtils.add(1,2,3,4,7,2,-29))
    print(OrderUtils.sum_numbers(1,2,-1))
    
    print("product class implematation  in new ----")
    p1=Product("01","potato","20")
    p2=Product("01","potato","40")
    p3=Product("02","chilli","30")
    p4=Product("04","tomato","90")
    Inventory1=Inventory("vegitable")
    Inventory1.add_product(p1)
    Inventory1.add_product(p2)
    Inventory1.add_product(p3)
    Inventory1.add_product(p4)
    
    Inventory1.check_inventory()
    
    truck1=DeliveryTruck("01","2025","6000","MH3489GH56","Delhi-Hyderabad")
    truck2=DeliveryTruck("02","2015","9000","MH3489GH57","Mumbai-Hyderabad") 
    RGVan1=RefrigeratedVan("01","2015","9000","MDH85RG56","-50") 
    RGVan2=RefrigeratedVan("02","2016","5000","MDH85RG57","-60")            
    vechileList=[truck1,truck2,RGVan1,RGVan2]
    for van in vechileList:
        van.get_details()
    print(RGVan1.load_vechile(20000))
    
    m1=Manager("01", "siva")
    Op1=Operator("01", "Shayam")

    print(m1.calculate_salary())
    print(m1.grant_bonus(9000))
    print(m1.grant_bonus())
    print(Op1.calculate_salary())
    
    manufacuring_unit=ManufacturingUnit()
    distrubution_unit=DistributionHub()
    print(manufacuring_unit.process_batch("45"))

    def handle_entity(obj,batch_id):
        return obj.process_batch(batch_id)
        
    print(handle_entity(distrubution_unit, "11"))
    B1=Batch("01", 25)
    B2=Batch("02", 30)
    
    print(B1)
    print(len(B1))
    B3=B1+B2
    print(B3)
    
    try:
       B4=B1+distrubution_unit
       print(B4)
    except Exception as e:
        print(e)
    else:
        print("success")
    finally:
        print("add dunder method")
        
    try:
       print(evalute_oder(200,500))
    except InsufficientOrderError as e :
       print(e)
    except InsufficientFundsError as e:
       print(e)