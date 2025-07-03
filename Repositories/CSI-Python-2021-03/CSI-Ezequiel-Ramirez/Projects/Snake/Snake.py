import pygame #Imports the Pygame package, which is crucial for pretty much everything here.
import time #Imports the Time package, which makes the games internal timer system function.
import random #Imports the Random package, used for randomizing the location of the food.

pygame.init() #Initializes the Pygame module, which then allows everything that comes after to function.

white = (255, 255, 255) #Sets the RGB value for the background color of the Game Over screen.
yellow = (255, 255, 102) #Sets the RGB value for the text used to keep track of the users score.
black = (0, 0, 0) #Sets the RGB value for the player-controlled Snake.
red = (255, 0, 0) #Sets the RBG value for the the text seen when getting a game over.
green = (0, 255, 0) #Sets the RGB value for the food the Snake has to collect
blue = (0, 0, 255) #Sets the RBG value for the background color.

dis_width = 800 #Sets the width of the Snake.
dis_height  = 600 #Sets the height of the Snake.

dis=pygame.display.set_mode((800,600)) #Creates the screen that users will use to view the game.
pygame.display.set_caption('Snake game by ya boi Zeke') #Credits the one and only creator of this script in the top of the screen.

clock = pygame.time.Clock() #Variable that keeps track of the time passed.

snake_block = 10 #Creates a variable that represents the Snake block.
snake_speed = 30 #The variable that controls the speed of the Snake.
 
font_style = pygame.font.SysFont("bahnschrift", 25) #The font used for the Game Over screen.
score_font = pygame.font.SysFont("comicsansms", 35) #The font used for the user for the score.


def Your_score(score): #Function used to keep track of your score.
    value = score_font.render("Your Score: " + str(score), True, yellow) #Renders out the text and number of your score.
    dis.blit(value, [0, 0]) #Transfers the users score value.



def our_snake(snake_block, snake_list): #The function used whenever a block needs to be added for the Snake's size.
    for x in snake_list: #Adds an extra block to the snake every time it collects food.
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block]) #Visually draws said added block.


def message(msg,color): #This function is called whenever text needs to be displayed onscreen.
    mesg = font_style.render(msg, True, color) #This line determines the text's font and color.
    dis.blit(mesg, [dis_width/2, dis_height/2]) #This line determines the position of the text.


def gameLoop():  #Creates the function that makes up the bulk of the game's code.
    game_over = False #Sets the default Game Over state as false.
    game_close = False #Makes it so the game doesn't close instantly lmao.
 
    x1 = dis_width/2 #Sets the default starting value of the Snake on the x axis.
    y1 = dis_height/2 #Sets the default starting value of the Snake on the y axis.
  
    x1_change = 0 #The variable that handles the change in x axis position.
    y1_change = 0 #The variable that handles the change in y axis position.
    
    snake_List = [] #Stores the length of the Snake within brackets.
    Length_of_snake = 1 #Keeps track of the length of the Snake as a variable number.
    
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #Places the food in a random position of the x axis.
    foody = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #Places the food in a random position of the y axis.

    while not game_over: #Begins a while loop while the Game Over state is false.
        
        while game_close == True: #This while loop will display the Game Over text for when the player loses the game.
            dis.fill(white) #Fills the screen with nothing but white noise, just like my soul.
            message("You Lost! Press Q-Quit or C-Play Again", red) #The Game Over text.
            
            pygame.display.update() #Updates the on-screen visuals.
 
            for event in pygame.event.get(): #Initiates the for loop whenever any event happens in-game.
                if event.type == pygame.KEYDOWN: #Else-if for if the event that happens is the user pressing a key on their keyboard.
                    if event.key == pygame.K_q: #This if statement makes it so that if the Q key is pressed, the Game Over state will be true and the game will close.
                        game_over = True #Makes the  Game Over state true.
                        game_close = False #Makes the game close itself.
                    if event.key == pygame.K_c: #This if statement makes it so that if the C key is pressed, the game will start over.
                        gameLoop() #Calls the function to start the game over again.
        
        for event in pygame.event.get(): #Gets all of the actions that take place on the screen.
            if event.type==pygame.QUIT: #Makes it so that if the quit button is pressed on the UI, then the game quits.
                game_over=True #Makes the Game Over state true.
            if event.type == pygame.KEYDOWN: #Initiated if the user presses a key on the keyboard.
                if event.key == pygame.K_LEFT: #Initiated if the user pressed the left arrow key.
                    x1_change = -10 #Moves the Snakes position to the left on the x axis.
                    y1_change = 0 #Stays the same.
                elif event.key == pygame.K_RIGHT: #Initiated if the user pressed the right arrow key.
                    x1_change = 10 #Moves the Snakes position to the right on the x axis.
                    y1_change = 0 #Stays the same.
                elif event.key == pygame.K_UP: #Initiated if the user pressed the up arrow key.
                    y1_change = -10 #Moves the Snakes position upwards on the y axis.
                    x1_change = 0 #Stays the same.
                elif event.key == pygame.K_DOWN: #Initiated if the user pressed the down arrow key.
                    y1_change = 10 #Moves the Snakes position downwards on the y axis.
                    x1_change = 0 #Stays the same.
        
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0: #This elif checks every frame if the Snake is out-of-bounds or not.
            game_close = True #Initiates a Game Over if the player tries to go out-of-bounds.
        x1 += x1_change #This is what actually moves the users x axis position after the key inputs.
        y1 += y1_change #This is what actually moves the users y axis position after the key inputs.
        dis.fill(blue) #Applies the previous defined RGB values to the background.
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block]) #Visually draws the collectable food.
        snake_Head = [] #Calls the brackets which contain the length of the Snake.
        snake_Head.append(x1) #Adds an extra block to the Snake when moving on the x axis.
        snake_Head.append(y1) #Adds an extra block to the Snake when moving on the x axis.
        snake_List.append(snake_Head) #Appends the default Snake head the player always starts out with to the list.
        if len(snake_List) > Length_of_snake: #The default length of the Snake is one block, so if the length contained within the list exceeds it, then it will replace that length with the new length.
            del snake_List[0] #Deletes the old version of the list.
 
        for x in snake_List[:-1]: #Initiates whenever the Snake collides with itself.
            if x == snake_Head: #Whenever the Snake's head collides with the rest of its body, the game ends.
                game_close = True #Ends the game.
 
        our_snake(snake_block, snake_List) #Aside from having a very communist name, this just handles the actual length of the Snake.
 
        
        pygame.display.update() #Updates the active display of the game every other frame.
        
        if x1 == foodx and y1 == foody: #Checks to see if the Snake's position is the same as that of the food.
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0 #Randomizes the food to a different spot on the x axis.
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0 #Randomizes the food to a different spot on the y axis.
            Length_of_snake += 1
        
        clock.tick(snake_speed) #Makes the game at the snake's speed, which in this case is 30, so it runs at 30 FPS.

    pygame.quit() #Quits the game. Pretty self-explanatory.
    quit() #Quits the Python script. Even MORE self-explanatory.


gameLoop() #Calls the function that makes the magic happen.