from time import time       #This line of code imports time and the functions that come with it
import pygame           #This line of code imports pygame and the functions that come with it
import time             #This line of code imports time and the functions that come with it
import random           #This line of code imports random and the functions that come with it

pygame.init()           # This line of code initializes the game

blue=(50,153,213)#Establishes the snakes color with its RGB number. 
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255,255,102)
green = (0,255,0)
red=(213,50,80)#Establishes the color with its RGB number.

dis_width =600                      #This line of code sets the width of the display screen
dis_height = 400                     #This line of code sets the height of the display screen
dis= pygame.display.set_mode((dis_width,dis_width))      #This line of code creates the screen that will be used for the game

pygame.display.set_caption('Snake game by Edureka')      #This line of code gives the name 'Snake game by Edureka' to the screen

clock = pygame.time.Clock()                          #This line of code is to see the time frame while the snake is moving
snake_block = 10                                        #This line of code sets the size of the snake block
snake_speed = 15                                      #This line of code sets the speed of the snake

font_style = pygame.font.SysFont("bahnschrift",25)               #This line of code sets the font for the game
score_font = pygame.font.SysFont("comicsansms", 35)                  #This line of code sets the font for the game

def Your_score(score):   #This function displays the score of the player which is equal to the lenght of the snake minus 1
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 

def our_snake(snake_block, snake_list):                     #This function draws the body of the snake
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])



def message(msg,color):                                 #This line of code defines the function called message, which displays messages to on the playing screen
    mesg = font_style.render(msg,True,color)            #This line of code sets the parameters of the variable called mesg
    dis.blit(mesg, [dis_width/6, dis_height/3])         #This line of code sets the coordinates will the text will appear

def gameLoop():  
    game_over=False                                          #This line of code creates a booleang variale that is set to False, meaning that the game is not over unitl this variable is true.
    game_close = False
 
    x1 = dis_width/2                                               #This line of code sets the starting x coordinate position for the head of the snake 
    y1 = dis_height/2                                              #This line of code sets the starting y coordinate position for the head of the snake 

    x1_change = 0                                           #This line of code holds the updating values of the x coordinate. 
    y1_change = 0                                           #This line of code holds the updating values of the y coordinate.
 
    snake_List = []                                         #This line of code is an empty variable to store the length and the parts of the body that are being added to the snake
    Length_of_snake = 1                                     #This line of code is a variable equal to 1 that will later be used to add length to the snake.

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0   #This line of code will create a food on the screen on the given x coordinate calculation
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0   #This line of code will create a food on the screen on the given y coordinate calculation


    while not game_over:                                     #This line of code is a loop that says that the screen will not go away until the game_over variable is set to True
        while game_close == True:
            dis.fill(white)                                 #This line of code says that the display screen will be white
            message("You Lost! Press Q-Quit or C-Play Again", red) #This line of code displays the given message in color red.
            pygame.display.update()                                 #This line of code updates the display screen
 
            for event in pygame.event.get():                        #This forloop is saying that when the Q key is pressed, the game will quit, and if the C key is pressed, it will begin a new game
                if event.type == pygame.KEYDOWN:                    
                    if event.key == pygame.K_q:                     #This ends the forloop if Q is pressed 
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:                     #This restarts the the game if c is pressed
                        gameLoop()

            for event in pygame.event.get():                     #This line of code runs a forloop over every event that will be in a set list. 
                        # print(event)   #prints out all the actions that take place on the screen
                    if event.type==pygame.QUIT:                      #This line of code says that when the program detects an attempt to close the program, it will change the game_over variable to True, and this will end the game.
                            game_over=True                               #This line of code gives the variable 'game_over' a True value, which then causes the game to end.
                    if event.type == pygame.KEYDOWN:                 #This line of code uses the functions of KEYDOWN to move the snake
                        if event.key == pygame.K_LEFT:               #This line of code moves the snake to the left.
                                x1_change = -snake_block
                                y1_change = 0
                        elif event.key == pygame.K_RIGHT:            #This line of code moves the snake to the right.
                                x1_change = snake_block
                                y1_change = 0
                        elif event.key == pygame.K_UP:              #This line of code moves the snake up.
                                y1_change = -snake_block
                                x1_change = 0
                        elif event.key == pygame.K_DOWN:            #This line of code moves the snake down.
                                y1_change = snake_block
                                x1_change = 0
                    
            if  x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #This line of code is saying that if the snake block hits any of the edges of the screen, the game will end.
                        game_over = True

            x1 += x1_change                                     #This line of code holds the updating values of the x coordinate.
            y1 += y1_change                                     #This line of code holds the updating values of the y coordinate.
            
            dis.fill(blue)                                     #This line of code says that the display screen will be blue
            # pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])      #This line of code draws a rectangle in the display at the given cordinates
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])#This line of code draws a rectangle in the display at the given cordinates
            
            #The following group of code draws the head, the body, and other elements of the snake.
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
    
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
    
            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)                     #This is the score that will be displayed on the screen (length of snake - 1)
    
            pygame.display.update()                             #This line of code updates the screen
    
            if x1 == foodx and y1 == foody:                     #This if statement says that if the coordinates of the food are equal to the coordinates of the head, it will add to the length of the snake.
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0       #This line of code gives the food an x coordinate
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0      #This line of code gives the food an y coordinate
                Length_of_snake += 1                            #This line of code adds length to the snake
    
            clock.tick(snake_speed)
                
            # if x1 == foodx and y1 == foody:                     #This line of code is saying that if the snake passes over the coordinates where the food is, it will say Yummy!!
            #     print("Yummy!!")
            # clock.tick(snake_speed)                                      #This line of code sets the speed for the snake
                
                # pygame.draw.rect(dis,blue,[200,150,10,10])           #This line of code draws a rectangle in the display at the given cordinates
                
            # message("You lost", red)                                   #This lines of code display a message saying "You Lost" after the player has lost.
            # pygame.display.update()                                   #This lines of code display a message saying "You Lost" after the player has lost.
            # time.sleep(2)                                   #This lines of code display a message saying "You Lost" after the player has lost.

        pygame.quit()           #This line of code unitializes the game that has been started
        quit()                  #This line of code unitializes everything

    gameLoop()