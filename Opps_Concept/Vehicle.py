# -*- coding: utf-8 -*-
"""
Created on Tue Sep 30 16:24:55 2025

@author: mailt
"""

class Vehicle:
    def __init__(self,vehicle_id,model,capacity_kg):
        self.vehicle_id=vehicle_id
        self.model=model
        self.capacity_kg=capacity_kg
        
    def get_details(self):
        return f'vechicle id {self.vehicle_id:>10}model{self.model:>10}capacity_kg{self.capacity_kg}'
       

class DeliveryTruck(Vehicle):
    def __init__(self, vehicle_id, model, capacity_kg,icense_plate,route):
        super().__init__(vehicle_id, model, capacity_kg)
        self.icense_plate=icense_plate
        self.route=route
        
    def get_details(self):
        print( f'vechicle id {self.vehicle_id:>5} model {self.model:>5} capacity_kg {self.capacity_kg:>5} icense_plate {self.icense_plate:>5} route {self.route}')
    
class RefrigeratedVan(Vehicle):
    def __init__(self, vehicle_id, model, capacity_kg,icense_plate,temperature_limit_celsius):
        super().__init__(vehicle_id, model, capacity_kg)
        self.icense_plate=icense_plate
        self.temperature_limit_celsius=temperature_limit_celsius
    def check_temprature(self):
        if self.temperature_limit_celsius<=-20:
            return "temperature is OK"
        else:
            return "temperature is increasing then -20 degree centigrade"
    def load_vechile(self,load_qantity):
        calculate_load=float(load_qantity)*0.5
        if calculate_load<=float(self.capacity_kg):
            return "load is in limit"
        else:
            return "load is out of limit"
        
    def get_details(self):
        print(f'vechicle id {self.vehicle_id:>5} model {self.model:>5} capacity_kg {self.capacity_kg:>5} icense_plate {self.icense_plate:>5} temperature_limit_celsius {self.temperature_limit_celsius}')
