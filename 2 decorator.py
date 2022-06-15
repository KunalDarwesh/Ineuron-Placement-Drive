# -*- coding: utf-8 -*-
"""
@author: kunal.darwesh
"""

def create_adder(x):
    def adder(y):
        return x+y
 
    return adder

def create_subtractor(x):
    def subtractor(y):
        return x-y
 
    return subtractor

def create_divisioner(x):
    def divisioner(y):
        return x/y
 
    return divisioner

def create_Multiplyer(x):
    def Multiplyer(y):
        return x*y
 
    return Multiplyer

   
add_30 = create_adder(30)
sub_30 = create_subtractor(30)
div_30 = create_divisioner(30)
mul_30 = create_Multiplyer(30)
 
print(add_30(10))
print(sub_30(10))
print(div_30(10))
print(mul_30(10))