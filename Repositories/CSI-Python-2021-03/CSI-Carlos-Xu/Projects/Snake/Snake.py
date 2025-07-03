import pygame #It calls the module where the game is.
import time #Allows to use the time frame in the game. 
import random # This is for the food to appear in a random position. 
pygame.init() #This step initialize the game.


blue=(0,0,255) #Defines the RGB combination for blue.
red=(255,0,0) #Defines the RGB combination for red. 
white = (255, 255, 255) #Defines the RGB combination for white.
black = (0, 0, 0) #Defines the RGB combination for black. 
yellow = (255, 255, 102) #Defines the RGB combination for yellow.
green = (0, 255, 0) #Defines the RGB combination for green. 


dis_width = 800 #Indicates the width of the display.
dis_height  = 600 #Indicates the height of the display.

 
dis=pygame.display.set_mode((dis_width,dis_height)) #This creates a display for the game with those dimensions.
pygame.display.set_caption('Snake game by Carlos Xu') #This string names the screen. 

clock = pygame.time.Clock() #This allows the coder to use the clock.tick variable. 
snake_block=10 #Dimensions of the snake. 
snake_speed=20 #Speed of the snake

font_style = pygame.font.SysFont("bahnschrift", 35) #Indicates the font and size of the letters for game over message.
score_font = pygame.font.SysFont("comicsansms", 35) #Indicates the font and size of the letters for the score. 

def Your_score(score): #Defining the score of the game. 
    value = score_font.render("Your Score: " + str(score), True, black) #Indicates the three parameters for the score [the correct message ("Your Score"), its number (the string) and its color].
    dis.blit(value, [0, 0]) #The location of the score in the display of the game.  

def our_snake(snake_block, snake_list): #Defining the body of the snake. 
    for x in snake_list: #When eating food, the body's snake will grow. 
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block]) #The body's snake will grow one snake blcok every time it eats. 

def message(msg,color): #defining the message function.
    mesg = font_style.render(msg, True, color) #Indicates the three parameters for the game over message (the correct message and its color)
    dis.blit(mesg, [dis_width/9, dis_height/2]) #Indicates where the message is going to appear (its position).

def gameLoop():  #Creating a function for a gameloop. 
    game_over = False ##The display of the game closes when losing. 
    game_close = False #Appears the message of "Game over! Press Q-Quit or C-Play Again"

    x1 = dis_width/2 #indicates the position of the snake in the display in terms of the x-axis. 
    y1 = dis_height/2 #indicates the position of the snake in the display in terms of the y-axis. 
    x1_change = 0  #This is to hold the updating values of the x and y coordinates.    
    y1_change = 0  #This is to hold the updating values of the x and y coordinates.   

    snake_List = [] #Defines the snake's body as a list. 
    Length_of_snake = 1 #Its body will start with one block. 

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #Indicates the dimension and the size of the food in x-axis.
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 #Indicates the dimension and the size of the food in y-axis.
    while not game_over: #This is a loop that will keep repeating itself until the gameover variable has been set to true. 
        while game_close == True: # After the game is over. 
            dis.fill(white) #The display will be white. 
            message("Game over! Press Q-Quit or C-Play Again", red) ##It will appear this message on the screen. 
            Your_score(Length_of_snake - 1) #The score of the game will increase by one every time the snake eats one block of food. This means that the score will increase as much as the snake's body.
            pygame.display.update() #This step updates the display of the screen.

            for event in pygame.event.get(): #get every event as a list and run a forloop over them. 
                if event.type == pygame.KEYDOWN: #Establishes the keyboard keys that are being used while playing the game. 
                    if event.key == pygame.K_q: #Pressing Q equals exit the game. 
                        game_over=True #If it receives a quit event, then the forloop ends.
                        game_close = False # It will not appear the message of "Game over! Press Q-Quit or C-Play Again"
                    if event.key == pygame.K_c: #Pressing C equals play again. 
                        gameLoop() #The game will start again. 

        for event in pygame.event.get(): #get every event as a list and run a forloop over them. 
            if event.type==pygame.QUIT: #Here, system receives an event which quits the game.
                game_over = True #When the screen closes and exits the game. 
            if event.type == pygame.KEYDOWN: #Establishes the keyboard keys that are being used while playing the game. 
                if event.key == pygame.K_LEFT: #Indicates the use of the left arrow. 
                    x1_change = -snake_block # When pressing it, the snake will move -10 in x-axis. 
                    y1_change = 0 # When pressing it, the snake will not move in the y-axis. 
                elif event.key == pygame.K_RIGHT: #Indicates the use of the right arrow. 
                    x1_change = snake_block # When pressing it, the snake will move 10 in x-axis. 
                    y1_change = 0  # When pressing it, the snake will not move in the y-axis.
                elif event.key == pygame.K_UP: #Indicates the use of the upper arrow. 
                    y1_change = -snake_block #When pressing it, the snake will move -10 in y-axis. 
                    x1_change = 0 #When pressing it, the snake will not move in the x-axis.
                elif event.key == pygame.K_DOWN: #Indicates the use of the lower arrow. 
                    y1_change = snake_block #When pressing it, the snake will move 10 in y-axis. 
                    x1_change = 0 #When pressing it, the snake will not move in the x-axis.

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #If the snake touches the boundaries of the display, the game is over. 
            game_close = True #Game is over. 
        
        x1 += x1_change #Does an update of the snake position in the x-axis. 
        y1 += y1_change #Does an update of the snake position in the y-axis. 
        dis.fill(white) #Indicates that the display will be white. 
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block]) #Set the position (coordinates 200, 150- in the middle) and size (10, 10- pixels) of the snake.

        snake_Head = [] #Defines the variable of the snake's head as a empty list.
        snake_Head.append(x1) #It will increase in x-axis.
        snake_Head.append(y1) #It will increase in y-axis.
        snake_List.append(snake_Head) #This will add one block to the snake every time it eats. 


        if len(snake_List) > Length_of_snake: #If the length of the snake list is greater than the snake's body.
            del snake_List[0] #It will remain as an empty list. 
 
        for x in snake_List[:-1]: #The snake cannot touch itself. 
            if x == snake_Head: # If any part of the snake's body touches its head, then the player will lose.
                game_close = True #It will appear the game over message and the game will close. 
 
        our_snake(snake_block, snake_List) #Calls the function our_snake with parameters snake_block and snake_List. 

        Your_score(Length_of_snake - 1) #The score of the game will increase by one every time the snake eats one block of food. This means that the score will increase as much as the snake's body.
 
 
        pygame.display.update() #Updates the display.

        if x1 == foodx and y1 == foody: #If the snake touches food. 
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #Moves the food's x values elsewhere. 
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 #Moves the food's y values elsewhere.
            Length_of_snake += 1 #The lenght of the snake will increase by one block. 


        if x1 == foodx and y1 == foody: #This describes when the snake eats the food. 
            print("Yummy!!") #This will be printed in the terminal when the snake eats the food. 
        clock.tick(snake_speed) #Set the game speed to snake_speed. 

    pygame.quit() #Uninitialize the screen display. 
    quit() #Uninitialize everything. 
gameLoop() #Calls the function that makes the game.  