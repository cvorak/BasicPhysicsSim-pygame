import pygame
import math
class Particle:
    def __init__(self, screen, position, size):
        self.screen = screen
        self.size = size
        (self.x, self.y) = position        
        self.color = (0, 0, 255)
        self.thickness = 1

        # Speed and direction parameters
        self.speed = 0.01
        self.angle = math.pi / 2

    def display(self):
        pygame.draw.circle(self.screen, self.color, (int(self.x), int(self.y)), 
            self.size, self.thickness)

    def move(self):
        self.x += math.sin(self.angle) * self.speed
        self.y -= math.cos(self.angle) * self.speed
        
