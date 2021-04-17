import tkinter
import pygame
import random
import math


pygame.init()
pygame.font.init()
clock = pygame.time.Clock()
score = 0


WINDOW_SIZE = (500,500)
BACKGROUND_COLOR = (255,192,203)
BLACK= (0,0,0)
BLUE = (0,0,255)
GRAY = (128,128,128)
food_color = (198,198,198) 

player_speed = 10
player_x = 10
player_y = 410
playerleft = False

food_x = random.randint(30, 450)
food_y = 100



scorefont = pygame.font.SysFont('Comic Sans MS', 30)
programIcon = pygame.image.load("assets/player.png")
pygame.display.set_icon(programIcon)
pygame.display.set_caption("Catch to foods")

window = pygame.display.set_mode(WINDOW_SIZE)
food = pygame.image.load("assets/banana.png")
food = pygame.transform.scale(food, (50,50))
player_right = pygame.image.load("assets/player.png")
player_left = pygame.image.load("assets/player.png")

player_right = pygame.transform.scale(player_right, (70,70))
   
player_left = pygame.transform.scale(player_left, (70,70))
   
# player movement functions
def moveplayer_right():
    global player_x



def moveplayer_left():
    global player_x
    player_x -= player_speed

# colision detection function 
def hascolided(playerx, playery, foodx,foody, ofset):
    distance = math.sqrt(math.pow( foodx - playerx ,2) + math.pow( foody - playery ,2))
    if distance <ofset:
        colision = True
    else:
        colision = False
    return colision

# main game loop function
game_state_running = True

while game_state_running:
    # drawingbackground
    window.fill(BACKGROUND_COLOR)
    # drawing base
    pygame.draw.rect(window, GRAY, pygame.Rect(0, 450, 500, 50)) 
    window.blit(food, (food_x, food_y))
    # player
    if playerleft:
        window.blit(player_left, (player_x, player_y))
    elif not(playerleft):
        window.blit(player_right, (player_x, player_y))
    for event in pygame.event.get():
        # checking if the player wants to quit or not 
        if event.type == pygame.QUIT:
            game_state_running = False

    # checking for any keypresses
    keys = pygame.key.get_pressed()  
    if keys[pygame.K_LEFT]: 
        playerleft = True
        player_x -= player_speed

    if keys[pygame.K_RIGHT]:
        playerleft = False
        player_x += player_speed

    if player_x <0:
        player_x = 0

    if player_x >450:
        player_x = 450

    if hascolided(player_x,player_y, food_x, food_y, 50):
        score +=1
        food_y = 100
        food_x = random.randint(30, 450)

    if food_y >450:
        if not(score ==0):
            score -=1
        food_y = 100
        food_x = random.randint(30, 450)


    # checking if food is out of the screen
    text_score = scorefont.render(str(score), True, (255,0,0), BACKGROUND_COLOR)
    window.blit(text_score, (250, 50))
    
    credit = scorefont.render("Made by Prabesh Shrestha", True, (255,0,0), BACKGROUND_COLOR)
    window.blit(credit, (70, 10))
    # print("speed added")
    food_y +=10
    #fps set of game screen
    pygame.display.update()
    clock.tick(30)
    