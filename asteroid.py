from circleshape import CircleShape
from constants import LINE_WIDTH
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen, color, pos, radius, line_width=LINE_WIDTH):
        pygame.draw.circle(screen, color, pos, radius, line_width)
    
    def update(self, dt):
        self.position += self.velocity * dt 
