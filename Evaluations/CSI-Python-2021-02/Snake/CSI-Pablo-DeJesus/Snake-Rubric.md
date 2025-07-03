# Snake Rubric: CSI-Pablo-DeJesus

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
pygame.init() #initializes the code
dis=pygame.display.set_mode((400,300))
pygame.display.update() #updates the changes made to screen
pygame.display.set_caption('Snake game by Pablo De Jota') #prints message at start of game in pygame screen
game_over=False #continues game
while not game_over:
    for event in pygame.event.get(): 
        print(event) #the last three lines use the input of player to determine what is printed on the screen
pygame.quit()
quit() #uninitializes the code
#this code opens the python game screen
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