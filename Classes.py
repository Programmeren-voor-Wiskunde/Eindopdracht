# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:44:02 2021

@author: Jelger
"""

import pygame
import sys
import random
import copy
import time





class Card:
    """Represents a cart of the game Set"
    
    Attributes: color, number, filling, shape.
    Methods: init, str
    Functions: is_set, file_name"""
    
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

    def file_name(self):
        """ 
        Given a card, this method returns the name of the associated image file of the card.
        
        Input: Card object
        Output: name of the image file of the card; string
        """
        
        # initialise file_name
        file_name = ""
        
        # add attribute color to file_name
        if self.color == 0:
            file_name += "green"
        elif self.color == 1:
            file_name += "purple"
        elif self.color == 2:
            file_name += "red"
            
        # add attribute shape to file_name
        if self.shape == 0:
            file_name += "diamond"
        elif self.shape == 1:
            file_name += "oval"
        elif self.shape == 2:
            file_name += "squiggle"
        
        # add attribute filling to file_name
        if self.filling == 0:
            file_name += "empty"
        elif self.filling == 1:
            file_name += "filled"
        elif self.filling == 2:
            file_name += "shaded"
        
        # add attribute number to file_name
        file_name += str(self.number+1)
        
        # add necessary image type
        file_name += ".gif"
        
        return file_name
    
    
    


class Game:
    """
    Represents a round of the game Set
    
    Attributes: set_of_twelve, deck(, language)
    Methods: init, str
    Functions: update_set_of_twelve
    """
    def __init__(self):
        """
        This function creates an object representing an round of the game Set.
        Input: -
        Output: game: Game
        """
        self.difficulty=10
        self.deck = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        self.deck.append(Card(i,j,k,l))
        random.shuffle(self.deck)

        self.set_of_twelve = []
        for i in range(12):
            self.set_of_twelve.append(self.deck[-1])
            del self.deck[-1]
            
        self.language = 'English'
        
    def __str__(self):
        return("Cards on the table:\n"+str(self.set_of_twelve[0])+str(self.set_of_twelve[1])+str(self.set_of_twelve[2])+str(self.set_of_twelve[3])+"\n"+str(self.set_of_twelve[4])+str(self.set_of_twelve[5])+str(self.set_of_twelve[6])+str(self.set_of_twelve[7])+"\n"+str(self.set_of_twelve[8])+str(self.set_of_twelve[9])+str(self.set_of_twelve[10])+str(self.set_of_twelve[11])+"\n"+"Aantal kaarten op de stapel:"+str(len(self.deck)))
        
    def update_set_of_twelve(self, set_indices):
        """
        Removes the last three elements of self.deck and replaces indicated cards of self.set_of_twelve with these new three cards.
        
        Input: game, set_indices: list of cards in the set_of_twelve which have to be renewed.
        Output: None
        Changed attributes: self.deck, self.set_of_twelve
        
        """
        for i in set_indices:
            if len(self.deck) != 0:
                self.set_of_twelve[i] = self.deck[-1]
                del self.deck[-1]
            else:
                self.set_of_twelve[i] = "black"
                
