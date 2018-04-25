import random
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
        particles.append(particle)
    return particles