import pygame, sys
from menu_button import Button
from fighter import Fighter
from fighter2 import Fighter2

pygame.init()

'''def MainMenu():
	screem = pygame.display.set_mode((1280, 720))
	pygame.display.set_caption("Menu")

	BG = pygame.image.load("assets/images/background/bg.jpg")

	#def get_font(size): #Returns Press-Start-2P in the desired size

	def play(): #Play screen
		pygame.display.set_caption("Play")
		
		while True:
			PLAY_MOUSE_POS = pygame.mouse.get_pos()

			screen.fill("black")

			PLAY_TEXT = get_font(45).render("This is the PLAY screen", True, "White")
			PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 460))
			screen.blit(PLAY_TEXT, PLAY_RECT)

			PLAY_BACK = Button(image=None, pos=(640, 460), 
					  			text_input="BACK", font=get_font(75), base_colour="White", hovering_colour="Green")
			

			PLAY_BACK.changeColour(PLAY_MOUSE_POS)
			PLAY_BACK.update(screen)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
						main_menu()

			pygame.display.update()
	
	def options(): #Option screen
		pygame.display.set_caption("Options")
		
		while True:
			OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

			screen.fill("white")

			OPTIONS_TEXT = get_font(45).render("This is the PLAY screen", True, "White")
			OPTIONS_RECT = PLAY_TEXT.get_rect(center=(640, 460))
			screen.blit(PLAY_TEXT, PLAY_RECT)

			OPTIONS_BACK = Button(image=None, pos=(640, 460), 
					  			text_input="BACK", font=get_font(75), base_colour="Black", hovering_colour="Green")
			

			OPTIONS_BACK.changeColour(PLAY_MOUSE_POS)
			OPTIONS_BACK.update(screen)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.MOUSEBUTTONDOWN:
					if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
						main_menu()

			pygame.display.update()
	
	def main_menu(): #Main Menu screen
		pygame.display.set_caption("Menu")

		while True:
			screen.blit(BG, (0,0))

			MENU_MOUSE_POS = pygame.mouse.get_pos()

			MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
			MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

			PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), text_input="PLAY", font=get_font(75), base_colour="#d7fcd4", hovering_colour="White")
			
			OPTION = Button(image=pygame.image.load("assets/Option Rect.png"), pos=(640, 400), text_input="OPTIONS", font=get_font(75), base_colour="#d7fcd4", hovering_colour="White")
			
			QUIT = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), text_input="QUIT", font=get_font(75), base_colour="#d7fcd4", hovering_colour="White")

			screen.blit(MENU_TEXT, MENU_RECT)

			for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
				button.changeColour(MENU_MOUSE_POS)
				button.update(screen)

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				if event.type == pygame.QUIT:
					if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
						play()
					if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
						options()
					if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
						pygame.quit()
						sys.exit()

			pygame.display.update()
	main_menu()'''


def MainGame():
	#game window
	SCREEN_WIDTH = 1500
	SCREEN_HEIGHT = 600
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	pygame.display.set_caption("CrossVerse")
	#set framerate
	clock = pygame.time.Clock()
	FPS = 60
	#load background image
	bg_image = pygame.image.load("assets/images/background/bg.jpg").convert_alpha()
	#function for drawing background
	def draw_bg():
		scaled_bg = pygame.transform.scale(bg_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
		screen.blit(scaled_bg, (0, 0))
	#create two instanecs of fighters
	fighter_1 = Fighter(300, 310)
	fighter_2 = Fighter2(1150, 310)
	#game loop
	run = True
	while run:
		clock.tick(FPS)
		#draw background
		draw_bg()
		#move fighters
		fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
		fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1)
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

MainGame()