import pygame
import random
import helpers as hp
from particle import Particle

# Set screen properties.
(width, height) = (1200, 800)
bg_color = (255, 255, 255)


screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Physics')

particles = hp.generate_particles(screen, 10)

# Start main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(bg_color)

    for particle in particles:
        particle.move()
        particle.display()
        
    pygame.display.flip()    
