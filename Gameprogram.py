# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 16:04:27 2021

@author: Jelger
"""
import copy
import random
import time

class Card:
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
        return("("+str(self.color)+","+str(self.number)+","+str(self.filling)+","+str(self.shape)+")")
        
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

#Not in Card definition anymore

class Game:
    """
    Represents a round of the game Set
    
    Attributes: set_of_twelve, deck
    Methods: init, str
    Functions: update_set_of_twelve
    """
    def __init__(self):
        """
        This function creates an object representing an round of the game Set.
        Input: -
        Output: game: Game
        """
        self.deck = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        self.deck.append(Card(i,j,k,l))
        random.shuffle(self.deck)

        self.set_of_twelve = []
        for i in range(12):
            self.set_of_twelve.append(str(self.deck[-1]))
            del self.deck[-1]
        
    def __str__(self):
        return("Cards on the table:\n"+str(self.set_of_twelve[0])+str(self.set_of_twelve[1])+str(self.set_of_twelve[2])+str(self.set_of_twelve[3])+"\n"+str(self.set_of_twelve[4])+str(self.set_of_twelve[5])+str(self.set_of_twelve[6])+str(self.set_of_twelve[7])+"\n"+str(self.set_of_twelve[8])+str(self.set_of_twelve[9])+str(self.set_of_twelve[10])+str(self.set_of_twelve[11])+"\n"+"Aantal kaarten op de stapel:"+str(len(self.deck)))
        
    def update_set_of_twelve(self, set_indices):
        """
        Removes the last three elements of self.deck and replaces indicated cards of self.set_of_twelve with this new three cards.
        
        Input: game, set_indices: list of cards in the set_of_twelve which have to be renewed.
        Output: none
        Changed attributes: self.deck, self.set_of_twelve
        """
        for i in set_indices:
            self.set_of_twelve[i]=self.deck[-1]
            del self.deck[-1]
            
#Not in Game definition anymore

def possible_combinations(set_of_twelve: list):
    """
    This function returns all the possible combinations of three different cards 
    from a set of twelve cards, in which the order of the cards doesn't matter.
    
    input: list of the cards in the set of twelve cards
    output: all possible combinations of three cards in this set of twelve cards.

    """
    possibilities = []
    for i in range(12):
        combination = [set_of_twelve[i]]
        for j in range(i+1,12):
            combination.append(set_of_twelve[j])
            for k in range(j+1,12):
                combination.append(set_of_twelve[k])
                if combination not in possibilities and len(combination)==3:
                    possibilities.append(copy.copy(combination))
                    combination.pop()
            combination.pop()
    return possibilities

def find_allsets(set_of_twelve: list):
    """
    This function finds al Sets in ta set of twelve cards.
    Input: list of twelve cards
    Output: If there is at least one Set, this function returns a list of all Sets (list of lists with the indices 
            of the cards that form a Set).
            If there isn't any Set in this set of twelve cards, the function
            returns False.   
    """
    allsets=[]
    Possible_combinations = possible_combinations(set_of_twelve)
    for combination in Possible_combinations:
        card1 = combination[0]
        card2 = combination[1]
        card3 = combination[2]
        if card1.is_set(card2, card3):
            allsets.append(combination)
    return allsets

def find_set(set_of_twelve: list):
    """
    This function finds a Set in a set of twelve cards.
    
    Input: list of twelve cards
    Output: If there is a Set, this function returns a list with the indices 
            of the cards that form a Set.
            If there isn't any Set in this set of twelve cards, the function
            returns False.
    """
    if find_allsets(set_of_twelve)==[]:
        return False
    else:
        return find_allsets(set_of_twelve) 

def unit_tests():
    """Unit Tests: worden alleen geprint indien returnvalue onjuist is""" 
    #is_set, expected: True 
    kaart1, kaart2, kaart3=Card(0,1,2,1), Card(0,2,3,3), Card(0,3,1,4)
    kaart4, kaart5, kaart6=Card(1,0,2,1), Card(2,0,3,3), Card(3,0,1,4)
    kaart7, kaart8, kaart9=Card(1,2,0,1), Card(2,3,0,3), Card(3,1,0,4)
    kaart10, kaart11, kaart12=Card(1,2,1,0), Card(2,3,3,0), Card(3,1,4,0)
    
    if kaart1.is_set(kaart2,kaart3)==False:
        print("Unit test 1: "+str(kaart1)+","+str(kaart2)+","+str(kaart3)+" "+ "Expected: True, return Falue:"+str(kaart1.is_set(kaart2,kaart3)))
    if kaart4.is_set(kaart5,kaart6)==False:
        print("Unit test 2: "+str(kaart4)+","+str(kaart5)+","+str(kaart6)+" "+ "Expected: True, return Falue:"+str(kaart4.is_set(kaart5,kaart6)))
    if kaart7.is_set(kaart8,kaart9)==False:
        print("Unit test 3: "+str(kaart7)+","+str(kaart8)+","+str(kaart9)+" "+ "Expected: True, return Falue:"+str(kaart7.is_set(kaart8,kaart9)))
    if kaart10.is_set(kaart11,kaart12)==False:
        print("Unit test 4: "+str(kaart10)+","+str(kaart11)+","+str(kaart12)+" "+ "Expected: True, return Falue:"+str(kaart10.is_set(kaart11,kaart12)))      
    
    #is_set, expected: False 
    kaart13, kaart14, kaart15=Card(1,1,2,1), Card(0,2,2,3), Card(0,1,1,3)
    kaart16, kaart17, kaart18=Card(2,1,3,3), Card(2,1,1,2), Card(1,2,1,2)
    kaart19, kaart20, kaart21=Card(3,2,1,1), Card(2,3,3,3), Card(3,3,1,1)
    
    if kaart13.is_set(kaart14,kaart15)==True:
        print("Unit test: "+str(kaart13)+","+str(kaart14)+","+str(kaart15)+" "+ "Expected: False, return Falue:"+str(kaart13.is_set(kaart14,kaart15)))
    if kaart16.is_set(kaart17,kaart18)==True:
        print("Unit test: "+str(kaart16)+","+str(kaart17)+","+str(kaart18)+" "+ "Expected: False, return Falue:"+str(kaart16.is_set(kaart17,kaart18)))
    if kaart19.is_set(kaart20,kaart21)==True:
        print("Unit test: "+str(kaart19)+","+str(kaart20)+","+str(kaart21)+" "+ "Expected: False, return Falue:"+str(kaart19.is_set(kaart20,kaart21)))
unit_tests()




    game=Game()
    print(game)
    starttime=time.time()
    while time.time()-starttime<10:
        index1,index2,index3=inputcontrol()
        card1,card2,card3=game.set_of_twelve[index1],game.set_of_twelve[index2],game.set_of_twelve[index3]
        if card1.is_set(card2,card3):
            return "Gelukt"
        else:
            return "Helaas1"
    return "Helaas2"

print(mainprogram())

    