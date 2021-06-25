# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:43:47 2021

@author: Levi G.R. van Lieshout & Jelger J. van Haskera
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
        return("("+str(self.color)+","+str(self.number)+","+str(self.filling)+","+str(self.shape)+")")
        
    def is_set(self,other1,other2):
        """
        This method checks whether the given cards form a Set.
        
        Input:
            self = Card object
            other1 = Card object
            other2 = Card object
        Output:
            True if the cards form a Set
            False if the cards don't form a Set
        """
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