#Visualise
# import the pygame module, so you can use it
import pygame
import sys
import time

import Classes
Card=Classes.Card
Game=Classes.Game

import Functions
card_positions = Functions.card_positions
#visualise_set_of_twelve = Functions.visualise_set_of_twelve
select_card = Functions.select_card
possible_combinations = Functions.possible_combinations
find_allsets = Functions.find_allsets
find_set = Functions.find_set

import Unittests





# define the RGB value for certain colors
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)
red = (220, 0, 0)
black = (0,0,0)
grey = (200,200,200)



#creates a new game
game = Game()
print(game)

# initialize the pygame module
pygame.init()
game.roundtime=time.time()

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

# create a surface on screen that has the size of 400 x 650 pixels
screen = pygame.display.set_mode((400,650), pygame.RESIZABLE)

# import font
font = pygame.font.SysFont(None, 30)

# initialise selected_cards
selected_cards = []

# creates grid to enable card selection by mouse clicking
rect_set_of_twelve = []
for i in range(len(game.set_of_twelve)):
    rect_set_of_twelve.append(
        pygame.Rect(card_positions(game.set_of_twelve)[i][1], 
                    card_positions(game.set_of_twelve)[i][0], 100, 200))

#other initalizations
pygame.display.set_caption("Set")
t0=-3
running = True


def visualise_set_of_twelve(set_of_twelve, selected_cards , not_a_set_message, 
                            overtime_message, score = (0,0), player_name = 'Player1'): 
    """
    This function displays the set of twelve cards on the table and the current score.

    Parameters
    ----------
    set_of_twelve : List containing the twelve cards that are visible on the game table.
    selected_cards : List containing up to three cards that are selected in the game. 
    not_a_set_message : Boolean value.
    overtime_message : Boolean value
    score : list with score of player and computer.
    player_name : name of the player of the game

    Returns
    -------
    None.

    """
    
    window_width, window_height = pygame.display.get_surface().get_size()
    # make a score board
    pygame.draw.rect(screen, grey, (0, 0, window_width, 50))
    
    # load player name and computer to screen
    player_name_display = font.render(player_name, True, black)
    computer_name_display = font.render("Computer", True, black)
    
    screen.blit(computer_name_display, (window_width-115,15))
    screen.blit(player_name_display, (10, 15))
    
    # load score to screen
    player_score = score[0]
    computer_score = score[1]
    score_text = str(player_score) + " - " + str(computer_score)
    score_display = font.render(score_text, True, black)
    score_display_rect = score_display.get_rect(center = (window_width//2, 25))
    screen.blit(score_display, score_display_rect)
    
    
    # initialise list of loaded images
    loaded_images = []
    
    # load image for outline
    selection_image = pygame.image.load("rode_omlijning_transparant.png")
    
    # load images of the cards in set_of_twelve
    for i in range(len(set_of_twelve)):
        loaded_images.append(pygame.image.load(set_of_twelve[i].file_name()).convert())
        
    # blit images of set_of_twelve to screen
    for i in range(len(set_of_twelve)):
        screen.blit(loaded_images[i], (card_positions(set_of_twelve)[i][1],
                                       card_positions(set_of_twelve)[i][0]))
        
    # Outlines selected card in window
    for i in selected_cards:
        screen.blit(selection_image, (card_positions(game.set_of_twelve)[i][1],
                                       card_positions(game.set_of_twelve)[i][0]))
        
    # displays error message if necessary
    if not_a_set_message:
        if game.language == 'Nederlands':
            error_message = font.render("Dat is helaas geen Set.", True, red)
            screen.blit(error_message, (90, 220))
        elif game.language == 'English':
            error_message = font.render("That is not a Set.", True, red)
            screen.blit(error_message, (110, 220))
        
        # displays error message if necessary
    if overtime_message:
        if game.language == 'Nederlands':
            error_message = font.render("Computer heeft een Set.", True, red)
            screen.blit(error_message, (100, 220))
        elif game.language == 'English':
            error_message = font.render("Computer has a Set.", True, red)
            screen.blit(error_message, (110, 220))



# initialises the screen with not_a_set_message = False and overtime_message=False
visualise_set_of_twelve(game.set_of_twelve, selected_cards, False, False)
# display loaded images on screen
pygame.display.flip()


# -------- Main Program Loop -----------

while running == True:
        
    # Limit to 10 frames per second
    clock.tick(10)
    
    # check size of screen
    window_width, window_height = pygame.display.get_surface().get_size()
    
    for event in pygame.event.get():
        # close game when you click on "Close"-button
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            # if you click on the same card twice, unselect that card.
            i = select_card(game.set_of_twelve, rect_set_of_twelve)
            if i in selected_cards:
                selected_cards.remove(i)
                # fixes a weird bug
                pygame.draw.rect(screen, black, (0,50, window_width, window_height-50))
                
            # if you click on a card, store it in selected_cards.
            else:
                selected_cards.append(i)
                # fixes a weird bug
                pygame.draw.rect(screen, black, (0,50, window_width, window_height-50))
        
    #check whether there are any sets:
    if find_allsets(game.set_of_twelve)==[]:
        game.update_set_of_twelve(1,2,3)

    #the computer wins if the player didn't found any set after a certain seconds
    if time.time()-game.roundtime>game.difficulty:
        overtime_message=True
        t0=time.time()
        print("De computer heeft deze ronde gewonnen.")
        game.update_set_of_twelve(find_set(game.set_of_twelve))
        game.roundtime = time.time()
        print(game)
        selected_cards = []

    # check whether the given combination of cards is a set and update if necessary
    if len(selected_cards)==3:
        if game.set_of_twelve[selected_cards[0]].is_set(game.set_of_twelve[selected_cards[1]],
                                                game.set_of_twelve[selected_cards[2]])==True:
            game.update_set_of_twelve(selected_cards)
            game.roundtime=time.time()
            print(game)
        else:
            not_a_set_message = True
            t0 = time.time()
            print("Dat is helaas geen Set.")
        selected_cards = []

            
    # after 3 seconds the error messages wil vanish
    if time.time()-t0>=3:
        not_a_set_message = False
        overtime_message = False
    
    #start = time.time()
    # update the screen
    visualise_set_of_twelve(game.set_of_twelve, selected_cards, not_a_set_message, overtime_message)
    pygame.display.update()
    #print(start-time.time())
        
pygame.quit()
sys.exit()      
               