# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 17:52:42 2025

@author: mailt
"""

class Transaction:
    def __init__(self,EmpID,Salary):
        self.EmpID=EmpID
        self.Salary=Salary
        self._company="The Company"
    
    def get_company(self):
        return self._company
        
    def __eq__(self,other):
        if not isinstance(other,Transaction):
            return NotImplemented
        return self.EmpID==other.EmpID
    def __repr__(self):
        return f"Emp id is {self.EmpID} and Slaray is {self.Salary}"
    def __str__(self):
        return f"the instance of Transaction class is Emp id is {self.EmpID} and Slaray is {self.Salary}"
    

class Product:
    def __init__(self,name,price):
        self.name=name
        self.price
