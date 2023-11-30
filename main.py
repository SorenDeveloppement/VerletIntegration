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
    VerletObject(401, 100, 1, 10, False),
    VerletObject(400, 200, 1, 10, False),
    VerletObject(400, 300, 1, 10, False),
    VerletObject(400, 400, 1, 10, True)
]

"""sticks: list[Stick] = [
    Stick(points[0], points[1], 100),
    Stick(points[1], points[2], 100),
    Stick(points[2], points[3], 100)
]"""

sticks: list[Stick] = [
    Spring(points[0], points[1], 10, 30, 0.7),
    Spring(points[1], points[2], 10, 30, 0.7),
    Spring(points[2], points[3], 10, 30, 0.7)
]

while True:
    dt = clock.tick() / 100
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if pygame.mouse.get_pressed()[0]:
                for point in points:
                    mouse_pos = pygame.mouse.get_pos()
                    if point.contact(mouse_pos):
                        point.set_pos(mouse_pos[0], mouse_pos[1])

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
