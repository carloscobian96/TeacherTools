import pygame

import time

import random

    #Begins the game
pygame.init()

    #Varaibles assigned for each color used in the snake game

white = (255, 255, 255)

yellow = (255, 255, 102)

black = (0, 0, 0)

red = (213, 50, 80)

green = (0, 255, 0)

blue = (50, 153, 213)

    #The distance of the width and the height are set as fixed integers

dis_width = 600

dis_height = 400

    #Window size is displayed with height and width variables

dis = pygame.display.set_mode((dis_width, dis_height))

    #The snake game caption is set

pygame.display.set_caption('Snake Game by Edureka')

    #Clock that shows how much time has passed assigned in a variable

clock = pygame.time.Clock()

    #The size of the snake's block is set as a fixed integer

snake_block = 10

    #The snake's speed is set as a fixed integer

snake_speed = 15

    #Font styles are set for every letter or number in game

font_style = pygame.font.SysFont("bahnschrift", 25)

score_font = pygame.font.SysFont("comicsansms", 35)

    #A function called Your_score is created to update the score with the input from the player

def Your_score(score):

        #Value is a variable assigned for the player’s score

    value = score_font.render("Your Score: " + str(score), True, yellow)

    dis.blit(value, [0, 0])

    #A function called our_snake is created for the list and block

def our_snake(snake_block, snake_list):

    for x in snake_list:

    #Each block is moved to one back or one foward

        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

    #A function called message is defined for dimensions, font and style as you will se below

    def message(msg, color):

    #The message's font style,dimensions and color is rendered

            mesg = font_style.render(msg, True, color)

            dis.blit(mesg, [dis_width / 6, dis_height / 3])

            #Loop is created as a function to restar the game at the end

            def gameLoop():

            #game_over and game_close get defined as false

            game_over = False

            game_close = False

            #The coordinate values are defined as the halves of dimensions

            x1 = dis_width / 2

            y1 = dis_height / 2

            #Two more variables of x and y to update the snake's location continuously

            x1_change = 0

            y1_change = 0

            #The snake list is created

            snake_List = []

            #Length of the actual snake is defined as a fixed integer

            Length_of_snake = 1

            #Food locations are randomly defined, one for each axis

            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            #A while loop using the variable game_over is created

            while not game_over:

            #A while loop within a while loop is created to respond if the game crashes or is closed

            while game_close == True:

            #The backround will become blue

            dis.fill(blue)

            #Prints message “You lost”

            message("You Lost! Press C-Play Again or Q-Quit", red)

            #The display is updated

            pygame.display.update()

            #If else logic to update the location of the snake as input is received

            for event in pygame.event.get():

            #Reads input

            if event.type == pygame.KEYDOWN:

            #If the letter "q" is pressed, then the game will close

            if event.key == pygame.K_q:

            game_over = True

            game_close = False

            #If the letter "c" is pressed, then the game will continue and the game loop will take effect

            if event.key == pygame.K_c:

            gameLoop()

            #checks the current events and renew the locations with if else logic

            for event in pygame.event.get():

            #Using if else logic to close game if a certain input is received

            if event.type == pygame.QUIT:

            game_over = True

            #Checks every event of whatever input is received

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

            #When input suggests borders of the game to be broken, game_close will come into play(no pun intended)

            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:

            game_close = True

            #Changes coordinates and colors of the snake head.

            x1 += x1_change

            y1 += y1_change

            dis.fill(blue)

            #Draws the rectangle

            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

            #The snake's head is defined as an empty list

            snake_Head = []

            #Axis are appended to the previously defined empty list

            snake_Head.append(x1)

            snake_Head.append(y1)

            snake_List.append(snake_Head)

            #The first object on the snake list is deleted to update the last block

            if len(snake_List) > Length_of_snake:

            del snake_List[0]

            #If else logic to put in use in case the snake touches itself by using the loop(double loop)

            for x in snake_List[:-1]:

            if x == snake_Head:

            game_close = True

            #The our_snake function is used in order to update the snake's blocks and list locations

            our_snake(snake_block, snake_List)

            #Updates display

            pygame.display.update()

            #If snake eats, "Yummy" will be printed

            if x1 == foodx and y1 == foody:

            #New food is randomly generated after being consumed by the snake so that the food is updated as the player eats others.

            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

            #Adds length if player eats food

            Length_of_snake += 1

            #The clock ticks at the snake's movement speed

        clock.tick(snake_speed)

        #All current windows quit

        pygame.quit()

        #Quits pygame

        quit()

        #Function resets game code

        gameLoop()