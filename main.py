import pygame
from math import pow,sqrt

WIDTH = 800
HEIGHT = 600
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

running = True

CIRCLE_RADIUS = 50
CIRCLE_X = WIDTH // 2
CIRCLE_Y = HEIGHT // 2 
CIRCLE_X_DIRECTION = 0
CIRCLE_Y_DIRECTION = 0

MOUSE_CIRCLE_RADIUS = CIRCLE_RADIUS // 2

RADIUS_SUM = CIRCLE_RADIUS + MOUSE_CIRCLE_RADIUS


while running:
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill("black")
    # Ici on render les boules
    pygame.draw.circle(screen, 'yellow', (mouse_x,mouse_y), MOUSE_CIRCLE_RADIUS)
    pygame.draw.circle(screen, 'red', (CIRCLE_X, CIRCLE_Y), CIRCLE_RADIUS)
    distance = sqrt(pow(CIRCLE_X - mouse_x,2) + pow(CIRCLE_Y - mouse_y, 2))
    if distance <= RADIUS_SUM:
        CIRCLE_X_DIRECTION = CIRCLE_X - mouse_x
        CIRCLE_Y_DIRECTION = CIRCLE_Y - mouse_y
        
    CIRCLE_X += CIRCLE_X_DIRECTION
    CIRCLE_Y += CIRCLE_Y_DIRECTION
    
    CIRCLE_X_DIRECTION *= 0.99
    CIRCLE_Y_DIRECTION *= 0.99
    if abs(CIRCLE_X_DIRECTION) < 0.1:
        CIRCLE_X_DIRECTION = 0
    if abs(CIRCLE_Y_DIRECTION) < 0.1:
        CIRCLE_Y_DIRECTION = 0    
        
    if CIRCLE_X_DIRECTION > 0 and CIRCLE_X > WIDTH - CIRCLE_RADIUS:
        CIRCLE_X_DIRECTION *= -1
    if CIRCLE_Y_DIRECTION > 0 and CIRCLE_Y > HEIGHT - CIRCLE_RADIUS:
        CIRCLE_Y_DIRECTION *= -1
        
    if CIRCLE_X_DIRECTION < 0 and CIRCLE_X < CIRCLE_RADIUS:
        CIRCLE_X_DIRECTION *= -1
    if CIRCLE_Y_DIRECTION < 0 and CIRCLE_Y < CIRCLE_RADIUS:
        CIRCLE_Y_DIRECTION *= -1
    pygame.display.flip()
    clock.tick(FPS)  # limits FPS to 60

pygame.quit()