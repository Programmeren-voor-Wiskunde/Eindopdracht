# -*- coding: utf-8 -*-
from Class.py import Card
import random



class Game(Card):
    """
    Represents a round of the game Set
    
    Attributes: set_of_twelve, deck
    Methods: init
    Functions: update_set_of_twelve
    """
    def __init__(self,deck: list,set_of_twelve: list):
        """
        This function creates an object representing an round of the game Set.
        Input: -
        Output: game: Game
        """
        deck = []
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    for l in range(3):
                        deck.append(Card(i,j,k,l))
        random.shuffle(deck)
        self.deck=deck

        set_of_twelve = []
        for i in range(12):
            set_of_twelve.append(str(self.deck[0]))
            del deck[0]
        self.set_of_twelve=set_of_twelve
        
    def update_set_of_twelve(self,indices):
        """
        Updates the cards at the table if necessary and thereby remove this cards from the deck
        
        Input: game, indices: list of cards in the set_of_twelve which has to be renewed.
        Output: none
        Changed attributes: self.deck, self.set_of_twelve
        """
        for i in indices:
            self.set_of_twelve[i]=self.deck[0]
            del self.deck[0]
    
    