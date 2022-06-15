# -*- coding: utf-8 -*-
"""
@author: kunal.darwesh
"""

from abc import ABC, abstractmethod
 
class Cars(ABC):
 
    @abstractmethod
    def noofshape(self):
        pass
 
class Hatchback(Cars):
 
    # overriding abstract method
    def noofshape(self):
        print("I have Maruti Suzuki Swift")
 
class Sedan(Cars):
 
    # overriding abstract method
    def noofshape(self):
        print("I have Honda City")
 
class MiniSUV(Cars):
 
    # overriding abstract method
    def noofshape(self):
        print("I have Hyundai Creta")
 
class SUV(Cars):
 
    # overriding abstract method
    def noofshape(self):
        print("I have Toyota Fortuner")
 

R = Hatchback()
R.noofshape()
 
K = Sedan()
K.noofshape()
 
R = MiniSUV()
R.noofshape()
 
K = SUV()
K.noofshape()