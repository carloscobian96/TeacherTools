

import pygame# imports the Library used for the display
import time# imports time module
import random# imports the random mocule thet alows for randomising numbers
pygame.init() #Starts all the modules used for the game

 
white = (255, 255, 255)# defines the rgb for white
black = (0, 0, 0)# defines the rgb for black
red = (255, 0, 0)# defines the rgb for red
blue = (0, 0, 255)# defines the rgb for blue
green = (0, 255, 0)#defines the rgb for blue
yellow = (255, 255, 102)# defines the rgb value for yellow
dis_width = 800# defines the width of display
dis_height  = 600# defines the heigth of display
 
dis = pygame.display.set_mode((dis_width, dis_width))#Opens the display and sets the bounderies for it
pygame.display.set_caption('Snake game by Carlos Q')#Starts the caption for the game

clock = pygame.time.Clock()#the velocity of the game is defined
 
snake_block = 10 # defines the variable where the snake starts
snake_speed = 15 # sets the speed for the game to 15 tics 
 
font_style = pygame.font.SysFont("bahnschrift", 25) # sets the font to be bahnschrift
score_font = pygame.font.SysFont("comicsansms", 35)# sets the font to be comicsansms
 
 
def Your_score(score):#creates a function to show score
    value = score_font.render("Your Score: " + str(score), True, yellow) # creates a yellow string with yoru game score
    dis.blit(value, [0, 0]) # Dislpays the score on the game screen
 
 
def our_snake(snake_block, snake_list):#Function that creates the snake
    for x in snake_list: # creates a loop
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])# creates the snake in the middle of the game
 
 
def message(msg, color): #Function that renders a message ith a function
    mesg = font_style.render(msg, True, color) #Creates a message with the given color and given string
    dis.blit(mesg, [dis_width / 6, dis_height / 3]) # Defines the width of the distance as 6 and defines the hegith of the message as a thrid to the display
 
 
def gameLoop(): #Function that creates the game 
    game_over = False# The game is not over
    game_close = False #The game has not closed
 
    x1 = dis_width / 2 # set the original state of the snake to the middle of the display
    y1 = dis_height / 2 # set the original state of the snake to the middle of the display
 
    x1_change = 0# At the start of the game there is no state of change in x
    y1_change = 0 #At the start of the game there is no state of change in y
 
    snake_List = [] 
    Length_of_snake = 1 # the length of the snake is one at the begining of the game
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 # sets the x value of the food to a randmo number
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 # sets the y value of the food to arandom number
 
    while not game_over:# loops if the game is not over
 
        while game_close == True:# if the game has closed
            dis.fill(blue) # fill the backgroudn with blue
            message("You Lost! Press C-Play Again or Q-Quit", red)# displays the loose message
            Your_score(Length_of_snake - 1) # Displays your score as the length of the snake
            pygame.display.update() # updates the display
 
            for event in pygame.event.get(): # For every event
                if event.type == pygame.KEYDOWN: # if a key is pressed
                    if event.key == pygame.K_q: #if the key is q
                        game_over = True # The game if over
                        game_close = False # but it isnt closed
                    if event.key == pygame.K_c:
                        gameLoop() #if the key pressed is c then the game will start again
 
        for event in pygame.event.get(): # for every event in the game 
            if event.type == pygame.QUIT:# if the display has been quit
                game_over = True# then the game is over
            if event.type == pygame.KEYDOWN:# if a key is pressed
                if event.key == pygame.K_LEFT: # if the key is left
                    x1_change = -snake_block #change the x value negatively
                    y1_change = 0 #but dont change the x value
                elif event.key == pygame.K_RIGHT: #if the rigth key is pressed
                    x1_change = snake_block #change the x value positivelt
                    y1_change = 0 #but fdint change the y value
                elif event.key == pygame.K_UP: #if the up key is presed
                    y1_change = -snake_block #change the y value negatively
                    x1_change = 0# but dont change the x value
                elif event.key == pygame.K_DOWN: # if the downard key is preessed
                    y1_change = snake_block # change the y value positivelt
                    x1_change = 0# dont change the x value
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: # if the cnake hits the boder
            game_close = True # close the game
        x1 += x1_change # add the change in  x to the  x value of the snake
        y1 += y1_change# add the change in  y to the  y value of the snake
        dis.fill(blue) # fill the background wit blue
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) # 
        snake_Head = []# create a blank array named snake_Head
        snake_Head.append(x1) # append the values of x every time they change
        snake_Head.append(y1) # append the values of y every time they change
        snake_List.append(snake_Head) # Append the snaeke_head to the list
        if len(snake_List) > Length_of_snake: #If th 
            del snake_List[0] # delete snake List 
        #if the snake head touches any part of itself 
        for x in snake_List[:-1]: 
            if x == snake_Head:
                game_close = True#end the game 
 
        our_snake(snake_block, snake_List) #Iniciate the snake 
        Your_score(Length_of_snake - 1) # display the score
 
        pygame.display.update()# updates the display
 
        if x1 == foodx and y1 == foody:# If the snake touches the food
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #Eliminate the food x 
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 # eliminate the food y
            Length_of_snake += 1# adds 1 to the length of the snake 
 
        clock.tick(snake_speed) # sets the velocity of the game 
 
    pygame.quit() #quits the displau
    quit()# Quits the code
 
 
gameLoop()# Calls  the function that stats the game