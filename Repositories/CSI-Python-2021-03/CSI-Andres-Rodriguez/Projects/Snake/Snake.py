# acces the script from another Python file
import pygame
# Allows to work with time in Python
import time
#import random
import random
 
#initiates the game
pygame.init()
 # Different RBG. RGB describes a color as a tuple of three components.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 102)
green = (0, 255, 0)
blue = (50, 153, 213)
brown = (92, 42, 42)
pink = (238, 32, 224)
purple = (135, 32, 238)
 
#The dis module includes functions for working with Python bytecode by “disassembling” it into a more human-readable form.
#width
dis_width = 600
#height
dis_height  = 400
 

#This control displays a list of items for the user to select. The items parameter must be a Python list. It can contain as many items as you wish.
# Display the width and the height of the screen in the game
dis = pygame.display.set_mode((dis_width, dis_width))
#Shows or display the name of the game (Snake Game by Edureka)
pygame.display.set_caption('Snake Game by Andrés')
 
 #time frame of the game
clock = pygame.time.Clock()
 
 #height and width of the sanke
snake_block = 10
# Speed of the sanke
snake_speed = 15
 
 #font stryle and size for the game over and the score
font_style = pygame.font.SysFont("bahnschrift", 35)
score_font = pygame.font.SysFont("comicsansms", 25)
 
 # define the function of the score and the value of the score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 #define the snake 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 #defie the parameters of the function and of the message. Also define the position of the , message
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width /6, dis_height / 3])
 
 # define teh game loop
def gameLoop():
    game_over = False
    game_close = False
 
    # width of the sanke divided by 2
    x1 = dis_width/2
# height of the sanke divided by 2
    y1 = dis_height/2
 
 #values of the change in direction
    x1_change = 0
    y1_change = 0
 
 # define the size of the snake
    snake_List = []
    Length_of_snake = 1
 
 # define the position of the food in the x axis and the y axis
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 # define the message if the game is over
        while game_close == True:
            #while playing the game the background is going to be blue
            dis.fill(blue)
            #if you loose change the background red and put the message "you lost"
            message("You Lost! Press C-Play Again or Q-Quit", white)
            #you're score depends on every food you eat
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
 #define what key you have to press to touch if you want to start again or if you want to quit
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #press q to quit the game when you lose
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    #press c if you want to start again
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
            #it will do a variable name "game over" that has a value of true
                game_over = True
            if event.type == pygame.KEYDOWN:
            #It moves the snake to the left by changing the x axis and making it negative.
                if event.key == pygame.K_LEFT:
                    #the x axis is negative
                    x1_change = -snake_block
                    #the y axis is 0
                    y1_change = 0
                #It moves the snake to the right by changing the x axis and making it positive. 
                elif event.key == pygame.K_RIGHT:
                    #the x axis is positive
                    x1_change = snake_block
                    #the y axis is 0
                    y1_change = 0
                #It moves the snake up by changing the y axis and making it positive.
                elif event.key == pygame.K_UP:
                    #the y axis is positive
                    y1_change = -snake_block
                    #the x axis is 0
                    x1_change = 0
                #It moves the snake down by changing the y axis and making it negative.
                elif event.key == pygame.K_DOWN:
                    # the y axis is negative
                    y1_change = snake_block
                    #the x axis is 0
                    x1_change = 0
 
 
 #define the limits of boundaries of the game
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            #if you touched the boundaries you loose
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        #draw the food
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        #define the stucture of the snake
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
 #if the snake touch itself the game is over
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
 # function of the score
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
 #if the snake find the food and eat it then it will sum 1
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 #defined the speed of the snake
        clock.tick(snake_speed)
 
 #finsished the game
    pygame.quit()
    quit()
 
 #start again
gameLoop()


