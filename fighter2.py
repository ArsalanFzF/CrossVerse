'''import pygame

class Fighter2():
    def __init__(self, x, y):
        self.rect = pygame.Rect((x, y, 80, 180))
        self.vel_y = 0
        self.jump = False
        self.attacking = False
        self.attack_type = 0

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        GRAVITY = 2
        dx = 0
        dy = 0

        #get keypresses
        key = pygame.key.get_pressed()

        #can only perform other actions of currently not attacking
        #if self.attacking == False:
            
        #movement
        if key[pygame.K_LEFT]:
            dx = -SPEED
        if key[pygame.K_RIGHT]:
            dx = SPEED
        #jump
        if key[pygame.K_UP] and self.jump == False:
            self.vel_y = -30
            self.jump = True
        #attack
        if key[pygame.K_KP_1] or key[pygame.K_KP_2]:
            self.attack(surface, target)
            #determine which attack has been pressed
            if key[pygame.K_KP_1]:
                self.attack_type = 1
            if key[pygame.K_KP_2]:
                self.attack_type = 2


        #apply gravity
        self.vel_y += GRAVITY
        dy += self.vel_y

        #ensure player stays on screen
        if self.rect.left + dx < 0:
            dx =  - self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 70:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 70 - self.rect.bottom

        #update player position
        self.rect.x += dx
        self.rect.y += dy

    def attack(self, surface, target):
        attacking_rect = pygame.Rect(self.rect.centerx, self.rect.y, -2 * self.rect.width, self.rect.height)
        if attacking_rect.colliderect(target.rect):
            print("HIT")
        pygame.draw.rect(surface, (0, 255, 0), attacking_rect)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), self.rect)'''