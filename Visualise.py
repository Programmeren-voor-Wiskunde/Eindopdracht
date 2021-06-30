#Visualise
# import the pygame module, so you can use it
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
            self.set_of_twelve.append(self.deck[-1]) #heb hier str(self.deck) weggehaald
            del self.deck[-1]
        
    def __str__(self):
        return("Cards on the table:\n"+str(self.set_of_twelve[0])+str(self.set_of_twelve[1])+str(self.set_of_twelve[2])+str(self.set_of_twelve[3])+"\n"+str(self.set_of_twelve[4])+str(self.set_of_twelve[5])+str(self.set_of_twelve[6])+str(self.set_of_twelve[7])+"\n"+str(self.set_of_twelve[8])+str(self.set_of_twelve[9])+str(self.set_of_twelve[10])+str(self.set_of_twelve[11])+"\n"+"Aantal kaarten op de stapel:"+str(len(self.deck)))
        
    def update_set_of_twelve(self, set_indices):
        """
        Removes the last three elements of self.deck and replaces indicated cards of self.set_of_twelve with these new three cards.
        
        Input: game, set_indices: list of cards in the set_of_twelve which have to be renewed.
        Output: none
        Changed attributes: self.deck, self.set_of_twelve
        """
        for i in set_indices:
            self.set_of_twelve[i]=self.deck[-1]
            del self.deck[-1]






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
    # initialise list of positions
    positions = []
    # append pixel positions of cards to positions
    for i in range(len(set_of_twelve)):
        row, column = divmod(i, 4)
        row = 200*row
        column = 100*column
        positions.append([row, column]) 
    return positions


def visualise_set_of_twelve(set_of_twelve, selected_cards , not_a_set): 
    """
    This function displays the set of twelve cards on the table.

    Parameters
    ----------
    set_of_twelve : List containing the twelve cards that are visible on the game table.
    not_a_set : Boolean value.

    Returns
    -------
    None, but its effect is a window with twelve game cards.

    """
    # initialise list of loaded images
    loaded_images = []
    
    # load image for outline
    selection_image = pygame.image.load("rode_omlijning_transparant.png")
    
    # load images of the cards in set_of_twelve
    for i in range(len(set_of_twelve)):
        loaded_images.append(pygame.image.load(set_of_twelve[i].file_name()).convert())
        
    # load images of set_of_twelve to screen
    for i in range(len(set_of_twelve)):
        screen.blit(loaded_images[i], (card_positions(set_of_twelve)[i][1],
                                       card_positions(set_of_twelve)[i][0]))
        
    # Outlines selected card in window
    for i in selected_cards:
        screen.blit(selection_image, (card_positions(game.set_of_twelve)[i][1],
                                       card_positions(game.set_of_twelve)[i][0]))
        
    # displays error message if necessary
    if not_a_set:
        error_message = font.render("Dat is helaas geen Set.", True, red)
        screen.blit(error_message, (90, 170))
    
    # display loaded images on screen
    pygame.display.flip()
    
    
def select_card(set_of_twelve, rect_set_of_twelve):
    """
    This function enables mouse-click selection of cards.
    
    Parameters
    ----------
    set_of_twelve : List containing the twelve cards that are visible on the game table.
    rect_set_of_twelve : List of Rectangles that are as big as the card images
                         and that are on the same spot as the card images.

    Returns
    -------
    index of mouse-clicked card

    """
    mouse_position = pygame.mouse.get_pos()
    for i in range(len(set_of_twelve)):
        if rect_set_of_twelve[i].collidepoint(mouse_position):
            return i



    
"""
Now starting the real executioning program.

"""
    


game = Game()
print(game)

# initialize the pygame module
pygame.init()

# Used to manage how fast the screen updates
clock=pygame.time.Clock()
    
pygame.display.set_caption("Set")
    
# create a surface on screen that has the size of 400 x 600 pixels
screen = pygame.display.set_mode((400,600), pygame.RESIZABLE)

# import font
font = pygame.font.SysFont(None, 30)

    
rect_set_of_twelve = []
for i in range(len(game.set_of_twelve)):
    rect_set_of_twelve.append(
        pygame.Rect(card_positions(game.set_of_twelve)[i][1], 
                    card_positions(game.set_of_twelve)[i][0], 100, 200))

# initialise selected_cards
selected_cards = []

# define the RGB value for certain colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (220, 0, 0)
black = (0,0,0)

not_a_set = False
t0=-3
running = True

# -------- Main Program Loop -----------
while running == True:
    visualise_set_of_twelve(game.set_of_twelve, selected_cards, not_a_set)
    
    # Limit to 10 frames per second
    clock.tick(10)
    
    
    for event in pygame.event.get():
        # closes game when you click on "Close"-button
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            # if you click on the same card twice, then it will unselect.
            i = select_card(game.set_of_twelve, rect_set_of_twelve)
            if i in selected_cards:
                selected_cards.remove(i)
                
            # if you click on a card, it will be stored in the selected cards.
            else:
                selected_cards.append(i)
            print(i)
        

    # checks whether the given combination of cards is a set and updates if necessary
    if len(selected_cards)==3:
        if game.set_of_twelve[selected_cards[0]].is_set(game.set_of_twelve[selected_cards[1]],
                                                game.set_of_twelve[selected_cards[2]])==True:
            game.update_set_of_twelve(selected_cards)
            print(game)
        else:
            not_a_set = True
            t0 = time.time()
            print("Dat is helaas geen Set.")
        selected_cards = []
        
    # removes outlines from cards when there aren't anymore selected cards
    if len(selected_cards) == 0:
        for i in range(12):
            pygame.draw.rect(screen, black, (card_positions(game.set_of_twelve)[i][1], 
                        card_positions(game.set_of_twelve)[i][0], 100, 200), 3)
            
    # after 3 seconds the error message wil vanish
    if time.time()-t0>=3:
        not_a_set = False
        
pygame.quit()
sys.exit()            
                


    


"""
# load and set the logo
greendiamondempty1 = pygame.image.load("greendiamondempty1.gif")
pygame.display.set_icon(greendiamondempty1)
"""