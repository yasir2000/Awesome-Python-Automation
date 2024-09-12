import pygame
import os
import math
from abc import ABC, abstractmethod

# Load environment variables
WIDTH = int(os.getenv("WIDTH", 1000))
HEIGHT = int(os.getenv("HEIGHT", 800))
AU = float(os.getenv("AU", 149600000000))
G = float(os.getenv("G", 6.67428e-11))
SCALE = float(os.getenv("SCALE", 0.00000167677))
TIMESTEP = int(os.getenv("TIMESTEP", 86400))

pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")
FONT = pygame.font.SysFont("comicsans", 16)

# Abstract Factory for creating planets
class PlanetFactory(ABC):
    @abstractmethod
    def create_planet(self, x, y, radius, color, mass, y_vel=0):
        pass

class SimplePlanetFactory(PlanetFactory):
    def create_planet(self, x, y, radius, color, mass, y_vel=0):
        return Planet(x, y, radius, color, mass, y_vel)

class Planet:
    def __init__(self, x, y, radius, color, mass, y_vel=0):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass
        self.y_vel = y_vel
        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

    def draw(self, win):
        x = self.x * SCALE + (WIDTH / 2)
        y = self.y * SCALE + (HEIGHT / 2)

        if len(self.orbit) > 2:
            updated_points = [(px * SCALE + WIDTH / 2, py * SCALE + HEIGHT / 2) for px, py in self.orbit]
            pygame.draw.lines(win, self.color, False, updated_points, 2)

        pygame.draw.circle(win, self.color, (x, y), self.radius)

        if not self.sun:
            distance_text = FONT.render(f"{round(self.distance_to_sun/1000, 1)} km", 1, (255, 255, 255))
            win.blit(distance_text, (x - distance_text.get_width() / 2, y - distance_text.get_height() / 2))

    def attraction(self, other):
        other_x, other_y = other.x, other.y
        distance_x = other_x - self.x
        distance_y = other_y - self.y
        distance = math.sqrt(distance_x ** 2 + distance_y ** 2)

        if other.sun:
            self.distance_to_sun = distance

        force = G * self.mass * other.mass / distance ** 2
        theta = math.atan2(distance_y, distance_x)
        force_x = math.cos(theta) * force
        force_y = math.sin(theta) * force
        return force_x, force_y

    def update_position(self, planets):
        total_fx, total_fy = 0, 0
        for planet in planets:
            if self == planet:
                continue
            fx, fy = self.attraction(planet)
            total_fx += fx
            total_fy += fy

        self.y_vel += total_fy / self.mass * TIMESTEP
        self.x += self.y_vel * TIMESTEP
        self.orbit.append((self.x, self.y))


def main():
    run = True
    clock = pygame.time.Clock()
    factory = SimplePlanetFactory()

    sun = factory.create_planet(0, 0, 30, (255, 255, 0), 1.98892 * 10**30)
    sun.sun = True
    planets = [
        sun,
        factory.create_planet(-AU, 0, 16, (100, 149, 237), 5.9742 * 10**24, 29.738 * 1000),
        factory.create_planet(-1.524 * AU, 0, 12, (188, 39, 50), 6.39 * 10**23, 24.077 * 1000),
        factory.create_planet(0.387 * AU, 0, 8, (80, 78, 81), 3.30 * 10**23, -47.4 * 1000),
        factory.create_planet(0.732 * AU, 0, 14, (255, 255, 255), 4.8685 * 10**24, -35.02 * 1000),
    ]

    while run:
        clock.tick(60)
        WIN.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            planet.update_position(planets)
            planet.draw(WIN)

        pygame.display.update()
    pygame.quit()

if __name__ == "__main__":
    main()
