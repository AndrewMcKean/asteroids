# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    
    player = Player(x=SCREEN_WIDTH/2, y=SCREEN_HEIGHT/2)

    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    
        for updatable in updatables:
            updatable.update(dt)

        screen.fill("black")


        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()

        # Limit fps to 60
        dt = clock.tick(60) / 1000






if __name__ == "__main__":
    main()
