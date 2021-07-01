# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 10:43:28 2021

@author: Jelger
"""
import pygame
import copy

import Classes
Card=Classes.Card
Game=Classes.Game





def card_positions(set_of_twelve):
    """
    This function converts the index of a card in set_of_twelve to a position 
    on screen.

    Parameters
    ----------
    set_of_twelve : List containing the twelve cards that are visible on the game table.

    Returns
    -------
    positions : List of lists containing the coördinates of where every card in 
    set_of_twelve should be mapped to.

    """
    # get window size
    window_width, window_height = pygame.display.get_surface().get_size()
    
    # initialise list of positions
    positions = []
    
    # append pixel positions of cards to positions
    for i in range(len(set_of_twelve)):
        row, column = divmod(i, 4)
        row = 200*row+50
        column = (window_width//2)-200+100*column
        positions.append([row, column]) 
    return positions




    
def select_card(set_of_twelve, rect_set_of_twelve):
    """
    This function enables mouse-click selection of cards.
    
    Parameters
    ----------
    set_of_twelve : List 
        List of the cards in the set of twelve cards on the table.
    rect_set_of_twelve : list 
        List of Rectangles that are as big as the card images and that are on 
        the same spot as the card images.

    Returns
    -------
    index of mouse-clicked card or Boolean value

    """
    # get position of mouse
    mouse_position = pygame.mouse.get_pos()
    
    # determine on which card is clicked
    for i in range(len(set_of_twelve)):
        if rect_set_of_twelve[i].collidepoint(mouse_position):
            return i
    return False





def possible_combinations(set_of_twelve: list):
    """
    This function returns all the possible combinations of three different 
    indices from a list of indices, in which the order of the indices doesn't matter.

    Parameters
    ----------
    set_of_twelve : list
        List of the cards in the set of twelve cards on the table.

    Returns
    -------
    possibilities : list
        All possible combinations of three indices in a set of indices.

    """
    #initialise possibilities
    possibilities = []
    
    # append combinations to possibilities
    for i in range(len(set_of_twelve)):
        combination = [i]
        for j in range(i+1,len(set_of_twelve)):
            combination.append(j)
            for k in range(j+1,len(set_of_twelve)):
                combination.append(k)
                if combination not in possibilities and len(combination)==3:
                    possibilities.append(copy.copy(combination))
                    # prepare for a new combination
                    combination.pop()
            # prepare for a new combination
            combination.pop()
    return possibilities





def find_allsets(set_of_twelve: list):
    """
    This function finds all Sets in a set.

    Parameters
    ----------
    set_of_twelve : list
        List of the cards in the set of twelve cards on the table.

    Returns
    -------
    allsets : list/Boolean value
        If there is at least one Set, this function returns a list of all Sets 
        (list of lists with the indices of the cards that form a Set).
        If there isn't any Set in this set of twelve cards, the function
        returns False.   

    """
    # initialise allsets
    allsets=[]
    
    # determine all possible combinations of indices
    Possible_combinations = possible_combinations(set_of_twelve)
    
    # check whether a combination is a Set
    for combination in Possible_combinations:
        card1 = set_of_twelve[combination[0]]
        card2 = set_of_twelve[combination[1]]
        card3 = set_of_twelve[combination[2]]
        if card1.is_set(card2, card3) == True:
            allsets.append(combination)
    return allsets





def find_set(set_of_twelve: list):
    """
    This function finds a Set in a set.

    Parameters
    ----------
    set_of_twelve : list
        List of the cards in the set of twelve cards on the table.

    Returns
    -------
    list/Boolean value
        If there is a Set, this function returns a list with the indices 
        of the cards that form a Set.
        If there isn't any Set in this set of twelve cards, the function
        returns False.

    """
    # determines whether there is a set
    if find_allsets(set_of_twelve)==[]:
        return False
    else:
        return find_allsets(set_of_twelve)[0]