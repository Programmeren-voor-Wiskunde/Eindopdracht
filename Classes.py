# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:44:02 2021

@author: Jelger
"""

import random



class Card:
    """
    Represents a cart of the game Set

    Attributes
    ----------
    color, number, filling, shape
    
    Methods
    -------
    init, str, ne(!=), eq(==)
    
    Functions
    ---------
    is_set, file_name
    """
    
    def __init__(self, color = 0, number = 0, filling = 0, shape = 0): 
        self.color = color
        self.number = number
        self.filling = filling
        self.shape = shape
        
    def __str__(self):
        return("("+str(self.color)+","+str(self.number)+","+str(self.filling)+","+str(self.shape)+")")
    
    def __ne__(self, other):
        if self.color != other.color or self.number != other.number or (
                self.filling != other.filling or self.shape != other.shape):
                return True
        else:
            return False
    
    def __eq__(self, other):
        if self.color == other.color and self.number == other.number and (
                self.filling == other.filling and self.shape == other.shape):
                return True
        else:
            return False
        
    def is_set(self, other1, other2):
        """
        Returns wether three given cards are a set or not

        Parameters
        ----------
        self : TYPE, Card
        other1 :
            DESCRIPTION. Should be of TYPE Card.
        other2 :
            DESCRIPTION. Should be of TYPE Card.

        Returns
        -------
        TYPE: Boolean
            DESCRIPTION. Returns True if cards form a set, returns False otherwise.
        """

        if self == Card(4,4,4,4) or other1 == Card(4,4,4,4) or other2 == Card(4,4,4,4): #black cards used in the end of the game, have the function of "empty spaces"
            return False 
        else:    
            #in the dictionary, a key (property of the SET cards) gets the value True if all three SET cards have the same value, or all three cards have different values for this property
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
        
        Parameters
        ----------
        self : TYPE, Card
        
        Returns
        -------
        file_name : TYPE, str
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
    
    Attributes
    ----------
    set_of_twelve, deck, difficulty, language
    
    Methods
    -------
    init, str
    
    Functions
    ---------
    update_set_of_twelve
    """
    
    def __init__(self, difficulty = 1, language = 'English'):
        """
        Parameters
        ----------
        self : TYPE, Game
        
        difficulty : TYPE, optional
            DESCRIPTION. Should be of TYPE int. The default is 1.
        language : TYPE, optional
            DESCRIPTION. Should be of TYPE str. The default is 'English'.

        Returns
        -------
        None.

        """

        self.difficulty = difficulty
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
            
        self.language = language
        
    def __str__(self):
        return("Cards on the table:\n"+str(self.set_of_twelve[0])+str(self.set_of_twelve[1])+str(self.set_of_twelve[2])+str(self.set_of_twelve[3])+"\n"+str(self.set_of_twelve[4])+str(self.set_of_twelve[5])+str(self.set_of_twelve[6])+str(self.set_of_twelve[7])+"\n"+str(self.set_of_twelve[8])+str(self.set_of_twelve[9])+str(self.set_of_twelve[10])+str(self.set_of_twelve[11])+"\n"+"Aantal kaarten op de stapel:"+str(len(self.deck)))
        
    def update_set_of_twelve(self, set_indices):
        """
        Removes the last three elements of self.deck and replaces indicated cards of self.set_of_twelve with these new three cards.
        
        Parameters
        ----------
        self : TYPE, Game
        set_indices :
            DESCRIPTION. Should be of TYPE list, with elements of TYPE int. This are the indices of the cards to be replaced.

        Returns
        -------
        None.
        
        Changed attributes
        ------------------
        deck, set_of_twelve
        """
        
        for i in set_indices:
            if self.deck == []: #in the end cards are replaced by black cards, which have the function of empty spaces.
                self.set_of_twelve[i] = Card(4,4,4,4)  
            else:
                self.set_of_twelve[i] = self.deck[-1]
                del self.deck[-1]