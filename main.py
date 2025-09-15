import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
    pygame.init()
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fpsclock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # container attr is resolved at compile time
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    asteroid_field = AsteroidField()

    Player.containers = (updatables, drawables)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatables.update(dt)
        for asteroid in asteroids:
            if asteroid.is_colliding_with(player):
                print("Game Over!")
                sys.exit(0)

        screen.fill("black")

        for obj in drawables:
            obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = fpsclock.tick(60) / 1000


if __name__ == "__main__":
    main()
