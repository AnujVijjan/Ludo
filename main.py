from pygame import *
import math, random
import pygame

# Initialize Pygame
pygame.init()

# Create a screen
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

SPEED = 30

welcomeScreenImage = pygame.image.load('Images/welcomeScreen.jpg')
ludoLogo = pygame.image.load('Images/logo.png')
# Player 
blue1 = pygame.image.load('Images/BlueTokens/blue_token1.png')
blue2 = pygame.image.load('Images/BlueTokens/blue_token2.png')
blue3 = pygame.image.load('Images/BlueTokens/blue_token3.png')
blue4 = pygame.image.load('Images/BlueTokens/blue_token4.png')

red1 = pygame.image.load('Images/RedTokens/red_token1.png')
red2 = pygame.image.load('Images/RedTokens/red_token2.png')
red3 = pygame.image.load('Images/RedTokens/red_token3.png')
red4 = pygame.image.load('Images/RedTokens/red_token4.png')

green1 = pygame.image.load('Images/GreenTokens/green_token1.png')
green2 = pygame.image.load('Images/GreenTokens/green_token2.png')
green3 = pygame.image.load('Images/GreenTokens/green_token3.png')
green4 = pygame.image.load('Images/GreenTokens/green_token4.png')

yellow1 = pygame.image.load('Images/YellowTokens/yellow_token1.png')
yellow2 = pygame.image.load('Images/YellowTokens/yellow_token2.png')
yellow3 = pygame.image.load('Images/YellowTokens/yellow_token3.png')
yellow4 = pygame.image.load('Images/YellowTokens/yellow_token4.png')

# Background
background = pygame.image.load('Images/board.jpeg')

# Dice
dice1 = pygame.image.load('Images/DiceImages/dice1.jpeg')
dice2 = pygame.image.load('Images/DiceImages/dice2.jpeg')
dice3 = pygame.image.load('Images/DiceImages/dice3.jpeg')
dice4 = pygame.image.load('Images/DiceImages/dice4.jpeg')
dice5 = pygame.image.load('Images/DiceImages/dice5.jpeg')
dice6 = pygame.image.load('Images/DiceImages/dice6.jpeg')

# Safe Zone
safe_zone_image = pygame.image.load('Images/safe_zone_image.jpg')

# Crown Images
crown_image_1 = pygame.image.load('Images/CrownImages/crown1.png')
crown_image_2 = pygame.image.load('Images/CrownImages/crown2.png')
crown_image_3 = pygame.image.load('Images/CrownImages/crown3.png')
loser_image = pygame.image.load('Images/CrownImages/loser.png')

player1_color, player2_color, player3_color, player4_color = (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)

chance, num, current_player_points = 'red', 0, (228, 9)

red_index, yellow_index, blue_index, green_index = 'First', 'First', 'First', 'First'

player1_name, player2_name, player3_name, player4_name = ['Player 1'], ['Player 2'], ['Player 3'], ['Player 4']

FONT = pygame.font.SysFont('Arial', 20, 'b')

FPSCLOCK = pygame.time.Clock()

red_position = {'First' : -1, 'Second' : -1, 'Third' : -1, 'Fourth' : -1}
blue_position = {'First' : -1, 'Second' : -1, 'Third' : -1, 'Fourth' : -1}
green_position = {'First' : -1, 'Second' : -1, 'Third' : -1, 'Fourth' : -1}
yellow_position = {'First' : -1, 'Second' : -1, 'Third' : -1, 'Fourth' : -1}

GAME_SPRITES = {'blueFirst' : (565, 420), 'blueSecond' : (445, 420), 'blueThird' : (445, 540), 'blueFourth' : (565, 540),
                'greenFirst' : (205, 540), 'greenSecond' : (205, 420), 'greenThird' : (85, 420), 'greenFourth' : (85, 540),
                'redFirst' : (85, 180), 'redSecond' : (205, 180), 'redThird' : (205, 60), 'redFourth' : (85, 60),
                'yellowFirst' : (445, 60), 'yellowSecond' : (445, 180), 'yellowThird' : (565, 180), 'yellowFourth' : (565, 60)}

# Safe Zone positions.
safe_position = [0, 8, 13, 21, 26, 34, 39, 47]

# Player 1 route.
player1_track = [(85, 260), (125, 260), (165, 260), (205, 260), (245, 260), (285, 220), (285, 180), (285, 140), (285, 100), (285, 60), (285, 20),
                (325, 20), (365, 20), (365, 60), (365, 100), (365, 140), (365, 180), (365, 220), (405, 260), (445, 260), (485, 260), (525, 260), (565, 260),
                (605, 260), (605, 300), (605, 340), (565, 340), (525, 340), (485, 340), (445, 340), (405, 340), (365, 380), (365, 420), (365, 460), (365, 500), (365, 540), (365, 580), 
                (325, 580), (285, 580), (285, 540), (285, 500), (285, 460), (285, 420), (285, 380), (245, 340), (205, 340), (165, 340), (125, 340), (85, 340), (45, 340),
                (45, 300), (85, 300), (125, 300), (165, 300), (205, 300), (245, 300), (285, 300)]

# Player 2 route.
player2_track = [(365, 60), (365, 100), (365, 140), (365, 180), (365, 220), (405, 260), (445, 260), (485, 260), (525, 260), (565, 260),
                (605, 260), (605, 300), (605, 340), (565, 340), (525, 340), (485, 340), (445, 340), (405, 340), (365, 380), (365, 420), (365, 460), (365, 500), (365, 540), 
                (365, 580), (325, 580), (285, 580), (285, 540), (285, 500), (285, 460), (285, 420), (285, 380), (245, 340), (205, 340), (165, 340), (125, 340), (85, 340), 
                (45, 340), (45, 300), (45, 260), (85, 260), (125, 260), (165, 260), (205, 260), (245, 260), (285, 220), (285, 180), (285, 140), (285, 100), (285, 60), 
                (285, 20), (325, 20), (325, 60), (325, 100), (325, 140), (325, 180), (325, 220), (325, 260)]

# Player 3 route.
player3_track = [(565, 340), (525, 340), (485, 340), (445, 340), (405, 340), (365, 380), (365, 420), (365, 460), (365, 500), (365, 540), (365, 580), (325, 580), 
                (285, 580), (285, 540), (285, 500), (285, 460), (285, 420), (285, 380), (245, 340), (205, 340), (165, 340), (125, 340), (85, 340), (45, 340),
                (45, 300), (45, 260), (85, 260), (125, 260), (165, 260), (205, 260), (245, 260), (285, 220), (285, 180), (285, 140), (285, 100), (285, 60), (285, 20),
                (325, 20), (365, 20), (365, 60), (365, 100), (365, 140), (365, 180), (365, 220), (405, 260), (445, 260), (485, 260), (525, 260), (565, 260),
                (605, 260), (605, 300), (565, 300), (525, 300), (485, 300), (445, 300), (405, 300), (365, 300)]

# Player 4 route.
player4_track = [(285, 540), (285, 500), (285, 460), (285, 420), (285, 380), (245, 340), (205, 340), (165, 340), (125, 340), (85, 340), (45, 340),
                (45, 300), (45, 260), (85, 260), (125, 260), (165, 260), (205, 260), (245, 260), (285, 220), (285, 180), (285, 140), (285, 100), (285, 60), (285, 20),
                (325, 20), (365, 20), (365, 60), (365, 100), (365, 140), (365, 180), (365, 220), (405, 260), (445, 260), (485, 260), (525, 260), (565, 260),
                (605, 260), (605, 300), (605, 340), (565, 340), (525, 340), (485, 340), (445, 340), (405, 340), (365, 380), (365, 420), (365, 460), (365, 500), (365, 540), (365, 580), 
                (325, 580), (325, 540), (325, 500), (325, 460), (325, 420), (325, 380), (325, 340)]

hit = pygame.mixer.Sound('audio/hit.wav')
swoosh = pygame.mixer.Sound('audio/swoosh.wav')
win = pygame.mixer.Sound('audio/win.wav')

die_flag = False

no_of_players = 0

# Function which counts how many players are out of the home
def check():
    count, cnt = 0, 0
    if(chance == 'red'):
        position = red_position
    elif(chance == 'blue'):
        position = blue_position
    elif(chance == 'yellow'):
        position = yellow_position
    elif(chance == 'green'):
        position = green_position

    for value in position.values():
        if(value != -1):
            count += 1
        if(value == 56):
            cnt += 1

    return (count - cnt)

# This function will blit all tokens to the give positions.
def blit_tokens():
    # For Blue
    screen.blit(blue1, GAME_SPRITES['blueFirst'])   # First
    screen.blit(blue2, GAME_SPRITES['blueSecond'])   # Second
    screen.blit(blue3, GAME_SPRITES['blueThird'])   # Third
    screen.blit(blue4, GAME_SPRITES['blueFourth'])   # Fourth
    # For Green
    screen.blit(green1, GAME_SPRITES['greenFirst'])   # First
    screen.blit(green2, GAME_SPRITES['greenSecond'])   # Second
    screen.blit(green3, GAME_SPRITES['greenThird'])   # Third
    screen.blit(green4, GAME_SPRITES['greenFourth'])   # Fourth
    # For Red
    screen.blit(red1, GAME_SPRITES['redFirst'])   # First
    screen.blit(red2, GAME_SPRITES['redSecond'])   # Second
    screen.blit(red3, GAME_SPRITES['redThird'])   # Third
    screen.blit(red4, GAME_SPRITES['redFourth'])   # Fourth
    # For Yellow
    screen.blit(yellow1, GAME_SPRITES['yellowFirst'])   # First
    screen.blit(yellow2, GAME_SPRITES['yellowSecond'])   # Second
    screen.blit(yellow3, GAME_SPRITES['yellowThird'])   # Third
    screen.blit(yellow4, GAME_SPRITES['yellowFourth'])   # Fourth

def textObject(text, font, text_color):
        myText = font.render(text, True, text_color)
        return myText, myText.get_rect()

def message_to_screen(msg, color, font, x, y):
    TextSurface, TextRect = textObject(msg, font, color)
    screen.blit(TextSurface, (x, y))

# This function is used for blitting all the player names to the screen.
def blit_tokens_names():
    message_to_screen(''.join(player1_name), player1_color, FONT, 130, 30)
    message_to_screen(''.join(player2_name), player2_color, FONT, 490, 30)
    message_to_screen(''.join(player3_name), player3_color, FONT, 490, 660)
    message_to_screen(''.join(player4_name), player4_color, FONT, 130, 660)

# This function will generate a random number and will also return it.
def get_random_number():
    return random.randint(1, 6)

# This function will give you option to choose a perticular tokens among all.
def give_options(index):
    global red_index, yellow_index, blue_index, green_index  
    b = True
    while(b):
        for event in pygame.event.get():
            if(event.type == QUIT):
                b = False
            elif(event.type == pygame.KEYDOWN):
                if(num != 6):
                    if(event.key == K_1 and position['First'] not in [56, -1]):
                        index, b = 'First', False
                    elif(event.key == K_2 and position['Second'] not in [56, -1]):
                        index, b = 'Second', False
                    elif(event.key == K_3 and position['Third'] not in [56, -1]):
                        index, b = 'Third', False
                    elif(event.key == K_4 and position['Fourth'] not in [56, -1]):
                        index, b = 'Fourth', False
                else:
                    if(event.key == K_1 and position['First'] != 56):
                        index, b = 'First', False
                    elif(event.key == K_2 and position['Second'] != 56):
                        index, b = 'Second', False
                    elif(event.key == K_3 and position['Third'] != 56):
                        index, b = 'Third', False
                    elif(event.key == K_4 and position['Fourth'] != 56):
                        index, b = 'Fourth', False

    if(chance == 'red'):
        red_index = index
        return red_index
    elif(chance == 'yellow'):
        yellow_index = index  
        return yellow_index
    elif(chance == 'blue'):
        blue_index = index
        return blue_index
    else:
        green_index = index
        return green_index

die_flag = False
# This function will change the current position of a token back to the home.
def change_the_position_of_token_to_home(key, flag, position, first, second, third, fourth):
    global die_flag
    if(key == 'First'): 
        GAME_SPRITES[flag + 'First'], position['First'] = first, -1
    elif(key == 'Second'): 
        GAME_SPRITES[flag + 'Second'], position['Second'] = second, -1
    elif(key == 'Third'): 
        GAME_SPRITES[flag + 'Third'], position['Third'] = third, -1
    elif(key == 'Fourth'):
        GAME_SPRITES[flag + 'Fourth'], position['Fourth'] = fourth, -1
    die_flag = True

# This Function will check if any token has collide or not
def isCollide():
    # For Red
    if(chance == 'red'):
        for  rkey in red_position.keys():
            for ykey in yellow_position.keys():
                if(player1_track[red_position[rkey]] == player2_track[yellow_position[ykey]] and red_position[rkey] not in safe_position):
                    change_the_position_of_token_to_home(ykey, 'yellow', yellow_position, (445, 60), (445, 180), (565, 180), (565, 60))
                    hit.play()
            for bkey in blue_position.keys():
                if(player1_track[red_position[rkey]] == player3_track[blue_position[bkey]] and red_position[rkey] not in safe_position):
                    change_the_position_of_token_to_home(bkey, 'blue', blue_position, (565, 420), (445, 420), (445, 540), (565, 540))
                    hit.play()
            for gkey in green_position.keys():
                if(player1_track[red_position[rkey]] == player4_track[green_position[gkey]] and red_position[rkey] not in safe_position):
                    change_the_position_of_token_to_home(gkey, 'green', green_position, (205, 540), (205, 420), (85, 420), (85, 540))
                    hit.play()
                    
    # For Yellow
    if(chance == 'yellow'):
        for  ykey in yellow_position.keys():
            for rkey in red_position.keys():
                if(player2_track[yellow_position[ykey]] == player1_track[red_position[rkey]] and yellow_position[ykey] not in safe_position):
                    change_the_position_of_token_to_home(rkey, 'red', red_position, (85, 180), (205, 180), (205, 60), (85, 60))
                    hit.play()
            for bkey in blue_position.keys():
                if(player2_track[yellow_position[ykey]] == player3_track[blue_position[bkey]] and yellow_position[ykey] not in safe_position):
                    change_the_position_of_token_to_home(bkey, 'blue', blue_position, (565, 420), (445, 420), (445, 540), (565, 540))
                    hit.play()
            for gkey in green_position.keys():
                if(player2_track[yellow_position[ykey]] == player4_track[green_position[gkey]] and yellow_position[ykey] not in safe_position):
                    change_the_position_of_token_to_home(gkey, 'green', green_position, (205, 540), (205, 420), (85, 420), (85, 540))
                    hit.play()
    # For Blue
    if(chance == 'blue'):
        for  bkey in blue_position.keys():
            for rkey in red_position.keys():
                if(player3_track[blue_position[bkey]] == player1_track[red_position[rkey]] and blue_position[bkey] not in safe_position):
                    change_the_position_of_token_to_home(rkey, 'red', red_position, (85, 180), (205, 180), (205, 60), (85, 60))
                    hit.play()
            for ykey in yellow_position.keys():
                if(player3_track[blue_position[bkey]] == player2_track[yellow_position[ykey]] and blue_position[bkey] not in safe_position):
                    change_the_position_of_token_to_home(ykey, 'yellow', yellow_position, (445, 60), (445, 180), (565, 180), (565, 60))
                    hit.play()
            for gkey in green_position.keys():
                if(player3_track[blue_position[bkey]] == player4_track[green_position[gkey]] and blue_position[bkey] not in safe_position):
                    change_the_position_of_token_to_home(gkey, 'green', green_position, (205, 540), (205, 420), (85, 420), (85, 540))
                    hit.play()
    
    # For Green
    if(chance == 'green'):
        for  gkey in green_position.keys():
            for rkey in red_position.keys():
                if(player4_track[green_position[gkey]] == player1_track[red_position[rkey]] and green_position[gkey] not in safe_position):
                    change_the_position_of_token_to_home(rkey, 'red', red_position, (85, 180), (205, 180), (205, 60), (85, 60))
                    hit.play()
            for ykey in yellow_position.keys():
                if(player4_track[green_position[gkey]] == player2_track[yellow_position[ykey]] and green_position[gkey] not in safe_position):
                    change_the_position_of_token_to_home(ykey, 'yellow', yellow_position, (445, 60), (445, 180), (565, 180), (565, 60))
                    hit.play()
            for bkey in blue_position.keys():
                if(player4_track[green_position[gkey]] == player3_track[blue_position[bkey]] and green_position[gkey] not in safe_position):
                    change_the_position_of_token_to_home(bkey, 'blue', blue_position, (565, 420), (445, 420), (445, 540), (565, 540))
                    hit.play()

# This function will return true if the token is eligible to get out from home.               
def is_eligible_to_get_out_from_home(position, index):
    if(position[index] > -1):
        return True
    else:
        return False

# This function will blit the dice number to a perticular position. Position is passed as a parameter to this function.
def blit_number_to_the_Screen(num, current_player_points):
    if(num == 1):
        screen.blit(dice1, current_player_points)
    elif(num == 2):
        screen.blit(dice2, current_player_points)
    elif(num == 3):
        screen.blit(dice3, current_player_points)
    elif(num == 4):
        screen.blit(dice4, current_player_points)
    elif(num == 5):
        screen.blit(dice5, current_player_points)
    else:
        screen.blit(dice6, current_player_points)


# This method will blit the banner image according to the variable count.
def get_the_banner_image():
    if(cnt == 1):
        return crown_image_1
    elif(cnt == 2):
        return crown_image_2
    elif(cnt == 3):
        return crown_image_3
    elif(cnt == 4):
        return loser_image


red_flag, yellow_flag, blue_flag, green_flag, cnt = 1, 1, 1, 1, 0

# This function will check if someone has won or not.
def check_winner():
    global red_flag, yellow_flag, blue_flag, green_flag, cnt

    if(red_position['First'] == 56 and red_position['Second'] == 56 and red_position['Third'] == 56 and red_position['Fourth'] == 56):
        if(red_flag):
            cnt += 1; win.play(); red_flag = 0
        screen.blit(get_the_banner_image(), (45, 80))
    if(yellow_position['First'] == 56 and yellow_position['Second'] == 56 and yellow_position['Third'] == 56 and yellow_position['Fourth'] == 56):
        if(yellow_flag):
            cnt += 1; win.play(); yellow_flag = 0
        screen.blit(get_the_banner_image(), (405, 80))
    if(blue_position['First'] == 56 and blue_position['Second'] == 56 and blue_position['Third'] == 56 and blue_position['Fourth'] == 56):
        if(blue_flag):
            cnt += 1; win.play(); blue_flag = 0
        screen.blit(get_the_banner_image(), (405, 435))
    if(green_position['First'] == 56 and green_position['Second'] == 56 and green_position['Third'] == 56 and green_position['Fourth'] == 56):
        if(green_flag):
            cnt += 1; win.play(); green_flag = 0
        screen.blit(get_the_banner_image(), (45, 435))

# This function will change the chance.
def change_the_chance(index):
    global chance, player1_color, player2_color, player3_color, player4_color, die_flag
    
    if(not die_flag):
        if(no_of_players == 4):
            if(chance == 'red' and num != 6 ):
                player1_color, player2_color, player3_color, player4_color = (0, 0, 0), (255, 255, 0), (0, 0, 0), (0, 0, 0)
                chance = 'yellow'
            elif(chance == 'yellow' and num != 6):
                player1_color, player2_color, player3_color, player4_color = (0, 0, 0), (0, 0, 0), (0, 0, 255), (0, 0, 0)
                chance = 'blue'
            elif(chance == 'blue' and num != 6):
                player1_color, player2_color, player3_color, player4_color = (0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 128, 0)
                chance = 'green'
            elif(chance == 'green' and num != 6):
                player1_color, player2_color, player3_color, player4_color = (255, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)
                chance = 'red'
        else:
            if(chance == 'red' and num != 6):
                player1_color, player3_color = (0, 0, 0), (0, 0, 255)
                chance = 'blue'
            elif(chance == 'blue' and num != 6):
                player1_color, player3_color = (255, 0, 0), (0, 0, 0)
                chance = 'red'
    else:
        die_flag = False 

# This function will blit all the dice boxes on the screen.
def show_dice_boxes():
    # Box for showing the dice near green tokens.
    pygame.draw.rect(screen, (0,255,0), (225, 660, 75, 53))
    # Box for showing the dice near red tokens.
    pygame.draw.rect(screen, (255,0,0), (225, 7, 75, 53))
    # Box for showing the dice near yellow tokens.
    pygame.draw.rect(screen, (255,255,0), (585, 7, 75, 53))
    # Box for showing the near blue tokens.
    pygame.draw.rect(screen, (0,0,255), (585, 660, 75, 53))

def main_game():
    global position, running, num, current_player_points, GAME_SPRITES
    cheating_flag = 0
    running = True
    while running:

        screen.fill((255,255,255))
        
        # Setting the background.
        screen.blit(background, (60, 60))

        # Setting the Safe zone images.
        screen.blit(safe_zone_image, (385, 545)) # Near Blue
        screen.blit(safe_zone_image, (147, 385)) # Near Green
        screen.blit(safe_zone_image, (306, 145)) # Near Red
        screen.blit(safe_zone_image, (547, 305)) # Near Yellow

        # Calling blit_tokens function to blit all the tokens to the screen.
        blit_tokens()

        show_dice_boxes()
        
        check_winner()

        blit_tokens_names()

        for event in pygame.event.get():
            if(event.type == QUIT):
                running = False
            elif(event.type == pygame.KEYDOWN):
                
                num = get_random_number()

                if(event.key == 257):
                    cheat_num, cheating_flag = 1, 1
                elif(event.key == 258):
                    cheat_num, cheating_flag = 2, 1
                elif(event.key == 259):
                    cheat_num, cheating_flag = 3, 1
                elif(event.key == 260):
                    cheat_num, cheating_flag = 4, 1
                elif(event.key == 261):
                    cheat_num, cheating_flag = 5, 1
                elif(event.key == 262):
                    cheat_num, cheating_flag = 6, 1

                if(cheating_flag):
                    num = cheat_num

                if(event.key == K_SPACE):

                    if(chance == 'red'):
                            position, track, index, current_player_points = red_position, player1_track, red_index, (228, 9)
                    elif(chance == 'blue'):
                            position, track, index, current_player_points = blue_position, player3_track, blue_index, (588, 662)
                    elif(chance == 'yellow'):
                            position, track, index, current_player_points = yellow_position, player2_track, yellow_index, (588, 9)
                    elif(chance == 'green'):
                            position, track, index, current_player_points = green_position, player4_track, green_index, (228, 662)

                    
                    count = check()

                    for key, value in position.items():
                        if(count == 1 and value != -1):
                            index = key
    
                    blit_number_to_the_Screen(num, current_player_points)
                    
                    pygame.display.update()                       

                    if(num == 6):
                        index = give_options(index)
                        if(position[index] == -1):
                                swoosh.play()
                                position[index] = 0
                                GAME_SPRITES[chance + index] = track[position[index]]
                        else:
                            try:
                                position[index] += num
                                GAME_SPRITES[chance + index] = track[position[index]]
                            except:
                                position[index] -= num
                    else:
                        if(count > 1):
                            index = give_options(index)   
                        
                        if(is_eligible_to_get_out_from_home(position, index)):
                            try:
                                position[index] += num
                                GAME_SPRITES[chance + index] =  track[position[index]]
                            except:
                                position[index] -= num
                        
                    isCollide()
                    
                    change_the_chance(index)
                    
                    cheating_flag = 0
                    
        pygame.display.update()

def draw_rect(bx, by, width, height, color, color2, text_color, text):
    mouse = pygame.mouse.get_pos()
    if bx + width > mouse[0] > bx and by + height > mouse[1] > by:
        pygame.draw.rect(screen, color2, (bx,by,width,height))
    else:
        pygame.draw.rect(screen, color, (bx,by,width,height))
    TextSurf, TextRect = textObject(text, FONT, text_color)
    TextRect.center = ((bx + (width/2)), (by + (height/2)))
    screen.blit(TextSurf, TextRect)

def welcome_screen():

    global player1_name, player2_name, player3_name, player4_name, no_of_players

    player1TextField = {'x': 210, 'y': 350,'width': 300, 'height': 40, 'color': (255,255,255), 'color2': (192,192,192), 'text_color': (0,0,0)}
    player2TextField = {'x': 210, 'y': 400,'width': 300, 'height': 40, 'color': (255,255,255), 'color2': (192,192,192), 'text_color': (0,0,0)}
    player3TextField = {'x': 210, 'y': 450,'width': 300, 'height': 40, 'color': (255,255,255), 'color2': (192,192,192), 'text_color': (0,0,0)}
    player4TextField = {'x': 210, 'y': 500,'width': 300, 'height': 40, 'color': (255,255,255), 'color2': (192,192,192), 'text_color': (0,0,0)}
    twoPlayer = {'x': 230, 'y': 580,'width': 110, 'height': 40, 'color': (86,215,0), 'color2': (57,255,20), 'text_color': (255,255,255), 'text': "Two Player"}
    fourPlayer = {'x': 380, 'y': 580,'width': 110, 'height': 40, 'color': (86,215,0), 'color2': (57,255,20), 'text_color': (255,255,255), 'text': "Four Player"}
    startButton = {'x': 305, 'y': 650,'width': 100, 'height': 50, 'color': (86,215,0), 'color2': (57,255,20), 'text_color': (255,255,255), 'text': "Start"}

    while True:
        for event in pygame.event.get():
            # if user clicks on cross button, close the game
            if event.type == QUIT:
                pygame.quit()
                quit()
            elif event.type == MOUSEBUTTONDOWN:
                if ((pygame.mouse.get_pos()[0] > player1TextField['x'] and pygame.mouse.get_pos()[0] < player1TextField['x'] + player1TextField['width']) and
                   (pygame.mouse.get_pos()[1] > player1TextField['y'] and pygame.mouse.get_pos()[1] < player1TextField['y'] + player1TextField['height'])):
                    player1_flag, player2_flag, player3_flag, player4_flag = 1, 0, 0, 0
                elif ((pygame.mouse.get_pos()[0] > player2TextField['x'] and pygame.mouse.get_pos()[0] < player2TextField['x'] + player2TextField['width']) and
                    (pygame.mouse.get_pos()[1] > player2TextField['y'] and pygame.mouse.get_pos()[1] < player2TextField['y'] + player2TextField['height'])):
                    player1_flag, player2_flag, player3_flag, player4_flag = 0, 1, 0, 0
                elif ((pygame.mouse.get_pos()[0] > player3TextField['x'] and pygame.mouse.get_pos()[0] < player3TextField['x'] + player3TextField['width']) and
                    (pygame.mouse.get_pos()[1] > player3TextField['y'] and pygame.mouse.get_pos()[1] < player3TextField['y'] + player3TextField['height'])):
                    player1_flag, player2_flag, player3_flag, player4_flag = 0, 0, 1, 0
                elif ((pygame.mouse.get_pos()[0] > player4TextField['x'] and pygame.mouse.get_pos()[0] < player4TextField['x'] + player4TextField['width']) and
                    (pygame.mouse.get_pos()[1] > player4TextField['y'] and pygame.mouse.get_pos()[1] < player4TextField['y'] + player4TextField['height'])):
                    player1_flag, player2_flag, player3_flag, player4_flag = 0, 0, 0, 1
                elif ((pygame.mouse.get_pos()[0] > twoPlayer['x'] and pygame.mouse.get_pos()[0] < twoPlayer['x'] + twoPlayer['width']) and
                    (pygame.mouse.get_pos()[1] > twoPlayer['y'] and pygame.mouse.get_pos()[1] < twoPlayer['y'] + twoPlayer['height'])):
                        no_of_players = 2; swoosh.play()
                elif ((pygame.mouse.get_pos()[0] > fourPlayer['x'] and pygame.mouse.get_pos()[0] < fourPlayer['x'] + fourPlayer['width']) and
                    (pygame.mouse.get_pos()[1] > fourPlayer['y'] and pygame.mouse.get_pos()[1] < fourPlayer['y'] + fourPlayer['height'])):
                        no_of_players = 4; swoosh.play()
                elif ((pygame.mouse.get_pos()[0] > startButton['x'] and pygame.mouse.get_pos()[0] < startButton['x'] + startButton['width']) and
                    (pygame.mouse.get_pos()[1] > startButton['y'] and pygame.mouse.get_pos()[1] < startButton['y'] + startButton['height']) and no_of_players != 0):
                        return
                elif ((pygame.mouse.get_pos()[0] > startButton['x'] and pygame.mouse.get_pos()[0] < startButton['x'] + startButton['width']) and
                    (pygame.mouse.get_pos()[1] > startButton['y'] and pygame.mouse.get_pos()[1] < startButton['y'] + startButton['height'])):
                        hit.play()
                
            elif event.type == KEYDOWN:
                if(player1_flag == 1):
                    player1_name.append(chr(event.key))
                    if(event.key == K_BACKSPACE):
                        player1_name = player1_name[:-2]
                elif(player2_flag == 1):
                    player2_name.append(chr(event.key))
                    if(event.key == K_BACKSPACE):
                        player2_name = player2_name[:-2]
                elif(player3_flag == 1):
                    player3_name.append(chr(event.key))
                    if(event.key == K_BACKSPACE):
                        player3_name = player3_name[:-2]
                elif(player4_flag == 1):
                    player4_name.append(chr(event.key))
                    if(event.key == K_BACKSPACE):
                        player4_name = player4_name[:-2]
            else:

                screen.blit(welcomeScreenImage, (0, 0))
                screen.blit(ludoLogo, (250, 100))

                red = pygame.transform.scale(red1, (50, 50))
            
                if(no_of_players == 2):
                    blue = pygame.transform.scale(blue2, (50, 50))
                    screen.blit(red, (130, 345))
                    screen.blit(blue, (130, 395))
                
                    player2_name.clear(); player4_name.clear()
                    draw_rect(player1TextField['x'], player1TextField['y'], player1TextField['width'], player1TextField['height'], player1TextField['color'], player1TextField['color2'], player1TextField['text_color'], ''.join(player1_name))
                    draw_rect(player2TextField['x'], player2TextField['y'], player2TextField['width'], player2TextField['height'], player2TextField['color'], player2TextField['color2'], player2TextField['text_color'], ''.join(player3_name))
                elif(no_of_players == 4):
                    yellow = pygame.transform.scale(yellow2, (50, 50))
                    blue = pygame.transform.scale(blue3, (50, 50))
                    green = pygame.transform.scale(green4, (50, 50))
                    
                    screen.blit(red, (130, 345))
                    screen.blit(yellow, (130, 395))
                    screen.blit(blue, (130, 445))
                    screen.blit(green, (130, 495))
                    
                    draw_rect(player1TextField['x'], player1TextField['y'], player1TextField['width'], player1TextField['height'], player1TextField['color'], player1TextField['color2'], player1TextField['text_color'], ''.join(player1_name))
                    draw_rect(player2TextField['x'], player2TextField['y'], player2TextField['width'], player2TextField['height'], player2TextField['color'], player2TextField['color2'], player2TextField['text_color'], ''.join(player2_name))
                    draw_rect(player3TextField['x'], player3TextField['y'], player3TextField['width'], player3TextField['height'], player3TextField['color'], player3TextField['color2'], player3TextField['text_color'], ''.join(player3_name))
                    draw_rect(player4TextField['x'], player4TextField['y'], player4TextField['width'], player4TextField['height'], player4TextField['color'], player4TextField['color2'], player4TextField['text_color'], ''.join(player4_name))
                
                draw_rect(startButton['x'], startButton['y'], startButton['width'], startButton['height'], startButton['color'], startButton['color2'], startButton['text_color'], startButton['text'])
                draw_rect(twoPlayer['x'], twoPlayer['y'], twoPlayer['width'], twoPlayer['height'], twoPlayer['color'], twoPlayer['color2'], twoPlayer['text_color'], twoPlayer['text'])
                draw_rect(fourPlayer['x'], fourPlayer['y'], fourPlayer['width'], fourPlayer['height'], fourPlayer['color'], fourPlayer['color2'], fourPlayer['text_color'], fourPlayer['text'])
                pygame.display.flip() 

                pygame.display.update()
                FPSCLOCK.tick(SPEED)

# Game Loop 
if __name__ == "__main__":
    running = True
    while running:
        welcome_screen()
        main_game()
