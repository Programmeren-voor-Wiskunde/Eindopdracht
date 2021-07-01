#Visualise
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



# define the RGB value for certain colors
white = (255, 255, 255)
green = (0, 255, 0)
dark_green = (0, 80, 0)
blue = (0, 0, 128)
red = (220, 0, 0)
black = (0,0,0)
grey = (200,200,200)



#creates a new game
game = Game()
print(game)
game.difficulty = 1
game.language = "Nederlands"

# initialize the pygame module
pygame.init()

# used to count how much seconds have passed since a Set was found.
game.roundtime=time.time()

# Used to manage how fast the screen updates
clock=pygame.time.Clock()

# create a surface on screen that has the size of 400 x 650 pixels
screen = pygame.display.set_mode((400,650), pygame.RESIZABLE)

# import font, used to display text in game 
font = pygame.font.SysFont(None, 30)

# initialise selected_cards
selected_cards = []

# initialise score
score = [0,0]

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
display_result_screen = False
not_a_set_message = False
overtime_message = False


def visualise_set_of_twelve(set_of_twelve, selected_cards , not_a_set_message, 
                            overtime_message, score = [0,0], player_name = 'Player1'): 
    """
    This function loads the set of twelve cards on the table and the current score
    to the screen.

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
    # create a score board
    pygame.draw.rect(screen, grey, (0, 0, window_width, 50))
    
    # create a dark green background
    pygame.draw.rect(screen, dark_green, (0,50, window_width, window_height-50))
    
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
        if set_of_twelve[i] != Card(4,4,4,4):
            loaded_images.append(pygame.image.load(set_of_twelve[i].file_name()).convert())
        else:
            loaded_images.append(pygame.image.load('zwarte_kaart.png').convert())
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
            screen.blit(error_message, ((window_width//2)-110, 220))
        elif game.language == 'English':
            error_message = font.render("That is not a Set.", True, red)
            screen.blit(error_message, ((window_width//2)-90, 220))
        
        # displays error message if necessary
    if overtime_message:
        if game.language == 'Nederlands':
            error_message = font.render("Computer heeft een Set.", True, red)
            screen.blit(error_message, ((window_width//2)-114, 60))
        elif game.language == 'English':
            error_message = font.render("Computer has a Set.", True, red)
            screen.blit(error_message, ((window_width//2)-97, 60))


def result_screen(score, language, player_name = "Player1"):
    """
    This function

    Parameters
    ----------
    score : TYPE
        DESCRIPTION.
    language : TYPE
        DESCRIPTION.
    player_name : TYPE, optional
        DESCRIPTION. The default is "Player1".

    Returns
    -------
    None.

    """
    window_width, window_height = pygame.display.get_surface().get_size()
    
    # load text to screen
    if language == "Nederlands":
        cause_game_stop = font.render("Geen Sets meer mogelijk", True, white)
    elif language == "English":
        cause_game_stop = font.render("No more Sets possible", True, white)
    cause_game_stop_rect = cause_game_stop.get_rect(center = (window_width//2, 20))
    
    
    # load score to screen
    player_score = score[0]
    computer_score = score[1]
    score_text = str(player_name) + "  " + str(player_score
                            ) + " - " + str(computer_score) + "  " + "Computer"
    score_display = font.render(score_text, True, white)
    score_display_rect = score_display.get_rect(center = (window_width//2, 
                                                          (window_height//2)+50))
    
    
    # determines who won the game
    if player_score > computer_score:
        # load green background to screen
        screen.fill(green)
        # load winning message to screen
        if language == "Nederlands":
            win = font.render("Gefeliciteerd, je hebt gewonnen!", True, white)
        elif language == "English":
            win = font.render("Congratulations, you've won!", True, white)
        win_rect = win.get_rect(center = (window_width//2, window_height//2))
        screen.blit(win, win_rect)
        screen.blit(score_display, score_display_rect)
        screen.blit(cause_game_stop, cause_game_stop_rect)
    elif computer_score>player_score:
        # load red background to screen
        screen.fill(red)
        # load losing message to screen
        if language == "Nederlands":
            lose = font.render("Helaas, volgende keer beter!", True, white)
        elif language == "English":
            lose = font.render("Better luck next time!", True, white)
        lose_rect = lose.get_rect(center = (window_width//2, window_height//2))
        screen.blit(lose, lose_rect)
        screen.blit(score_display, score_display_rect)
        screen.blit(cause_game_stop, cause_game_stop_rect)
    else:
        # load black background to screen
        screen.fill(black)
        # load tie message to screen
        if language == "Nederlands":
            tie = font.render("Gelijkspel", True, white)
        elif language == "English":
            tie = font.render("Tie", True, white)
        tie_rect = tie.get_rect(center = (window_width//2, window_height//2))
        screen.blit(tie, tie_rect)
        screen.blit(score_display, score_display_rect)
        screen.blit(cause_game_stop, cause_game_stop_rect)
    



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
        
    # check whether there are any sets
    any_sets_left = True
    while find_allsets(game.set_of_twelve) == [] and any_sets_left:
        # load result_screen to screen
        if game.deck == []:
            display_result_screen = True 
            any_sets_left = False
            
        # replace the first three cards with three cards of the game.deck
        else:
            game.update_set_of_twelve([1,2,3])
    

    # the computer selects a set if the player didn't found any set after a 
    # certain amount of seconds and the result screen shouldn't be displayed
    if time.time()-game.roundtime>game.difficulty and any_sets_left:
        overtime_message=True
        t0=time.time()
        print("De computer heeft een Set gevonden.")
        score[1]+=1
        game.update_set_of_twelve(find_set(game.set_of_twelve))
        game.roundtime = time.time()
        print(game)
        selected_cards = []

    # check whether the given combination of cards is a set and update if necessary
    if len(selected_cards)==3:
        if game.set_of_twelve[selected_cards[0]].is_set(game.set_of_twelve[selected_cards[1]],
                                                game.set_of_twelve[selected_cards[2]])==True:
            score[0]+=1
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
    if display_result_screen == True:
        result_screen(score, game.language)
    else:
        visualise_set_of_twelve(game.set_of_twelve, selected_cards, not_a_set_message, 
                            overtime_message, score)
    pygame.display.update()
    #print(start-time.time())
        
pygame.quit()
sys.exit()      
                