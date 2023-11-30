import math
import pygame
from verlet import VerletObject


class Stick:
    def __init__(self, p1: VerletObject, p2: VerletObject, length: int) -> None:
        self.__point_1: VerletObject = p1
        self.__point_2: VerletObject = p2
        self.__length: int = length

    def update(self) -> None:
        dx = self.__point_2.get_x() - self.__point_1.get_x()
        dy = self.__point_2.get_y() - self.__point_1.get_y()
        dist = math.sqrt(dx * dx + dy * dy)
        diff = self.__length - dist
        percent = (diff / dist) / 2

        offset_x = dx * percent
        offset_y = dy * percent

        if not self.__point_1.is_sticked():
            self.__point_1.set_pos(self.__point_1.get_x() -
                                   offset_x, self.__point_1.get_y() - offset_y)

        if not self.__point_2.is_sticked():
            self.__point_2.set_pos(self.__point_2.get_x() +
                                   offset_x, self.__point_2.get_y() + offset_y)

    def draw(self, screen) -> None:
        pygame.draw.line(screen, (255, 255, 255),
                         self.__point_1.get_pos(), self.__point_2.get_pos())
