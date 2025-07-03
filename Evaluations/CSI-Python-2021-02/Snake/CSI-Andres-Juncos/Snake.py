import pygame
import random
#This creates the screen for the snake game
pygame.init()
#These are the codes for the colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
#These sets the dimensions of the game
dis_width = 600
dis_height = 400
#This is the name of the game, which is displayed on top of the screen
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snek')
 
clock = pygame.time.Clock()
#Variable for snake size and speed
snake = 10
movement_speed = 15
#This determines the font for text
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 #This displays your current score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
#This creates the snake
def our_snake(snake, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, white, [x[0], x[1], snake, snake])
 
#This commands where the text is going to appear
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])
 
 
def gameLoop():   #This is the loop that makes the game continue until you die
    game_over = False
    game_close = False
 
    x1 = dis_width / 2
    y1 = dis_height / 2
    #These are the empty variables that are used for the snake's movement
    x1_change = 0
    y1_change = 0
    #This are the variables that keep track of the snake's length
    snake_List = []
    Length_of_snake = 1
    #Randomizer for the food
    foodx = round(random.randrange(0, dis_width - snake) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake) / 10.0) * 10.0
    
    while not game_over:
        #This displays the death message
        while game_close == True:
            dis.fill(blue)
            message("You are die. Press E to play again or Q to quit", red)
 
            pygame.display.update()
         #This forloop is to exit and retry the game
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        #This loop are what let you move around as the snake in-game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                #Move left
                if event.key == pygame.K_LEFT:
                    x1_change = -snake
                    y1_change = 0
                #Move right
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake
                    y1_change = 0
                #Move up
                elif event.key == pygame.K_UP:
                    y1_change = -snake
                    x1_change = 0
                #Move down
                elif event.key == pygame.K_DOWN:
                    y1_change = snake
                    x1_change = 0
        #This is to end the game if the player hits the boundary
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        #This fills the backround with a color
        dis.fill(black)
        #This spawns the food
        pygame.draw.rect(dis, green, [foodx, foody, snake, snake])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        #This increases the snakes length dependsing on the food eaten
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake, snake_List)
        Your_score(Length_of_snake - 1) 
 
        pygame.display.update()
        #This increaes the snakes length upon eating food
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake) / 10.0) * 10.0
            Length_of_snake += 1
 
        clock.tick(movement_speed)
    #This closes the game
    pygame.quit()
    quit()
 
#This loop repeats the entire game 
gameLoop()