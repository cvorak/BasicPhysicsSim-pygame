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

    def check_edges(self, screen):
        # Get screen dimensions
        width = screen.get_rect().width
        height = screen.get_rect().height

        # Right and left edge
        if self.x > width - self.size or self.x < self.size:
            self.angle = - self.angle
        # Top and bottom edge
        if self.y < self.size or self.y > height - self.size:
            self.angle = math.pi - self.angle
        