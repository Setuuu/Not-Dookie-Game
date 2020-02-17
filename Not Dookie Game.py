#Not Dookie Game presented by Dookie Games, made by Setu Patel Inspired by my grade 10(2016) creation on scratch... Not Dookie Game
#Scratch version: https://scratch.mit.edu/projects/111490363/
#Images of Character(Cloud) ~ http://spritedatabase.net/file/3382
#Images of Hadouken ~ https://giphy.com/gifs/online-hadoken-sites-8TB91dQVqMR6U
#Edited each one to make it diff colour and sizes
#                                                                                                CONTROLS
# Using “A” and “D” you control your character side to side, and “W” to jump up, use space bar to teleport to your mouse location, and of course use your mouse to change your mouse position!

import pygame, sys, os
import random
from pygame.locals import *

stdout = sys.__stdout__
stderr = sys.__stderr__
pygame.init()
sys.stdout = stdout
sys.stderr = stderr

# Set the width and height of the screen [width, height]
W, H = 600, 450
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
font = pygame.font.SysFont('Calibri', 25, True, False)

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("My Game")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def checkCollision(obj1, obj2):
    [obj1x, obj1y, obj1w, obj1h] = obj1
    [obj2x, obj2y, obj2w, obj2h] = obj2

    # check bounding box
    if obj1x + obj1w >= obj2x and obj1x <= obj2x + obj2w:
        if obj1y + obj1h >= obj2y and obj1y <= obj2y + obj2h:
            return True

    return False

#Frame counter, score counter and sets everything to false
done = False
jump = False
teleport = False
screen_done = False
score = 0
frame = 0

#All the Hadouken x positions
hadouken_x_pos_blue = 0
hadouken_x_pos_black = 0
hadouken_x_pos_purple = 0

#Character x and y positon and changes
character_x_pos = 0
character_x_change = 0
character_y_pos = 0
character_y_change = 0

#Varibles for jumping and timer for hadoukens
jump_timer = 0
timerCount = -1
timerCount2 = -1
x = 0

#Loads images and places them into a list
P_B_1 = pygame.image.load("P_B_1.png").convert()
P_B_2 = pygame.image.load("P_B_2.png").convert()
P_B_3 = pygame.image.load("P_B_3.png").convert()
P_B_4 = pygame.image.load("P_B_4.png").convert()
Projectile_Blue = [P_B_1, P_B_2, P_B_3, P_B_4]

#Same hadouken/ medium speed
P_BL_1 = pygame.image.load("P_BL_1.png").convert()
P_BL_2 = pygame.image.load("P_BL_2.png").convert()
P_BL_3 = pygame.image.load("P_BL_3.png").convert()
P_BL_4 = pygame.image.load("P_BL_4.png").convert()
Projectile_Black = [P_BL_1, P_BL_2, P_BL_3, P_BL_4]

#Bigger hadouken/ fastest
P_PURP_1 = pygame.image.load("P_PURP_1.png").convert()
P_PURP_2 = pygame.image.load("P_PURP_2.png").convert()
P_PURP_3 = pygame.image.load("P_PURP_3.png").convert()
P_PURP_4 = pygame.image.load("P_PURP_4.png").convert()
Projectile_Purple = [P_PURP_1, P_PURP_2, P_PURP_3, P_PURP_4]

#Character images
Cloud1 = pygame.image.load("Cloud 1.gif").convert()
Cloud2 = pygame.image.load("Cloud 2.gif").convert()
Cloud3 = pygame.image.load("Cloud 3.gif").convert()
Cloud4 = pygame.image.load("Cloud 4.gif").convert()
Cloud5 = pygame.image.load("Cloud 5.gif").convert()
Cloud6 = pygame.image.load("Cloud 6.gif").convert()
Cloud = [Cloud1, Cloud2, Cloud3, Cloud4, Cloud5, Cloud6]

Background = pygame.image.load("Background24.jpg").convert()
Game_Over = pygame.image.load("Gameover.gif").convert()

#Background song
pygame.mixer.music.load("Rolex Song.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# -------- Main Program Loop -----------
while not done and not screen_done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                character_x_change = -14
            if event.key == pygame.K_d:
                character_x_change = 12
            if event.key == pygame.K_w:
                jump = True
            if event.key == pygame.K_SPACE:
                teleport = True
        elif event.type == pygame.KEYUP:
            teleport = False
            character_x_change = 0
    #Scrolling Background
    rel_x = x % Background.get_rect().width
    screen.blit(Background, (rel_x - Background.get_rect().width, 0))
    if rel_x < W:
        screen.blit(Background, (rel_x, 0))
    x -= 7
    pygame.display.update()

    #Blue Projectile
    if frame % 4 == 0 :
        screen.blit((Projectile_Blue[0]), [hadouken_x_pos_blue +500, 295])
    elif frame % 4 == 1:
        screen.blit((Projectile_Blue[1]), [hadouken_x_pos_blue +500, 295])
    elif frame % 4 == 2:
        screen.blit((Projectile_Blue[2]), [hadouken_x_pos_blue + 500, 295])
    else :
        screen.blit((Projectile_Blue[3]), [hadouken_x_pos_blue +500,295])
    if hadouken_x_pos_blue+680< 0:
        hadouken_x_pos_blue = 0
    hadouken_x_pos_blue -= random.randint(5,10)

    #Black Projectile after 10 seconds
    if timerCount == -1 :
        timerCount = 10*10
    if timerCount !=0:
        timerCount -=1
    else:
        if frame % 4 == 0:
            screen.blit((Projectile_Black[0]), [hadouken_x_pos_black + 500, 180])
        elif frame % 4 == 1:
            screen.blit((Projectile_Black[1]), [hadouken_x_pos_black + 500, 180])
        elif frame % 4 == 2:
            screen.blit((Projectile_Black[2]), [hadouken_x_pos_black + 500, 180])
        else:
            screen.blit((Projectile_Black[3]), [hadouken_x_pos_black + 500, 180])
        if hadouken_x_pos_black + 680 < 0:
            hadouken_x_pos_black = 0
        hadouken_x_pos_black -= random.randint(10, 25)

    #Purple projectile after 15 seconds
    if timerCount2 == -1 :
        timerCount2 = 15*10
    if timerCount2 !=0:
        timerCount2 -=1
    else:
        if frame % 4 == 0:
            screen.blit((Projectile_Purple[0]), [hadouken_x_pos_purple + 500, 50])
        elif frame % 4 == 1:
            screen.blit((Projectile_Purple[1]), [hadouken_x_pos_purple + 500, 50])
        elif frame % 4 == 2:
            screen.blit((Projectile_Purple[2]), [hadouken_x_pos_purple + 500, 50])
        else:
            screen.blit((Projectile_Purple[3]), [hadouken_x_pos_purple + 500, 50])
        if hadouken_x_pos_purple + 800 < 0:
            hadouken_x_pos_purple = 0
        hadouken_x_pos_purple -= random.randint(25, 35)

    #Character animation
    if frame % 6 == 0 :
        screen.blit((Cloud[0]), [character_x_pos, character_y_pos +300])
    elif frame % 6 == 1:
        screen.blit((Cloud[1]), [character_x_pos, character_y_pos +300])
    elif frame % 6 == 2:
        screen.blit((Cloud[2]), [character_x_pos, character_y_pos +300])
    elif frame % 6 == 3:
        screen.blit((Cloud[3]), [character_x_pos, character_y_pos +300])
    elif frame % 6 == 4:
        screen.blit((Cloud[4]), [character_x_pos, character_y_pos +300])
    elif frame % 6 == 5:
        screen.blit((Cloud[5]), [character_x_pos, character_y_pos +300])
    character_x_pos += character_x_change
    character_y_pos += character_y_change

    #Jumping up and down to a timer
    if jump == True :
        character_y_change -= 1
        jump_timer += 0.2
    if jump_timer > 3:
        character_y_change += 10
        jump_timer -= 0.5

    #Stops at the ground level
    if character_y_pos + 160 + character_y_change >180:
        character_y_change = 0
        character_y_pos = 0
        jump = False
        jump_timer = 0
    #Teleporting to mouse location
    if teleport == True:
        [mouse_x, mouse_y] = pygame.mouse.get_pos()
        character_x_pos = mouse_x -100
        character_y_pos  = mouse_y - 300
        character_y_change +=10

    #Each collision for possible deaths
    death = checkCollision([character_x_pos - 30, character_y_pos +300, 160, 160], [hadouken_x_pos_blue +510, 335, 80, 131])
    death2 = checkCollision([character_x_pos -30 , character_y_pos + 300, 160, 160],[hadouken_x_pos_black + 535, 230, 45, 50])
    death3 = checkCollision([character_x_pos - 30 , character_y_pos + 300, 160, 160], [hadouken_x_pos_purple + 550, 50, 60, 125])
    score += 0.1
    if death == True:
        screen_done = True
    if death2 == True:
        screen_done = True
    if death3 == True:
        screen_done = True
    #increment frame counter
    frame += 1
    pygame.display.flip()

    # --- Limit to 10 frames per second
    clock.tick(10)

#End screen loop
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    #White background
    screen.fill(WHITE)

    #Showing the final death screen
    screen.blit((Game_Over), [75, 75])
    screen.blit((font.render("You can't cause you're bad!", True, BLACK)), [175, 325])
    screen.blit((font.render("Score:" + str(int(score))  , True, BLACK)), [275, 350])

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
