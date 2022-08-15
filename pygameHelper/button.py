import pygame
import math
class Button:
    
    # AU = 149.6e6 * 1000
    SCALE = 0.1

    def __init__(self, x, y, image):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * self.SCALE), int(height * self.SCALE)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self, screen):
        action = False
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.image, (self.rect.x, self.rect.y))

        return action