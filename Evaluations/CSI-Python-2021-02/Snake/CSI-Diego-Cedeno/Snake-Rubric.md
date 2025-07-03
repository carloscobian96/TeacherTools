# Snake Rubric: CSI-Diego-Cedeno

## Score: /100 Points
| Criteria | Points | Score | 
|----------|--------|-------| 
| 9 commits | 45 |  | 
| Commented code | 40 |  | 
| Instructions | 15 |  | 


<br>

### Submitted Work: 

```python


import pygame
import time
import random

#This initializes all the imported pygame modules
pygame.init() 

#Here are the colors used
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red=(213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#Dimensions of the game
dis_width = 600
dis_height = 400

# Sets the dimensions for the game 
dis=pygame.display.set_mode((dis_width, dis_width)) 

#Will see this message on the display screen
pygame.display.set_caption('Snake game by Edureka') 

#This is used to keep time of the game
clock = pygame.time.Clock()
snake_block = 10
#The speed that the snake will have
snake_speed = 15

#font style for message
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

#Function created for the score of the game
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow) #Color of the score
    dis.blit(value, [0, 0])
 

#It creates the snakes's block and list
def our_snake(snake_block, snake_list):
    for x in snake_list:
        #the blocks keep moving to the next one
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

#This function creates the message that will appear at game over and it creates size, color, and position of the text
def message (msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])

#Creating a function for the game to start until it is over or closed
def gameLoop():
    game_over = False 
    game_close = False

    #The defined variables are width and height divided by 2
    x1 = dis_width/2
    y1 = dis_height/2

    #These are variables that have the values of x and y coordinates
    x1_change = 0
    y1_change = 0

    #The snake list and length
    snake_List = []
    Length_of_snake = 1

    #Here it places the food on random locations of x and y coordinates
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0

    #creates and starts the loop
    while not game_over:

        #A while for the game closing
        while game_close == True:
            dis.fill(blue) 

            #Here it gives you the message that you lost and it updates it on the display in red
            message("You Lost! Press Q-Quit or C-Play Again", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            #Here it checks for the event that is occuring on pygame
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN: 
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop() #restarts game

        #Returns all the actions 
        for event in pygame.event.get(): 
            #Here QUIT closes or exits the game
            if event.type == pygame.QUIT: 
                game_over = True
            #This is the KEYDOWN class of Pygame which has different key events that can move the snake in different directions.
            if event.type == pygame.KEYDOWN: 
                #Moves the snake to the left 
                if event.key == pygame.K_LEFT: 
                    x1_change = -snake_block
                    y1_change = 0
                #Moves the snake to the right
                elif  event.key == pygame.K_RIGHT: 
                    x1_change = snake_block
                    y1_change = 0
                #Moves the snake up
                elif  event.key == pygame.K_UP: 
                    y1_change = -snake_block
                    x1_change = 0
                #Moves the snake down
                elif  event.key == pygame.K_DOWN: 
                    y1_change = snake_block
                    x1_change = 0

        #defines limits for x and y coordinates of the snake, less or equal to the screen
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True
       
        #if x1 or y1 increase the change also increases
        x1 += x1_change
        y1 += y1_change

        #fills the display with the color
        dis.fill(blue)

        #This function draws the food as a rectangle with color and size
        pygame.draw.rect(dis, blue, [foodx, foody, snake_block, snake_block]) 

        #Snakes's head
        snake_Head = []
        #Here are the snake's head x and y coordinate
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)

        #if the lenth of the snake list is bigger than the snake it deletes the list
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        
        #When the snake is less than one the game closes or is over
        for x in snake_List[:-1]:
            if x == snake_Head:
                 game_close = True
        
        #It updates the snakes location of the blocks and your score
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)


        #This function draws the snake as a rectangle with color and size
        #pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block]) 

        #Here it updates the screen
        pygame.display.update() 
        
        #Each time the snake crosses over the food it will print this message
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1   

        #Here the clock keeps the snake speed 
        clock.tick(snake_speed)


    #Here it quits the game
    pygame.quit() 
    #Quits all
    quit() 

#Starts the game all over 
gameLoop()
```




# Instructions:

<div style="text-align:center">
        <img    src="https://d1jnx9ba8s6j9r.cloudfront.net/blog/wp-content/uploads/2019/10/final-screen-snake-game-Edureka.png"
                width="50%" 
                height="50%" />          
</div>

# [Snake](https://www.edureka.co/blog/snake-game-with-pygame/)

<br>

## Code Reading Practice
Follow the tutorial from the link above.

### Comment Code:
1. Create `Snake.py`
2. Copy the first block of code.
3. Run the code.
4. Comment each line of code.
5. Create a commit.
6. Read the next block of code. 
7. Include any new lines of code in your file.
8. Comment and repeat 4-7