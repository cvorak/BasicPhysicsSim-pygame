import pygame
from particle import Particle

# Set screen properties.
(width, height) = (800, 600)
bg_color = (255, 255, 255)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Physics')
screen.fill(bg_color)

particle = Particle(screen, (150, 50), 40)
particle.display()

pygame.display.flip()

# Start main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
