import pygame
from random import randrange

from settings import *

x, y = randrange(0, WIDTH, CELL_SIZE), randrange(0, HEIGHT, CELL_SIZE)
apple = randrange(0, WIDTH, CELL_SIZE), randrange(0, HEIGHT, CELL_SIZE)
snake_length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 5

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

while True:
    # Background
    sc.fill(BLACK)

    # Draw snake
    for xx, yy in snake:
        pygame.draw.rect(sc, GREEN, (xx, yy, CELL_SIZE, CELL_SIZE))

    # Draw apple
    pygame.draw.rect(sc, RED, (*apple, CELL_SIZE, CELL_SIZE))

    # Move snake
    x += dx * CELL_SIZE
    y += dy * CELL_SIZE

    # Add new head cell
    snake.append((x,y))
    # Remove tail cell
    snake = snake[-snake_length:]

    # Check apple
    if snake[-1] == apple:
        apple = randrange(0, WIDTH, CELL_SIZE), randrange(0, HEIGHT, CELL_SIZE)
        snake_length += 1

    # Check game overaw
    if x < 0 or x > WIDTH - CELL_SIZE or y < 0 or y > HEIGHT - CELL_SIZE:
        break
    # Check self intersection (head cell already in the list)
    if (x,y) in snake[:-1]:
        break

    pygame.display.flip()
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_w]:
        dx, dy = 0, -1
    if key[pygame.K_s]:
        dx, dy = 0, 1
    if key[pygame.K_a]:
        dx, dy = -1, 0
    if key[pygame.K_d]:
        dx, dy = 1, 0
