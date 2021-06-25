#Visualise
import pygame
import sys
import random

class Card:
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
    
def visualise_set_of_twelve(set_of_twelve):
    # initialize the pygame module
    pygame.init()
        
    # initialise list of loaded images
    loaded_images = []
    
    # load images of the cards in set_of_twelve
    for i in range(len(set_of_twelve)):
        print(set_of_twelve[i].file_name())
        loaded_images.append(pygame.image.load(set_of_twelve[i].file_name()))
    
    pygame.display.set_caption("Set")
     
    # create a surface on screen that has the size of 400 x 600 pixels
    screen = pygame.display.set_mode((400,600))
    
    # convert index in set_of_twelve to position on screen
    # initialise list of positions
    positions = []
    # append pixel positions of cards to positions
    for i in range(len(set_of_twelve)):
        row, column = divmod(i, 4)
        row = 200*row
        column = 100*column
        positions.append([row, column])
        
    # load images of set_of_twelve to screen
    for i in range(len(set_of_twelve)):
        screen.blit(loaded_images[i], (positions[i][1],positions[i][0]))
    
    # display loaded images on screen
    pygame.display.flip()

    # closes game when you click on "Close"-button
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
#visualise_set_of_twelve(set_of_twelve)