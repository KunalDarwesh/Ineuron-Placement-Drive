# -*- coding: utf-8 -*-
"""
@author: kunal.darwesh
"""
class Joey():
    def character(self):
        print("Loves to eat & sex")

class Chandler():
    def character(self):
        print("Is a Funny & Sarcastic")

class Ross():
    def character(self):
        print("A good paleontology")
        
class Phoebe():
    def character(self):
        print("She is weird")
        
class Monica():
    def character(self):
        print("Loves to cook, clean and is organised")

class Rachel():
    def character(self):
        print("Good in Fashion, but confused in life")        
        
        
class Friends(Joey,Chandler,Ross,Phoebe,Monica,Rachel):
    def character(self):
        Joey.character(self)
        Chandler.character(self)
        Ross.character(self)
        Phoebe.character(self)
        Monica.character(self)
        Rachel.character(self)
        print("Outstanding Comedy Series")
        
TV_Series=Friends()
TV_Series.character()