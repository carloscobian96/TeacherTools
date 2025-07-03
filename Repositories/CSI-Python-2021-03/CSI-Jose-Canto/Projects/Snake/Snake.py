# import pygame       #Imports the gane
# pygame.init()       #Starts the game
# dis=pygame.display.set_mode((400,300))      #creates the display

# pygame.display.update()     #Updates the display

# pygame.display.set_caption('Snake game by Canto')     #Adds to the display

# black=(0,0,0)       #Makes the original blue into black
# red=(255,0,0)       #Sets the color

# game_over=False         #If the game is over the gfame will end, if not it will continue
# while not game_over:
#     for event in pygame.event.get():    
#         if event.type==pygame.QUIT:
#             game_over=True              #if the game is over the game will quit
#         pygame.draw.rect(dis,black,[200,150,10,10])  #displays the blue rectangle
#     pygame.display.update()     #Updates display
 
# pygame.quit()       #Depending on "game_over" the game will end
# quit()          #The game will quit

import pygame   #imports the game
import time     #imports time
import random   #imports random
 
pygame.init()      #Starts game
 
white = (255, 255, 255)     #Colors
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 600     #sets the size 
dis_height  = 400 

dis = pygame.display.set_mode((dis_width, dis_height))       #sets the display's mode
pygame.display.set_caption('Snake Game by Canto')     #Adds to the display

clock = pygame.time.Clock()
 
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):      #Creates a score for the user
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])
 
def gameLoop():  # creating a function
    game_over = False       #Keeps the game from stopping
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close == True:       #Once the game is over the rest of the string will run
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:    
                    if event.key == pygame.K_q: 
                        game_over = True        
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()                  #Re-starts the game
 
        for event in pygame.event.get():        #Sets the controls for the game using the arrows
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0


            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_over = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block])       #Draws the snake food
            snake_Head = []
            snake_Head.append(x1)       #adds a block to the head 
            snake_Head.append(y1)       #adds a block to the head
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                    del snake_List[0]
        
            for x in snake_List[:-1]:
                if x == snake_Head:
                        game_close = True
    
            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1) #the score will be the length of the snake minus 1
    
            pygame.display.update()
    
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0       
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1        #adds length to the snake

            clock.tick(snake_speed)
 
        pygame.quit()
        quit()

gameLoop()