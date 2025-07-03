import pygame
import time
import random

#initialize imported pygame
pygame.init()

#define colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#define dimentions
dis_width = 600
dis_height  = 400

#sets window size
dis = pygame.display.set_mode((dis_width, dis_width))

#define x1 and x 2 as half of the width and len
x1 = dis_width/2
y1 = dis_height/2
 
#set size for snake block
snake_block=10

#updates display
pygame.display.update()
#sets caption
pygame.display.set_caption('Snake game by Edureka')
#variable used in while loop 
game_over=False


 


#clock to keep time
clock = pygame.time.Clock()
 #set snake block sie
snake_block = 10
#set speed for snake
snake_speed = 15

#set fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#function to print score
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

 #funstion for each snake block in the snake to follow list of instructions
def our_snake(snake_block, snake_list):
    #for each block
    for x in snake_list:
        #move each block to next block precious spot
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 #output message
def message(msg,color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/2, dis_height/2])

#define function for game
def gameLoop():
    #define game close and over var
    game_over=False
    game_close = False
    #variables updating the snake coordinates
    x1 = dis_width/2
    y1 = dis_height/2
    x1_change = 0       
    y1_change = 0

    #define snake list and lenght
    snake_List = []
    Length_of_snake = 1

    #add food location variables at random 
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

#while loop to keep window open
    while not game_over:
        #WHAT TO DO IF CLOSE   
        while game_close == True:
            #background white
            dis.fill(blue)
            #print You lost
            message("You Lost! Press Q-Quit or C-Play Again", red)
            #update display
            pygame.display.update()
            #check events
            for event in pygame.event.get():
                #chek letter hit and act accordingly 
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        #check events and update locations according to key
        for event in pygame.event.get():
            #close window if user hits X
            if event.type == pygame.QUIT:
                game_over = True
            #if key..
            if event.type == pygame.KEYDOWN:
                #if key left go left
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                #if key right go right
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                #if key up go up
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                #if key down go down
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
        #loose if hit border
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        #change coordinate of snake head
        x1 += x1_change
        y1 += y1_change
        #fill blue
        dis.fill(blue)
        #draw  rectangle
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
        #snake head defined
        snake_Head = []
        #append coordinates to snake head
        snake_Head.append(x1)
        snake_Head.append(y1)
        #append snake head location to snake_List
        snake_List.append(snake_Head)
        #delete first object on snake_List
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        #check if head crosses body and loose
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        #call function to update location of all the squares
        our_snake(snake_block, snake_List)
        #call function to print score of points
        Your_score(Length_of_snake - 1)


        #update display

        pygame.display.update()
        #add food
        pygame.draw.rect(dis, "blue", [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        #update display
        pygame.display.update()
        #print "yummy" if snake over food
        if x1 == foodx and y1 == foody:
            #set new food location
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            #increase the length of the snake by one square
            Length_of_snake += 1
        #snake speed
        clock.tick(snake_speed)
    #quit windows
    pygame.quit()
    #quit pygames
    quit()
 
#call function to start game
gameLoop()

