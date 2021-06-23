# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:43:47 2021

@author: Levi G.R. van Lieshout & Jelger J. van Haskera

Classes: Kaart
Functions, mogelijke_combinaties(), unit_tests(): 
"""

import copy

class Kaart:
    """Represents a card of the game Set"
    
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
        #Is de laatste komma die geprint wordt nodig?
        
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


#Not in Class definition anymore

def possible_combinations(deck: list):
    """
    This function returns all the possible combinations of three different cards 
    from a set of twelve cards, in which the order of the cards doesn't matter.
    
    input: list of the cards in the set of twelve cards
    output: all possible combinations of three cards in this set of twelve cards.

    """
    possibilities = []
    for i in range(12):
        combination = [deck[i]]
        for j in range(i+1,12):
            combination.append(deck[j])
            for k in range(j+1,12):
                combination.append(deck[k])
                if combination not in possibilities and len(combination)==3:
                    possibilities.append(copy.copy(combination))
                    combination.pop()
            combination.pop()
    print(possibilities)
    return possibilities

def unit_tests():
    """Unit Tests: worden alleen geprint indien returnvalue onjuist is""" 
    #is_set, expected: True 
    kaart1, kaart2, kaart3=Kaart(0,1,2,1), Kaart(0,2,3,3), Kaart(0,3,1,4)
    kaart4, kaart5, kaart6=Kaart(1,0,2,1), Kaart(2,0,3,3), Kaart(3,0,1,4)
    kaart7, kaart8, kaart9=Kaart(1,2,0,1), Kaart(2,3,0,3), Kaart(3,1,0,4)
    kaart10, kaart11, kaart12=Kaart(1,2,1,0), Kaart(2,3,3,0), Kaart(3,1,4,0)
    
    if kaart1.is_set(kaart2,kaart3)==False:
        print("Unit test 1: "+str(kaart1)+","+str(kaart2)+","+str(kaart3)+" "+ "Expected: True, return Falue:"+str(kaart1.is_set(kaart2,kaart3)))
    if kaart4.is_set(kaart5,kaart6)==False:
        print("Unit test 2: "+str(kaart4)+","+str(kaart5)+","+str(kaart6)+" "+ "Expected: True, return Falue:"+str(kaart4.is_set(kaart5,kaart6)))
    if kaart7.is_set(kaart8,kaart9)==False:
        print("Unit test 3: "+str(kaart7)+","+str(kaart8)+","+str(kaart9)+" "+ "Expected: True, return Falue:"+str(kaart7.is_set(kaart8,kaart9)))
    if kaart10.is_set(kaart11,kaart12)==False:
        print("Unit test 4: "+str(kaart10)+","+str(kaart11)+","+str(kaart12)+" "+ "Expected: True, return Falue:"+str(kaart10.is_set(kaart11,kaart12)))      
    
    #is_set, expected: False 
    kaart13, kaart14, kaart15=Kaart(1,1,2,1), Kaart(0,2,2,3), Kaart(0,1,1,3)
    kaart16, kaart17, kaart18=Kaart(2,1,3,3), Kaart(2,1,1,2), Kaart(1,2,1,2)
    kaart19, kaart20, kaart21=Kaart(3,2,1,1), Kaart(2,3,3,3), Kaart(3,3,1,1)
    
    if kaart13.is_set(kaart14,kaart15)==True:
        print("Unit test: "+str(kaart13)+","+str(kaart14)+","+str(kaart15)+" "+ "Expected: False, return Falue:"+str(kaart13.is_set(kaart14,kaart15)))
    if kaart16.is_set(kaart17,kaart18)==True:
        print("Unit test: "+str(kaart16)+","+str(kaart17)+","+str(kaart18)+" "+ "Expected: False, return Falue:"+str(kaart16.is_set(kaart17,kaart18)))
    if kaart19.is_set(kaart20,kaart21)==True:
        print("Unit test: "+str(kaart19)+","+str(kaart20)+","+str(kaart21)+" "+ "Expected: False, return Falue:"+str(kaart19.is_set(kaart20,kaart21)))
