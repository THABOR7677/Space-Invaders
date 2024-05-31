import pygame
import random
from pygame.sprite import Group, Sprite

class Alien(Sprite):
    def __init__(self, type, x, y):
        super().__init__()
        self.type = type
        path = f"Graphics/alien{type}.png"
        try:
            self.image = pygame.image.load(path)
        except pygame.error as e:
            print(f"Error loading image at {path}: {e}")
            self.image = pygame.Surface((50, 30))  # Placeholder in case of error
            self.image.fill((255, 0, 0))  # Fill with red color

        self.rect = self.image.get_rect(topleft=(x, y))

    def update(self, direction):
        self.rect.x += direction

class MysteryShip(Sprite):
    def __init__(self, screen_width, offset):
        super().__init__()
        self.screen_width = screen_width
        self.offset = offset
        try:
            self.image = pygame.image.load("Graphics/mystery.png")
        except pygame.error as e:
            print(f"Error loading image: {e}")
            self.image = pygame.Surface((75, 35))  # Placeholder in case of error
            self.image.fill((0, 0, 255))  # Fill with blue color

        x = random.choice([self.offset / 2, self.screen_width + self.offset - self.image.get_width()])
        if x == self.offset / 2:
            self.speed = 3
        else:
            self.speed = -3

        self.rect = self.image.get_rect(topleft=(x, 90))

    def update(self):
        self.rect.x += self.speed
        if self.rect.right > self.screen_width + self.offset / 2 or self.rect.left < self.offset / 2:
            self.kill()

# Ensure the pygame initialization is done before creating any pygame objects
if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((800, 600))  # Example screen initialization
    pygame.display.set_caption("Space Invaders")
    clock = pygame.time.Clock()

    # Example usage
    aliens = Group()
    aliens.add(Alien(1, 100, 100))
    mystery_ship = MysteryShip(800, 50)

    all_sprites = Group(aliens, mystery_ship)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        all_sprites.update()

        screen.fill((0, 0, 0))  # Clear screen with black
        all_sprites.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
