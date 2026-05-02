# Example file showing a circle moving on screen
import pygame
from collections import deque

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0.001

class celestial_bodies:
    def __init__(self, name, mass, position, velocity) -> None:
        self.name = name
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = pygame.Vector2()
        self.trail = deque(maxlen=500)

screen_middle = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

sun = celestial_bodies('sun', 10000, screen_middle, pygame.Vector2(0,0))
earth = celestial_bodies('earth', 1, pygame.Vector2(440,160), pygame.Vector2(0,500))
moon = celestial_bodies('moon', 0.5, pygame.Vector2(), pygame.Vector2(0,0))
        
G = 10000
M_ES = G * sun.mass * earth.mass # Numerator of F = GMeMs/r^2 where Me mass of Earth and Ms is mass of sun

#object = pygame.Vector2(440,160)    # Object and velocity are the only two values we can set
#velocity = pygame.Vector2(0, 500)
#object_pos = deque(maxlen=100)
#object_pos.append(object)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    pygame.draw.circle(screen, "red", sun.position, 40)
    pygame.draw.circle(screen,"blue",earth.position, 20)

    if len(earth.trail) >= 2:
        pygame.draw.aalines(screen, "white", False, earth.trail)

    displacement = sun.position - earth.position 
    displacement_unit = displacement.normalize()

    distance = pygame.math.Vector2.distance_squared_to(sun.position, earth.position) 

    force = M_ES/distance       
    force_vector = force * displacement_unit
                                  
    earth.acceleration = force_vector / earth.mass               #Using Semi-Euler method
    earth.velocity = earth.velocity + (earth.acceleration * dt)
    earth.position = earth.position + (earth.velocity * dt)


    earth.trail.append(earth.position)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()