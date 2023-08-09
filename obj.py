import pygame, sys
import settings

class ball():

    def __init__(self, radius, position, velocity, name, color):

        self.name = name
        self.color = color
        
        self.radius = radius
        
        self.position = position
        self.xPos, self.yPos = self.position

        self.velocity = velocity
        self.xVel, self.yVel = self.velocity

        self.rect = pygame.Rect(self.xPos, self.yPos, self.radius, self.radius)

    def render(self, screen):
        
        self.rect = pygame.Rect(self.xPos, self.yPos, self.radius, self.radius)
        self.draw = pygame.draw.rect(screen, self.color, self.rect)


    def update(self):

        self.position += self.velocity
        self.xPos, self.yPos = self.position

        self.velocity += pygame.Vector2(0, settings.GRAVITY) / settings.MAX_FRAMERATE
        self.xVel, self.yVel = self.velocity



class wall():

    def __init__(self, size, position, name, color):

        self.name = name
        self.color = color
        
        self.size = size
        self.xSize, self.ySize = size
        
        self.position = position
        self.xPos, self.yPos = self.position

        self.rect = pygame.Rect(self.xPos, self.yPos, self.xSize, self.ySize)

    def render(self, screen):

        self.rect = pygame.Rect(self.xPos, self.yPos, self.xSize, self.ySize)
        self.draw = pygame.draw.rect(screen, self.color, self.rect)