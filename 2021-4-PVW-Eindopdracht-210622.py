# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:43:47 2021

@author: Levi G.R. van Lieshout & Jelger J. van Haskera

Classes: Kaart
Functions: 
"""


class Kaart:
    """Represents a cart of the game Set"
    
    Attributes: color, number, filling, shape.
    Methods: init, str
    Functions: is_set"""
    
    def __init__(self,color=0,number=0,filling=0,shape=0):
        self.color=color
        self.number=number
        self.filling=filling
        self.shape=shape
        
    def __str__(self):
        return("("+str(self.color)+","+str(self.number)+","+str(self.filling)+","+str(self.shape)+","+")")
        
    def is_set(self,other1,other2):
        matchings={"color": False,"number": False, "filling": False, "shape": False}
        matchings["color"]=(self.color==other1.color and other1.color==other2.color) or (self.color!=other1.color and other1.color!=other2.color and self.color!=other2.color)
        matchings["number"]=(self.number==other1.number and other1.number==other2.number) or (self.number!=other1.number and other1.number!=other2.number and self.number!=other2.number)
        matchings["filling"]=(self.filling==other1.filling and other1.filling==other2.filling) or (self.filling!=other1.filling and other1.filling!=other2.filling and self.filling!=other2.filling)
        matchings["shape"]=(self.shape==other1.shape and other1.shape==other2.shape) or (self.shape!=other1.shape and other1.shape!=other2.shape and self.shape!=other2.shape)
        for i in matchings:
            if matchings[i]==False:
                return matchings[i]
        return True

"""Unit Tests:""" 
#is_set, expected: True 
kaart1=Kaart(0,1,2,1)
kaart2=Kaart(0,2,3,3)
kaart3=Kaart(0,3,1,4)

print("Unit test: "+str(kaart1)+","+str(kaart2)+","+str(kaart3)+" "+ "Expected: True, return Falue:"+str(kaart1.is_set(kaart2,kaart3)))
      
#is_set, expected: False 
kaart4=Kaart(1,1,2,1)
kaart5=Kaart(0,2,2,3)
kaart6=Kaart(0,1,1,3)

print("Unit test: "+str(kaart4)+","+str(kaart5)+","+str(kaart6)+" "+ "Expected: False, return Falue:"+str(kaart4.is_set(kaart5,kaart6)))