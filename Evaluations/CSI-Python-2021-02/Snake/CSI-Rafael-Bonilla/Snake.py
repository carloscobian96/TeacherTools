import pygame
import time
import random
#initializing pygame
pygame.init()

#white, yellow, black, red, green, and blue are in the parameter "255, 255, 255", "255, 255, 102",  "0, 0, 0", "255,0,0", "0, 255, 0", and "50, 153, 213" respectively
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (50, 153, 213)

#sets up a display mode that is on the parameter of width, 600, and height, 400
dis_width = 600
dis_height  = 400
dis = pygame.display.set_mode((dis_width, dis_width))

#it prints the caption that says 'Snake game by Edureka'
pygame.display.set_caption('Snake game by Edureka')

#adds a clock to the snake game
clock = pygame.time.Clock()
 
snake_block = 10
#adds the speed of the snake
snake_speed = 15

#establishes a font style for the game
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#estanlishes the score's font and the score of the player
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

#it establishes the snake and what it is composed of
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

#determines the font of the message
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

#loops the game
def gameloop():
    game_over = False
    game_close = False
    
    #parameters of x and y
    x1 = dis_width / 2
    y1 = dis_height / 2
    x1_change = 0
    y1_change = 0

    #makes a list for the snake and keeps track of its length
    snake_list = []
    Length_of_snake = 1


    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0


    while not game_over:
        #When the player loses it tells the player their score and if they want to quit or start a new game
        while game_close == True:
            dis.fill(blue)
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                game_over=True 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
    #changes the parameters of x1 and y1 to those of x1_change and y1_change
    x1 += x1_change
    y1 += y1_change
    dis.fill(blue)
    #draws a black square in the display
    pygame.draw.rect(dis,green,[foodx,foody,snake_block,snake_block])
    snake_head = []
    snake_head.append(x1)
    snake_head.append(y1)
    snake_list.append(snake_head)
    if len(snake_list) > Length_of_snake:
        del snake_list[0]

    for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True
 
    our_snake(snake_block, snake_list)
    Your_score(Length_of_snake - 1)

    #updates the screen display
    pygame.display.update()
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        Length_of_snake += 1

    clock.tick(snake_speed)

    #uninitializes everything
    pygame.quit()
    quit()

gameloop()
