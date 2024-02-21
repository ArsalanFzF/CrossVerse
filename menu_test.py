import pygame
import sys
from fighter import Fighter



def MainGame():
    #game window
    SCREEN_WIDTH = 1000
    SCREEN_HEIGHT = 600
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("CrossVerse")
     
    #set framerate
    clock = pygame.time.Clock()
    FPS = 60
     
    #define colours
    RED = (255, 0, 0)    
    WHITE = (255, 255, 255)
    YELLOW = (255, 255, 0)

    #load background image
    bg_image = pygame.image.load("assets/images/background/bg.jpg").convert_alpha()
     
    #function for drawing background
    def draw_bg():
        scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.blit(scaled_bg, (0, 0))
          
    #function for drawing fighter health bars
    def draw_health_bar(health, x, y):
        ratio = health / 1000
        pygame.draw.rect(screen, WHITE, (x-2, y-2, 404, 34))
        pygame.draw.rect(screen, RED, (x, y, 400, 30))
        pygame.draw.rect(screen, YELLOW, (x, y, 400 * ratio, 30))

            
    #create two instanecs of fighters
    fighter_1 = Fighter(300, 310)
    fighter_2 = Fighter(800, 310)
     
    #game loop
    run = True
    while run:
        clock.tick(FPS)
        
        #draw background
        draw_bg()
          
        #show player stats
        draw_health_bar(fighter_1.health, 20, 20)
        draw_health_bar(fighter_2.health, 580, 20)

        #move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
          
        #draw fighters
        fighter_1.draw(screen)
        fighter_2.draw(screen)
          
        #event handle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                    
        #update display
        pygame.display.update()
          
    #exit pygame
    pygame.quit()


def Menu():

    # Initialize Pygame
    pygame.init()

    # Set up display
    width, height = 800, 600
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Main Menu")

    # Colors
    white = (255, 255, 255)
    black = (0, 0, 0)
    gray = (192, 192, 192)

    # Fonts
    font = pygame.font.Font(None, 36)

    # Button class
    class Button:
        def __init__(self, text, x, y, width, height, color, hover_color, action):
            self.rect = pygame.Rect(x, y, width, height)
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
    start_button = Button("Start", 300, 200, 200, 50, gray, white, "start")
    credit_button = Button("Credit", 300, 300, 200, 50, gray, white, "credit")
    quit_button = Button("Quit", 300, 400, 200, 50, gray, white, "quit")

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
                            print("Start button clicked")
                            MainGame()
                        elif button.action == "credit":
                            print("Credit button clicked")
                            # Add my credit button action here
                        elif button.action == "quit":
                            print("Quit button clicked")
                            pygame.quit()
                            sys.exit()

        screen.fill(white)

        for button in buttons:
            if button.is_hovered():
                button.color = button.hover_color
            else:
                button.color = gray
            button.draw()

        pygame.display.flip()
    
Menu()