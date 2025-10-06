# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 17:22:15 2025

@author: mailt
"""

class Employee:
    def __init__(self,employee_id,name):
        self.employee_id=employee_id
        self.name=name
        self.base_salary=50000
        
    def calculate_salary(self):
        return self.base_salary +" INR"
class Manager(Employee):
    def __init__(self, employee_id, name):
        super().__init__(employee_id, name)
        self.base_bonus=10000
    def calculate_salary(self):
        return str(self.base_salary + self.base_bonus)+" INR"
    def grant_bonus(self,bonus_amount=5000):
        return f"bonus amount {bonus_amount}"

class Operator(Employee):
    def __init__(self, employee_id, name):
        super().__init__(employee_id, name)
        self.base_deduct=5000
        
    def calculate_salary(self):
        return str(self.base_salary - self.base_deduct)+" INR"

m1=Manager("01", "siva")
Op1=Operator("01", "Shayam")

print(m1.calculate_salary())
print(m1.grant_bonus(9000))
print(m1.grant_bonus())
print(Op1.calculate_salary())
        
from abc import ABC,abstractmethod

class SupplyChainEntity(ABC):
    def __init_(self):
        pass
    
    @abstractmethod
    def process_batch(self,batch_id):
        pass

class ManufacturingUnit(SupplyChainEntity):
    def process_batch(self,batch_id):
        return f"procssing Manufacturing unit of batch id {batch_id}"
class DistributionHub(SupplyChainEntity):
    def process_batch(self,batch_id):
        return f"procssing Distribution unit of batch id {batch_id}"

manufacuring_unit=ManufacturingUnit()
distrubution_unit=DistributionHub()
print(manufacuring_unit.process_batch("45"))

def handle_entity(obj,batch_id):
    return obj.process_batch(batch_id)
    
print(handle_entity(distrubution_unit, "11"))

class Batch:
    def __init__(self,batch_id,quantity):
        self.batch_id=batch_id
        self.quantity=quantity
    def __str__(self):
       return f"batch id : {self.batch_id} quantity:{self.quantity}"
    def __len__(self):
        return self.quantity
    def __add__(self,other):
        if isinstance(other, Batch):
            new_batch=self.batch_id+other.batch_id
            new_quantity=int(self.quantity)+int(other.quantity)
            return Batch(new_batch, new_quantity)
        else:
            raise Exception("Error Not Implemanted")
   
B1=Batch("01", 25)
B2=Batch("02", 30)
print(B1)
print(len(B1))
B3=B1+B2
print(B3)

    

        