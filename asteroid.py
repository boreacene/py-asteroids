import pygame
import random
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        # forward = pygame.Vector2(0, 1)
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        split_dir_1 = self.velocity.rotate(random_angle)
        split_dir_2 = self.velocity.rotate(-random_angle)

        split_asteroid_1 = Asteroid(
            self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS
        )
        split_asteroid_2 = Asteroid(
            self.position.x, self.position.y, self.radius - ASTEROID_MIN_RADIUS
        )
        split_asteroid_1.velocity = split_dir_1 * 1.2
        split_asteroid_2.velocity = split_dir_2 * 1.2
