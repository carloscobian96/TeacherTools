import pygame
import time
import random

#Initializes all of the imported Pygame modules.
pygame.init()

#Updates the display
#pygame.display.update()

#black, red, yellow, white, green, and blue are in the parameter "0, 0, 0", "213,50,80", "255, 255, 102" ,"255, 255, 255", "0, 255, 0", and "50,153,213" respectively
black=(0,0,0)
red=(213,50,80)
yellow = (255, 255, 102)
white = (255, 255, 255)
green = (0, 255, 0)
blue = (50,153,213)

#Sets the display paramaters
dis_width = 600
dis_height = 400
dis=pygame.display.set_mode((dis_width,dis_height))

#Names the display after the set caption
pygame.display.set_caption('Snake game by Edureka')

#Adds a clock
clock = pygame.time.Clock()

snake_block = 10
#It is the snake's speed
snake_speed = 15

#Establishes the fonts used in the game
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#Establishes the score of the player
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

#It draws the snake which is a black rectangle with the parameters of "x[0], x[1], snake_block, snake_block" 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

#It establishes the font of the message
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

#It makes it when game_over is false it prints out all the actions that take place on the screen. 
def gameLoop():
    game_over=False
    game_close=False

#parameters of x and y
    x1 = dis_width/2
    y1 = dis_height/2

#The change made in x and y
    x1_change = 0       
    y1_change = 0

    snake_List = []
    Length_of_snake=1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0


    while not game_over:
        #When game close is true, then it prints You lost
        while game_close == True:
            dis.fill(white)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            pygame.display.update()
 
            for event in pygame.event.get():
                #When pressed q then game_over is true and it closes the tab
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    #When the key c is pressed, then the game starts over
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            #When the X is pressed then game_over is true and the code ends
            if event.type == pygame.QUIT:
                game_over = True
            
            #When an arrow key is pressed then it moves according to the key pressed
            if event.type == pygame.KEYDOWN:

                #When the arrow key left is pressed then the snake goes to the left
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                
                #When the arrow key right is pressed then the snake goes to the right
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                #When the arrow key up is pressed then the snake goes up
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                #When the arrow key down is pressed then the snake goes down
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        #When x is greater or equal than the width of the screen or less than zero or y is greater than the height of the screen or is less than zero, then it is game over
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        #When x1 is increased, x1_change is increased
        x1 += x1_change
        #When x1 is increased, x1_change is increased
        y1 += y1_change
        dis.fill(blue)

        #It draws a blue rectangle with the parameters of foodx, food,y, snake_block and snake_block
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        #Make a list for the snake head
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        #If list of the snake head is less than 1, then it is game over
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
 
        #updates the display
        pygame.display.update()
 
        #When the snake is in the same x and y axis of the food, then it prints "Yummy!!!"
        if x1 == foodx and y1 == foody:
           foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
           foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
           Length_of_snake += 1

        clock.tick(snake_speed)
 
 #Used to unitialize everything
    pygame.quit()
    quit()
 
#Starts the game again
gameLoop()




