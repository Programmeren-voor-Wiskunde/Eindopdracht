# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 14:05:11 2021

@author: Jelger
"""
import pygame,sys

pygame.init()


clock=pygame.time.Clock()
screen = pygame.display.set_mode((400,650), pygame.RESIZABLE)
font = pygame.font.SysFont(None,32)
menu1_input=''
menu2_input=''

input_rect = pygame.Rect(200,200,140, 32)
color = pygame.Color('lightskyblue3')

menu1,menu2 = True, True
while menu1 == True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                menu1_input = menu1_input[:-1]
            elif event.key == pygame.K_RETURN:
                player_name=menu1_input
                menu1 = False
                break
            else:
                menu1_input+=event.unicode
            
            
    screen.fill((0,0,0))
  
    text_surface1=font.render("Onder welke naam wilt u spelen?",True,(255,255,255))
    screen.blit(text_surface1,(input_rect.x,input_rect.y - 30))  
  
    pygame.draw.rect(screen,color,input_rect, 2)
    text_surface2=font.render(menu1_input,True,(255,255,255))
    screen.blit(text_surface2,(input_rect.x+5,input_rect.y + 5))
    
    pygame.display.update()
    clock.tick(30)
    
while menu2 == True:
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                menu2_input = menu2_input[:-1]
            elif event.key == pygame.K_RETURN:
                difficulty=menu2_input
                menu2=False
            else:
                menu2_input+=event.unicode
            
            
    screen.fill((0,0,0))
  
    text_surface1=font.render("Onder welke naam wilt u spelen?",True,(255,255,255))
    screen.blit(text_surface1,(input_rect.x,input_rect.y - 30))  
  
    pygame.draw.rect(screen,color,input_rect, 2)
    text_surface2=font.render(menu1_input,True,(255,255,255))
    screen.blit(text_surface2,(input_rect.x+5,input_rect.y + 5))
  
    text_surface3=font.render("Moeilijkheidsgraad: Aantal seconden voor computer een set vindt.",True,(255,255,255))
    screen.blit(text_surface3,(input_rect.x,input_rect.y + 70))  
  
    pygame.draw.rect(screen,color,(input_rect.x,input_rect.y+ 105, 240, 32), 2)
    text_surface4=font.render(menu2_input,True,(255,255,255))
    screen.blit(text_surface4,(input_rect.x+5,input_rect.y + 110))
    
    pygame.display.update()
    clock.tick(30)
    
#screen.fill((0,0,0)) 
    