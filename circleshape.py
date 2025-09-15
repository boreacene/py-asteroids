import pygame


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def is_colliding_with(self, circle_shape_obj):
        distance = pygame.math.Vector2.distance_to(
            self.position, circle_shape_obj.position
        )
        return distance <= self.radius + circle_shape_obj.radius
