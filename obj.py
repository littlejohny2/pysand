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

    def render(self, screen):
        
        self.draw = pygame.draw.circle(screen, self.color, self.position, self.radius)


    def update(self):

        self.position += self.velocity
        self.velocity += pygame.Vector2(0, settings.GRAVITY) / settings.MAX_FRAMERATE



class wall():

    def __init__(self, size, position, name, color):

        self.name = name
        self.color = color
        
        self.size = size
        self.xSize, self.ySize = size
        
        self.position = position
        self.xPos, self.yPos = self.position

    def render(self, screen):

        self.rect = pygame.Rect(self.xPos, self.yPos, self.xSize, self.ySize)
        self.draw = pygame.draw.rect(screen, self.color, self.rect)