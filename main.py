import math
from verlet import VerletObject
from constrains.stick import Stick
from constrains.spring import Spring
from solver import Solver

import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 800
clock = pygame.time.Clock()

pygame.display.set_caption("Verlet physics")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

points: list[VerletObject] = [
    VerletObject(200, 200, 1, 10, False),
    VerletObject(300, 200, 1, 10, True),
    VerletObject(300, 300, 1, 10, False),
    VerletObject(200, 300, 1, 10, False)
]

"""sticks: list[Stick] = [
    Stick(points[0], points[1], 100),
    Stick(points[1], points[2], 100),
    Stick(points[2], points[3], 100)
]"""

sticks: list[Stick] = [
    Spring(points[0], points[1], 10, 100, 0.5),
    Spring(points[1], points[2], 10, 100, 0.5),
    Spring(points[2], points[3], 10, 100, 0.5),
    Spring(points[3], points[0], 10, 100, 0.5),
    Spring(points[2], points[0], 10, 141, 0.5),
    Spring(points[3], points[1], 10, 141, 0.5),
]

while True:
    dt = clock.tick() / 100
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                for point in points:
                    mouse_pos = pygame.mouse.get_pos()
                    if point.contact(mouse_pos):
                        point.is_sticked(not point.is_sticked())

    # update

    for point in points:
        point.update(dt)

    for stick in sticks:
        stick.update()

    # apply forces

    for point in points:
        point.constrain()

    # render

    for point in points:
        point.draw(screen)

    for stick in sticks:
        stick.draw(screen)

    pygame.display.update()
