import pygame
import math
from verlet import VerletObject


class Spring:
    def __init__(self, point_1: VerletObject, point_2: VerletObject, stiffness: float, rest_length: float, damping_factor: float) -> None:
        self.p1: VerletObject = point_1
        self.p2: VerletObject = point_2
        self.stiff: float = stiffness
        self.restlength: float = rest_length
        self.damp: float = damping_factor

    def update(self) -> None:
        delta_x = self.p2.get_x() - self.p1.get_x()
        delta_y = self.p2.get_y() - self.p1.get_y()
        dist = math.sqrt(delta_x * delta_x + delta_y * delta_y)
        diff = (dist - self.restlength) / dist

        if not self.p1.is_sticked():
            self.p1.set_pos(self.p1.get_x() + self.damp * diff *
                            delta_x, self.p1.get_y() + self.damp * diff * delta_y)

        if not self.p2.is_sticked():
            self.p2.set_pos(self.p2.get_x() - self.damp * diff *
                            delta_x, self.p2.get_y() - self.damp * diff * delta_y)

        """x = dist - self.restlength
        fs = x * self.stiff

        fdx = ((self.p2.get_x() - self.p1.get_x()) / dist) * \
            (self.p2.get_x() - self.p1.get_x()) * self.damp
        fdy = ((self.p2.get_y() - self.p1.get_y()) / dist) * \
            (self.p2.get_y() - self.p1.get_y()) * self.damp

        ftx = fs + fdx
        fty = fs + fdy

        dist_ab = math.sqrt((self.p1.get_x() - self.p2.get_x())**2 +
                            (self.p1.get_y() - self.p2.get_y())**2)

        fax = ((self.p2.get_x() - self.p1.get_x()) / dist) * ftx
        fay = ((self.p2.get_y() - self.p1.get_y()) / dist) * fty

        fbx = ((self.p1.get_x() - self.p2.get_x()) / dist_ab) * ftx
        fby = ((self.p1.get_y() - self.p2.get_y()) / dist_ab) * fty"""

    def draw(self, screen) -> None:
        pygame.draw.line(screen, (255, 255, 255),
                         self.p1.get_pos(), self.p2.get_pos())
