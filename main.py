import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, PLAYER_RADIUS, LINE_WIDTH
from logger import log_state
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    py_clock = pygame.time.Clock()
    dt = 0

    ## Creating game groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    ## Main game loop
    while True:
        log_state()
        screen.fill("black")
        for object in drawable:
            object.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.display.flip()
        dt = py_clock.tick(60) / 1000
        updatable.update(dt)


if __name__ == "__main__":
    main()
