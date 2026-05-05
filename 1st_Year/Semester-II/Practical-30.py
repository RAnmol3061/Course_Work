import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
position = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
dt = 0.01

g = pygame.Vector2(0,20)
velocity = pygame.Vector2(0,0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")
    
    screen_rect = pygame.display.get_surface().get_rect()
    bottom_left = pygame.Vector2(screen_rect.bottomleft)
    bottom_right = pygame.Vector2(screen_rect.bottomright)
    offset = pygame.Vector2(0,50)


    pygame.draw.line(screen,'white',bottom_left-offset, bottom_right-offset)
    pygame.draw.circle(screen,'blue', position, 50)

    velocity = velocity + g*dt
    position = position + velocity*dt

    print(position)
    if pygame.math.Vector2.distance_to(position, pygame.Vector2(640,670)) <= 50:
        velocity = -velocity


    pygame.display.flip()
    clock.tick(60)