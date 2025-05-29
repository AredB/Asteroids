import pygame
import random

class Explosion(pygame.sprite.Sprite):
    containers = ()

    def __init__(self, position):
        super().__init__(self.containers)
        self.particles = []
        self.position = pygame.Vector2(position)
        self.lifetime = 0.5  # seconds

        # Create particles: small circles flying outwards
        for _ in range(20):
            velocity = pygame.Vector2(random.uniform(-100, 100), random.uniform(-100, 100))
            self.particles.append({
                "pos": pygame.Vector2(self.position),
                "vel": velocity,
                "radius": random.randint(4, 8),
                "color": (255, random.randint(100, 200), 0)
            })

    def update(self, dt):
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
            return

        # Update particle positions
        for p in self.particles:
            p["pos"] += p["vel"] * dt
            # Slowly reduce radius (particle fades out)
            p["radius"] = max(0, p["radius"] - 20 * dt)

    def draw(self, screen):
        for p in self.particles:
            if p["radius"] > 0:
                pygame.draw.circle(screen, p["color"], (int(p["pos"].x), int(p["pos"].y)), int(p["radius"]))