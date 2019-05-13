import pygame


class GameEntity:
    def __init__(self, screen, x, y, width, height, velocity):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
        self.sprites = []
        self.animation_index = 0
        self.animation_speed = 5
        self.destroy = False

    def draw(self):
        if self.animation_index + 1 >= len(self.sprites) * self.animation_speed:
            self.animation_index = 0

        self.screen.blit(self.sprites[self.animation_index // self.animation_speed], (self.x, self.y))

        self.animation_index += 1

    def tick(self):
        pass

    def _load_sprites(self, sprites):
        modified_sprites = []

        for sprite in sprites:
            modified_sprites.append(pygame.transform.scale(pygame.image.load(sprite), (self.width, self.height)))

        return modified_sprites

    def _set_active_sprites(self, sprites):
        if self.sprites is not sprites:
            self.sprites = sprites
            self.animation_index = 0
