# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 21:44:47 2025

@author: mailt
"""

class InsufficientFundsError(Exception):
    def __init__(self,order, amount):
        super().__init__(f"Balance {amount} is not enough for order {order} qty")
        self.order = order
        self.amount = amount
        
class InsufficientOrderError(Exception):
    def __init__(self,order):
       super().__init__(f"insufficent order {order}")
       self.order=order
       
       
def evalute_oder(order,amount):
    if order<10:
        raise InsufficientOrderError(order)
    elif amount<(order*10):
        raise InsufficientFundsError(order, amount)
    
    return f"order :{order} qty accepted"
    
        
        
try:
    print(evalute_oder(11,500))
except InsufficientOrderError as e :
    print(e)
except InsufficientFundsError as e:
    print(e)