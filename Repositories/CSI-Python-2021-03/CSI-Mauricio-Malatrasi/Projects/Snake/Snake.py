import pygame #imports pygame
import time     #imports time
import random   #imports random

pygame.init()   #starts game

#Colors RGB, Red Green Blue
white = (255, 255, 255) #white color
black=(0,0,0)  #black color
red=(213, 50, 80)   #red color
blue=(50, 153, 213) #blue color
green = (0, 255, 0) #green color
yellow = (255, 255, 102) #yellow color

dis_width = 600     #width
dis_height  = 400   #height

dis=pygame.display.set_mode((dis_width, dis_height))  #Dimensions
pygame.display.set_caption('Snake game by Edureka') #Displays the name of the game

clock = pygame.time.Clock()     #Clock for the game

snake_block=10      #Shows the snake
snake_speed=15      #speed of the snake

font_style = pygame.font.SysFont("bahnschrift", 25) #Font size for the game
score_font = pygame.font.SysFont("comicsansms", 35)


def Your_score(score):  #Defines your_score
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):     #Defines our_snake
    for x in snake_list:                    #Draws every block in the snake, everytime you eat the food.
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])


def message(msg,color):         #Defines message
    mesg = font_style.render(msg, True, color) #Sets the style, with the height/width of the message.
    dis.blit(mesg, [dis_width/6, dis_height/3])


def gameLoop():     #Creates a function
    game_over=False #Tells you the game isn't over
    game_close=False #Tells the game to not close unless you press Q

    x1 = dis_width/2
    y1 = dis_height/2

    x1_change = 0       #Stores the change in the snake in x
    y1_change = 0       #Stores the change in the snake in y

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0   #Imports the food in a random manner in x
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0   #Imports the food in a random manner in y
    
    while not game_over:    #Start loops
        
        while game_close == True:
            dis.fill(blue) #full blue background
            message("You Lost! Press Q-Quit or C-Play Again", red)  #Shows you a message and lets you try again or quit
            Your_score(Length_of_snake - 1)
            pygame.display.update() #Updates the game

            for event in pygame.event.get():    #Makes "Q" for quitting the game and "C" to try again
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get(): 
            if event.type==pygame.QUIT:
                game_over=True  #If the game quits, game over = true
            if event.type == pygame.KEYDOWN: #Makes the movement of the snake
                if event.key == pygame.K_LEFT: #Left
                    x1_change = -10
                    y1_change = 0
                elif event.key == pygame.K_RIGHT: #Right
                    x1_change = 10
                    y1_change = 0
                elif event.key == pygame.K_UP: #Up
                    y1_change = -10
                    x1_change = 0
                elif event.key == pygame.K_DOWN: #Down
                    y1_change = 10
                    x1_change = 0
    
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:     #Makes it so if you do those things, it makes game_over true.
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)    #full blue background
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])   #Draws the food
        snake_Head = []     #Opens an empty list
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        pygame.display.update() #Updates the game

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)  #Makes a clock

    pygame.quit()   #quits the game
    quit()  #quits everything


gameLoop()