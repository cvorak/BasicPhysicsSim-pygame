import pygame

class Particle:
    def __init__(self, screen, position, size):
        self.screen = screen
        self.size = size
        self.position = position
        self.color = (0, 0, 255)
        self.thickness = 1

    def display(self):
        pygame.draw.circle(self.screen, self.color, self.position, 
            self.size, self.thickness)