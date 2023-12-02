import pygame
import math


class VerletObject:
    def __init__(self, x: int, y: int, mass: float, radius: int, sticked: bool) -> None:
        self.x: float = x
        self.y: float = y
        self.old_x: float = x
        self.old_y: float = y
        self.mass: float = mass
        self.radius: int = radius
        self.sticked: bool = sticked

        self.force_x = 0
        self.force_y = 9.81

    def update(self, dt: float) -> None:
        if not self.sticked:
            vel_x = self.x - self.old_x
            vel_y = self.y - self.old_y

            self.old_x = self.x
            self.old_y = self.y

            acc_x = self.force_x / self.mass
            acc_y = self.force_y / self.mass

            self.x += vel_x + acc_x * (dt*dt)
            self.y += vel_y + acc_y * (dt*dt)

    def constrain(self):
        vel_x = self.x - self.old_x
        vel_y = self.y - self.old_y

        if self.x < 0:
            self.x = 0
            self.old_x = self.x + vel_x
        elif self.x > 1000:
            self.x = 1000
            self.old_x = self.x + vel_x
        elif self.y < 0:
            self.y = 0
            self.old_y = self.y + vel_y
        elif self.y > 800:
            self.y = 800
            self.old_y = self.y + vel_y

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, (255, 255, 255),
                           (self.x, self.y), self.radius)

    def distance(self, other: __build_class__) -> float:
        return math.sqrt((self.x - other.get_x())**2 + (self.y - other.get_y())**2)

    def contact(self, pos: tuple[float, float] | list[int, int]) -> bool:
        return ((self.x - pos[0])**2 + (self.y - pos[1])**2) <= self.radius

    def get_pos(self) -> tuple[float, float]:
        return self.x, self.y

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def set_pos(self, x: float, y: float) -> None:
        self.x, self.y = x, y

    def set_x(self, x: float) -> None:
        self.x = x

    def set_y(self, y: float) -> None:
        self.y = y

    def is_sticked(self, sticked: bool = None) -> bool | None:
        if sticked == None:
            return self.sticked
        else:
            self.sticked = sticked
