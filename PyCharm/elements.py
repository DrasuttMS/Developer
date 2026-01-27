import constants
import pygame
import os

class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.wood = 5

        tree_path = os.path.join('Assets', 'Images', 'Objects', 'tree.png')
        self.image = pygame.image.load(tree_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constants.TREE, constants.TREE))
        self.size = self.image.get_width()

    def draw(self, screen, camera_x ,camera_y):
        #Calcular posicion en pantalla relativa a la camara
        screen_x = self.x - camera_x
        screen_y = self.y - camera_y

        #Solo dibujar si esta en pantalla
        if (screen_x + self.size >= 0 and screen_x <= constants.WIDTH and screen_y >= 0 and screen_y <= constants.HEIGHT):
            screen.blit(self.image, (screen_x, screen_y))

    def chop(self):
        if self.wood > 0:
            self.wood -= 1
            return True
        return False

class SmallStone:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.stone = 1

        small_stone_path = os.path.join('Assets', 'Images', 'Objects', 'small_stone.png')
        self.image = pygame.image.load(small_stone_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (constants.SMALL_STONE, constants.SMALL_STONE))
        self.size = self.image.get_width()

    def draw(self, screen, camera_x ,camera_y):
        # Calcular posicion en pantalla relativa a la camara
        screen_x = self.x - camera_x
        screen_y = self.y - camera_y

        # Solo dibujar si esta en pantalla
        if (screen_x + self.size >= 0 and screen_x <= constants.WIDTH and screen_y >= 0 and screen_y <= constants.HEIGHT):
            screen.blit(self.image, (screen_x, screen_y))