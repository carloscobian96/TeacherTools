# In order to import pygame, you must first install it to python by typing 'pip install pygame' on the terminal
# If that doesn't work for you, try manually downloading the newest version of python, allow PATH to be included, and then restart the visual studio code application
# After that, type 'pip install pygame' once again
import pygame
import time
import random

# Insert the .init() function to boot up the game
# This will be necessary for running this entire code
pygame.init()

# Insert the colors necessary to distinguish the snake, the food, and eventually the highscore 
# Colors in Python use an RGB (Red, Green, Blue) color scheme, with each color being determined by the specific quantity of red, green or blue a variable has
# So when you determine a color in the game's screen, put a parenthesis divided by three commas to properly organize its RGB scheme 
blue = (255, 255, 255)
yellow = (255,255,102)
black = (0,0,0)
red = (213,50,80)
green = (0,255,0)
white = (50,153,213)

# Set the width and length of the screen's surface
# These values will be used to establish the game's borders
dis_width = 600
dis_height = 400 

dis = pygame.display.set_mode((dis_width, dis_height))

# Set the game's title by writing a header
pygame.display.set_caption("Snake game by Nicolas Giner")

clock = pygame.time.Clock()

# Determine the size of the snake block and its speed
snake_block = 10
snake_speed = 15

# Determine the size and font for the game's title and score counter 
font_style = pygame.font.SysFont(None,30)
score_font = pygame.font.SysFont("comicsansms",35)

# Determine your current score in the game
# Notice how the parenthesis in value is organized: (message, True, color)
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0,0])

# Draw a snake for the game
def our_snake(snake_block, snake_list):
    for x in snake_list:

        # Because the snake is a rectangle, write 'pygame.draw.rect' to prevent any future errors
        pygame.draw.rect(dis,black,[x[0],x[1], snake_block, snake_block])

# Determine the length and color of the game over text that will appear later on in this code
def message (msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

# Determine the game's own loop code 
# By putting false in both 'game_over' and 'game_close', you stop the current game without quiting the program altogether
# It restarts the game using its code's own logic
def gameLoop():
    game_over = False
    game_close = False
    
    # This can be used to customize the x and y values of the snake
    x1 = dis_width/2
    y1 = dis_height/2

    # This will be important for updating the x and y coordinates of the snake
    x1_change = 0
    y1_change = 0

    # The snake in this game will be contained in a list so that it has an initial value where it can grow from, in this case being 1
    snake_List = []
    Length_of_snake = 1

    # Set the coordinates of the food by giving it a random range within the borders of the game screen 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        # This determines whether you lost the game by establishing a 'while' loop that could either restart or end the game depending on your choice
        while game_close == True:
            dis.fill(white)
            message("You lost! Press Q to quit or C to play again", red)

            # A trick used to determine your score is subtracting your snake's current length by one, since that's its base value in the beginning of the game 
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            # To give the player the option to restart or quit the game, write two keys that allow for such
            # 'KEYDOWN' will also be used for determining the direction of the snake 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:

                        # By writing these two lines, you end the current "Game Over" loop and the game overall
                        game_over = True
                        game_close = False

                    
                    if event.key == pygame.K_c:

                        # By writing "gameLoop()", you allow the program to resume its operations and restart the game
                        gameLoop()

        # This simply allows you to quit the game manually without having to lose
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over= True

            # In order to control the snake, first you need to establish which keys shall be used to maneuver it
            # By inputting 'KEYDOWN', you allow your game to use keys in order to move the snake, whether it's up, down, left, or right
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:

                    # The values of x1_change and y1_change will determine whether the change in the snake's direction is horizontal or vertical
                    x1_change = -snake_block
                    y1_change = 0

                elif event.key == pygame.K_DOWN:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_LEFT:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_RIGHT:
                    y1_change = snake_block
                    x1_change = 0
        
        # Establish a reaction to reaching or passing the game's borders
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True 

        # As stated beforehand, this updates the values for the x and y coordinates of the snake
        x1 += y1_change
        y1 += x1_change

        # This fills the screen with a given color
        dis.fill(white)
        
        # In order to distinguish the food from the snake, give the food its own color
        pygame.draw.rect(dis, green, [foodx,foody, snake_block, snake_block])

        # This makes it so that the snake's size grows by giving it another block
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        # This makes sure that the length of the snake only grows in accordance to the amount of food it eats
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        # This makes it so that the game is over once the snake touches any part of its body
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)

        # This allows for the snake to update its own display as it grows larger
        pygame.display.update() 

        # This establishes a reaction once the snake reaches the food's coordinates
        # What you want to do is make it so that the food changes its coordinates to a random arrangement within the borders of the game screen
        # Plus, now that the snake ate the food, you update it so that it grows larger
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            
        clock.tick(snake_speed)

    # At the end of this 'while not game_over' loop, its important to add these two lines to provide the game with an event called quit
    pygame.quit()
    quit()


gameLoop()