import pygame
import time
import random
 
pygame.init() #initialize the game 
 #These are all the color variables for the game
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
  #these two variables creates and displays the game with its with height
dis_width = 600
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height)) #displays the game
pygame.display.set_caption('Snake Game by Edureka') #Adds the text to the display 
 
clock = pygame.time.Clock()
 #Variables for the display of the snake and the velocity.
snake_block = 10
snake_speed = 15
 
font_style = pygame.font.SysFont("bahnschrift", 25)#The font and type of letter used for the style of the game.
score_font = pygame.font.SysFont("comicsansms", 35)#The font and type of letter used for the score.
 
 
def Your_score(score): #We create a function to update your score in the game.
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 #Here we use the draw rect function color the snake and know when it grows.
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block]) #we use the draw.rect()function to display the snake which will be a rectangle with its desired measurements and color, also to display the width and height of the food
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color) #this colors you the text in the game.
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():  #creating a function for the game to loop
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 #This spawns the food that the snake need to eat to get bigger and win the game. 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    #This makes sure that the food is not too big so it fits in the screen.
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
  # We create a wide loop to make the snake in game move.
    while not game_over:
  #This block creates a message so you are able to either quit or play again when you lose the game.
        while game_close == True:
            dis.fill(red)#By using the fill()method we change the display screen from its default black to blue.
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1) #The length of the snake grows
            pygame.display.update() #updates the display of the game.
 
            for event in pygame.event.get():# We use the event.get() function so the game doesnt quit instantly when you run it.
                if event.type == pygame.KEYDOWN:#If you click a key it does its job and makes the game loop
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop() #this makes this block of code loop 
 
        for event in pygame.event.get():# We use the event.get() function so the game doesnt quit instantly when you run it.
            if event.type == pygame.QUIT:#This makes the game quit when you hit the close button
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:#If you press the left key your x variable will be negative because it is moving left.
                    x1_change = -snake_block #negative because it is moving left.
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:#If you press the right key your x variable will be positive because it is moving right.
                    x1_change = snake_block #positive because it is moving right.
                    y1_change = 0
                elif event.key == pygame.K_UP:#If you press the up key your x variable will be negative because it is moving up.
                    y1_change = -snake_block #negative because it is moving up. 
                    x1_change = 0
                elif event.key == pygame.K_DOWN:#If you press the down key your x variable will be positive because it is moving down.
                    y1_change = snake_block#positive because it is moving down
                    x1_change = 0
 
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(red)#By using the fill()method we change the display screen from its default black to blue.
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) #we use the draw.rect()function to display the snake which will be a rectangle with its desired measurements and color, also to display the width and height of the food
        snake_Head = []
        #This blovk of code is to create the snake 
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 #This is for the snake to increase its score
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1) #Your score goes up everytime you collect food
 
        pygame.display.update() #updates the display of the game.
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #This spawns the food that the snake need to eat to get bigger and win the game. 
            #This makes sure that the food is not too big so it fits in the screen.
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1 #Makes the length of the snake bigger when you collect food
 
        clock.tick(snake_speed)
 
    pygame.quit() #uninitialize the game
    quit() #quit the game
 
 
gameLoop()#this loops the game or makes it possible for the game to restart