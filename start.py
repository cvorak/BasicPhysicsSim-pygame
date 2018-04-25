import pygame
import random
import helpers as hp
from particle import Particle

# Set screen properties.
(width, height) = (800, 600)
bg_color = (255, 255, 255)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Physics')
screen.fill(bg_color)

particles = hp.generate_particles(screen, 50)

for particle in particles:
    particle.display()

pygame.display.flip()

# Start main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
