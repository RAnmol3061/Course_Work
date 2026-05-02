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
    def __init__(self, name, mass, velocity) -> None:
        self.name = name
        self.mass = mass
        self.velocity = velocity

sun = celestial_bodies('sun', 10000, pygame.Vector2())
earth 
        

sun = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

#Normalized Constant
G, M1, M2 = 10000, 10000, 1

object = pygame.Vector2(440,160)    # Object and velocity are the only two values we can set
velocity = pygame.Vector2(0, 500)
object_pos = deque(maxlen=100)
object_pos.append(object)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    pygame.draw.circle(screen, "red", sun, 40)
    pygame.draw.circle(screen,"blue",object, 20)

    for pos in object_pos:
        pygame.draw.circle(screen, "white", pos, 2)

    dx = sun.x - object.x 
    dy = sun.y - object.y
     
    distance = pygame.math.Vector2.distance_to(sun, object) #r

    force = (G*M1*M2)/(distance * distance)       
    fx, fy = (force * (dx/distance)), (force * (dy/distance))               
    force_vector = pygame.Vector2(fx, fy)
                                  
    acceleration = force_vector / M2                      #Using Semi-Euler method
    velocity = velocity + (acceleration * dt)
    object = object + (velocity * dt)


    object_pos.append(object)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()