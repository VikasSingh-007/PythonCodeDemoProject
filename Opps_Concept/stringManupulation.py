# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 20:58:00 2025

@author: mailt

"""
from functools import reduce
import time
list1=list(["a","b","c"])
y=lambda x:"_".join(x)
print(y(list1))



strjoin=reduce(lambda x,y:x+"_"+y,list1)
print(strjoin)

total_count=0

def getCount():
    global total_count
    total_count=4
    total_count=total_count+1
    return total_count



print(getCount())
print(getCount())
print(total_count)

print("timer -please set time timer")
getCounter=input()
for x in range(int(getCounter),0,-1):
    print(f"timer start...{x}")
    
    for y in range(0,60):
        print(".")
        time.sleep(1)
        


