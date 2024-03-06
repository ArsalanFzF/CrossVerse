# Code needs to be rewritten 
import pygame
import sys
from pygame import mixer
from character import character

mixer.init()
pygame.init()


def MainGame():
  
  player1 = str(input("Enter player1's name: "))
  player2 = str(input("Enter player2's name: "))  
  p1 = player1 + ":"
  p2 = player2 + ":"
 # Check if the input is an integer
  try:
    player1_number = int(player1)
    print("Player1's name is a number:", player1_number)
    pygame.quit()
    sys.exit()
  except ValueError:
    print("Player1 has a valid names")

  try:
    player2_number = int(player2)
    print("Player2's name is a number:", player2_number)
    pygame.quit()
    sys.exit()
  except ValueError:
    print("Player2 has a valid name")

  #define the screen size
  SCREEN_W, SCREEN_H  = 1500, 800
  screen = pygame.display.set_mode((SCREEN_W - 10, SCREEN_H - 50))
  #create game window
  pygame.display.set_caption("CrossVerse")

  #set framerate
  clock = pygame.time.Clock()
  FPS = 60

  #define colours
  LIGHT_RED = (251, 101, 64)
  RED = (255, 0, 0)
  YELLOW = (255, 255, 0)
  WHITE = (255, 255, 255)
  GREEN = (0, 255, 97)

  #define game variables
  intro_count = 3
  last_count_update = pygame.time.get_ticks()
  score = [0, 0]#player scores. [P1, P2]
  round_over = False
  ROUND_OVER_COOLDOWN = 2000

  #define fighter variables
  WARRIOR_SIZE = 162
  WARRIOR_SCALE = 4
  WARRIOR_OFFSET = [72, 56]
  WARRIOR_DATA = [WARRIOR_SIZE, WARRIOR_SCALE, WARRIOR_OFFSET]
  WIZARD_SIZE = 250
  WIZARD_SCALE = 3
  WIZARD_OFFSET = [112, 107]
  WIZARD_DATA = [WIZARD_SIZE, WIZARD_SCALE, WIZARD_OFFSET]

  #load music and sounds
  pygame.mixer.music.load("assets/audio/music.mp3")
  pygame.mixer.music.set_volume(0.1)
  pygame.mixer.music.play(-1, 0.0, 5000)
  sword_fx = pygame.mixer.Sound("assets/audio/sword.wav")
  sword_fx.set_volume(0.5)
  magic_fx = pygame.mixer.Sound("assets/audio/magic.wav")
  magic_fx.set_volume(0.75)

  #load background image
  bg_image = pygame.image.load("assets/images/background/background.jpg").convert_alpha()

  #load spritesheets
  warrior_sheet = pygame.image.load("assets/images/warrior/Sprites/warrior.png").convert_alpha()
  wizard_sheet = pygame.image.load("assets/images/wizard/Sprites/wizard.png").convert_alpha()

  #load vicory image
  victory_img = pygame.image.load("assets/images/icons/victory.png").convert_alpha()

  #define number of steps in each animation
  WARRIOR_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]
  WIZARD_ANIMATION_STEPS = [8, 8, 1, 8, 8, 3, 7]

  #define font
  count_font = pygame.font.Font("assets/fonts/font.ttf", 120)
  score_font = pygame.font.Font("assets/fonts/font.ttf", 30)

  #function for drawing text
  def draw_text(p1, font, text_col, x, y):
    img = font.render(p1, True, text_col)
    screen.blit(img, (x, y))

  #function for drawing background
  def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_W, SCREEN_H))
    screen.blit(scaled_bg, (0, 0))

  #function for drawing fighter health bars
  def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 24))
    pygame.draw.rect(screen, LIGHT_RED, (x, y, 400, 20))
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 20))


  #create two instances of fighters
  Player_1 = character(1, SCREEN_W - SCREEN_W + 500, 510, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
  Player_2 = character(2, SCREEN_W - 500, 510, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

  #game loop
  run = True
  while run:

    clock.tick(FPS)

    #draw background
    draw_bg()

    #show player stats
    draw_health_bar(Player_1.health, SCREEN_W - SCREEN_W +20, 20)
    draw_health_bar(Player_2.health, SCREEN_W - 430, 20)
    draw_text( p1 + str(score[0]), score_font, RED, SCREEN_W - SCREEN_W + 20, 50)
    draw_text( p2 + str(score[1]), score_font, RED, SCREEN_W - 430, 50)

    #update countdown
    if intro_count <= 0:
      #move fighters
      Player_1.move(SCREEN_W, SCREEN_H, screen, Player_2, round_over)
      Player_2.move(SCREEN_W, SCREEN_H, screen, Player_1, round_over)
    else:
      #display count timer
      draw_text(str(intro_count), count_font, RED, SCREEN_W / 2, SCREEN_H / 3)
      #update count timer
      if (pygame.time.get_ticks() - last_count_update) >= 1000:
        intro_count -= 1
        last_count_update = pygame.time.get_ticks()

    #update fighters
    Player_1.update()
    Player_2.update()

    #draw fighters
    Player_1.draw(screen)
    Player_2.draw(screen)

    #check for player defeat
    if round_over == False:
      if Player_1.alive == False:
        score[1] += 1
        round_over = True
        round_over_time = pygame.time.get_ticks()
      elif Player_2.alive == False:
        score[0] += 1
        round_over = True
        round_over_time = pygame.time.get_ticks()
    else:
      #display victory image
      screen.blit(victory_img, (SCREEN_W /2 - 135 , SCREEN_H / 3))
      if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
        round_over = False
        intro_count = 3
        Player_1 = character(1, SCREEN_W - SCREEN_W + 500, 510, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
        Player_2 = character(2, SCREEN_W - 500, 510, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)
    #event handler
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      
        
    pygame.display.update()

  #exit pygame
  pygame.quit()

MainGame()