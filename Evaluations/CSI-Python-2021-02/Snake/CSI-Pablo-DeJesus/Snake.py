import pygame
pygame.init() #initializes the code
dis=pygame.display.set_mode((400,300))
pygame.display.update() #updates the changes made to screen
pygame.display.set_caption('Snake game by Pablo De Jota') #prints message at start of game in pygame screen
game_over=False #continues game
while not game_over:
    for event in pygame.event.get(): 
        print(event) #the last three lines use the input of player to determine what is printed on the screen
pygame.quit()
quit() #uninitializes the code
#this code opens the python game screen