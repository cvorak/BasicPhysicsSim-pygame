import random
import math
from particle import Particle

def generate_particles(screen, num_of_particles):
    """Generate particles with random positions and sizes on screen."""
    width = screen.get_rect().width
    height = screen.get_rect().height
    particles = []
    for n in range(num_of_particles):
        size = random.randint(10, 40)
        x = random.randint(size, width - size)
        y = random.randint(size, height - size)

        particle = Particle(screen, (x, y), size)
        # Random speed 0 to 1
        particle.speed = random.random()
        # Random direction
        particle.angle = random.uniform(0, math.pi * 2)

        particles.append(particle)
    return particles