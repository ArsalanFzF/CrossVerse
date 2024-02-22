# Code needs to be rewritten 
import pygame
import sys
import os
from pygame import mixer
from fighter import Fighter

mixer.init()
pygame.init()

'''player1 = input("Enter player1's name: ")
player2 = input("Enter player2's name: ")'''

def MainGame():

  os.environ['SDL_VIDEO_CENTERED'] = '1'
  info = pygame.display.Info()
  SCREEN_WIDTH, SCREEN_HEIGHT  = 1500, 800

  screen = pygame.display.set_mode((SCREEN_WIDTH - 10, SCREEN_HEIGHT - 50))
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
  count_font = pygame.font.Font("assets/fonts/turok.ttf", 80)
  score_font = pygame.font.Font("assets/fonts/turok.ttf", 30)

  #function for drawing text
  def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

  #function for drawing background
  def draw_bg():
    scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_bg, (0, 0))

  #function for drawing fighter health bars
  def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 2, y - 2, 404, 24))
    pygame.draw.rect(screen, LIGHT_RED, (x, y, 400, 20))
    pygame.draw.rect(screen, GREEN, (x, y, 400 * ratio, 20))


  #create two instances of fighters
  fighter_1 = Fighter(1, SCREEN_WIDTH - SCREEN_WIDTH + 500, 510, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
  fighter_2 = Fighter(2, SCREEN_WIDTH - 500, 510, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)

  #game loop
  run = True
  while run:

    clock.tick(FPS)

    #draw background
    draw_bg()

    #show player stats
    draw_health_bar(fighter_1.health, SCREEN_WIDTH - SCREEN_WIDTH +20, 20)
    draw_health_bar(fighter_2.health, SCREEN_WIDTH - 430, 20)
    draw_text("P1: " + str(score[0]), score_font, RED, SCREEN_WIDTH - SCREEN_WIDTH +20, 50)
    draw_text("P2: " + str(score[1]), score_font, RED, SCREEN_WIDTH - 85, 50)

    #update countdown
    if intro_count <= 0:
      #move fighters
      fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
      fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
    else:
      #display count timer
      draw_text(str(intro_count), count_font, RED, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
      #update count timer
      if (pygame.time.get_ticks() - last_count_update) >= 1000:
        intro_count -= 1
        last_count_update = pygame.time.get_ticks()

    #update fighters
    fighter_1.update()
    fighter_2.update()

    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)

    #check for player defeat
    if round_over == False:
      if fighter_1.alive == False:
        score[1] += 1
        round_over = True
        round_over_time = pygame.time.get_ticks()
      elif fighter_2.alive == False:
        score[0] += 1
        round_over = True
        round_over_time = pygame.time.get_ticks()
    else:
      #display victory image
      screen.blit(victory_img, (SCREEN_WIDTH /2 - 135 , SCREEN_HEIGHT / 3))
      if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
        round_over = False
        intro_count = 3
        fighter_1 = Fighter(1, SCREEN_WIDTH - SCREEN_WIDTH + 500, 510, False, WARRIOR_DATA, warrior_sheet, WARRIOR_ANIMATION_STEPS, sword_fx)
        fighter_2 = Fighter(2, SCREEN_WIDTH - 500, 510, True, WIZARD_DATA, wizard_sheet, WIZARD_ANIMATION_STEPS, magic_fx)
    #event handler
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False
      '''if event.type == pygame.VIDEORESIZE:
        screen = pygame.display.set_mode((event.w, event.h), pygame.FULLSCREEN)'''



    #update display
    pygame.display.update()

  #exit pygame
  pygame.quit()

def Menu():

    # Initialize Pygame
    pygame.init()

    # Set up display
    width, height = 1500, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("CrossVerse Menu")

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (192, 192, 192)
    blue = (19, 195, 247)
    red = (251, 101, 64)
    green = (0, 255, 97)

    # Fonts
    font = pygame.font.Font(None, 36)

    # Button class
    class Button:
        def __init__(self, text, x, y, width, height, color, hover_color, action):
            self.rect = pygame.Rect(x *2+50, y+ 50, width, height)
            self.color = color
            self.hover_color = hover_color
            self.text = text
            self.action = action

        def draw(self):
            pygame.draw.rect(screen, self.color, self.rect)
            pygame.draw.rect(screen, black, self.rect, 2)

            # Center the text
            text_surface = font.render(self.text, True, black)
            text_rect = text_surface.get_rect(center=self.rect.center)
            screen.blit(text_surface, text_rect)

        def is_hovered(self):
            return self.rect.collidepoint(pygame.mouse.get_pos())

    # Main menu buttons
    start_button = Button("Start", 300, 200, 200, 50, gray, red, "start")
    credit_button = Button("Credit", 300, 300, 200, 50, gray, red, "credit")
    quit_button = Button("Quit", 300, 400, 200, 50, gray, red, "quit")

    buttons = [start_button, credit_button, quit_button]

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for button in buttons:
                    if button.is_hovered():
                        if button.action == "start":
                            MainGame()
                        elif button.action == "credit":
                            print("Credit button clicked")
                            # Add your credit button action here
                        elif button.action == "quit":
                            pygame.quit()
                            sys.exit()

        bg_image = pygame.image.load("menu_assets/bg.png").convert_alpha()
        
        def draw_background():
            scaled_bg = pygame.transform.scale(bg_image, (width, height))
            screen.blit(scaled_bg, (0, 0))
        
        draw_background()

        for button in buttons:
            if button.is_hovered():
                button.color = button.hover_color
            else:
                button.color = gray
            button.draw()

        pygame.display.flip()
    
Menu()