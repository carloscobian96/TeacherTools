import pygame
import time
import random

#Begin pygame, which has been imported beforehand
pygame.init()

#Colors are defined with the use of variables
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#The distance of the width and the height are set as fixed integers
dis_width = 600
dis_height = 400

#Window size is set thanks to the use of the variable dis as well as the previously defined dis_width and dis_height
dis = pygame.display.set_mode((dis_width, dis_height))

#The snake game caption is set
pygame.display.set_caption('Snake Game by Edureka')

#The game's clock is created in order to track the time that has passed
clock = pygame.time.Clock()

#The size of the snake's block is set as a fixed integer
snake_block = 10

#The snake's speed is set as a fixed integer
snake_speed = 15

#Font styles ate set for any words that pop in the screen such as "Yummy" and for the score
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#A function called Your_score is created with the purpose to update the player's score throughout the game
def Your_score(score):

    #Value is defined as the score font's rendering as well as the score itself
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

#A function called our_snake is created which includes the snake_list and the snake's block
def our_snake(snake_block, snake_list):

    #This represents for each block
    for x in snake_list:

        #Each block is moved to the next block or to the previous
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
#A function called message is defined 
def message(msg, color):

    #The message's font style and color is rendered, as well as its dimensions
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
#The function gameLoop is created, with the purpose to loop the game once it ends
def gameLoop():

    #Two new variables are created, game_over and game_close, both defined as false
    game_over = False
    game_close = False
    
    #The x1 and y1 coordinate values are defined as the halves of the previously defined dis_width and dis_height
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    #The x1_change and y1_change variables are created that continuously update the snake's location
    x1_change = 0
    y1_change = 0
    
    #The snake list is created
    snake_List = []

    #the length of the snake is defined as a fixed integer
    Length_of_snake = 1
    
    #Food locations are added as variables, one for each axis; they are randomly generated. 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
    
    #A while loop using the variable game_over is created
    while not game_over:
        
        #A while loop within a while loop is created, this time with the variable game_close, which details what happens if the game is closed
        while game_close == True:

            #The backround will become blue
            dis.fill(blue)

            #The previously created message function is used to print "You lost" in red
            message("You Lost! Press C-Play Again or Q-Quit", red)

            #The display is updated
            pygame.display.update()

            #The purpose of this line of code is to check the current events and renew the locations with the use of if logic
            for event in pygame.event.get():

                #In the following block, the letters pressed will be checked
                if event.type == pygame.KEYDOWN:

                    #If the letter "q" is pressed, then the game will close
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False

                    #If the letter "c" is pressed, then the game will continue and the game loop will take effect
                    if event.key == pygame.K_c:
                        gameLoop()

        #The purpose of this line of code is to check the current events and renew the locations with the use of keys and for logic
        for event in pygame.event.get():

            #Using if logic, in an event where the user hits the X, the game will close
            if event.type == pygame.QUIT:
                game_over = True
            
            #The following block of code used if logic for every possible event where a key is selected
            if event.type == pygame.KEYDOWN:

                #When the left key is pressed, the snake will move -10 coordinates to the left
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                
                #When the right key is pressed, the snake will move +10 coordinates to the right
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0

                #When the up key is pressed, the snake will move -10 coordinates upwards
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0

                #When the down key is pressed, the snake will move +10 coordinates downwards
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        #Everytime that the height and width's borders are exceeded, game_close will take effect
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        
        #Coordinate values are created in order to change coordinates of the snake head, as well as its coloration. 
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        #A rectangle is drawn with the use of previous variables
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        #The snake's head is defined as an empty list
        snake_Head = []

        #The x1 and y1 axes are appended to the snake head
        snake_Head.append(x1)
        snake_Head.append(y1)

        #The snake head, along with its location, is appended to the empty snake list
        snake_List.append(snake_Head)

        #The first object on the snake list is deleted
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        #If the body crosses the snake head, game_close will take effect and the user will lose
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        #The our_snake function is used in order to update the snake's blocks and list locations 
        our_snake(snake_block, snake_List)
 
        #The display is updated
        pygame.display.update()

        #If the snake passes over the food locations on either axis, "Yummy" will be printed
        if x1 == foodx and y1 == foody:

            #New food is randomly generated after being consumed by the snake
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            #After the snake consumes the food, its length will increase by 1
            Length_of_snake += 1

        #The clock ticks at the snake's movement speed
        clock.tick(snake_speed)
    
    #All current windows quit
    pygame.quit()

    #The entirety of pygames is quit
    quit()

#The gameLoop function takes effect, and the game's code resets
gameLoop()