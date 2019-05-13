import pygame
import os
import GameEntity
import Rocket


class Fighter(GameEntity.GameEntity):
    def __init__(self, screen, x, y, width, height, velocity):
        super().__init__(screen, x, y, width, height, velocity)

        self.idle_sprites = self._load_sprites(
            [
                os.path.join('assets/white_fighter', 'spr_fighter_white_0.png'),
                os.path.join('assets/white_fighter', 'spr_fighter_white_1.png'),
                os.path.join('assets/white_fighter', 'spr_fighter_white_2.png'),
                os.path.join('assets/white_fighter', 'spr_fighter_white_3.png')
            ])

        self.left_sprites = self._load_sprites(
            [
                os.path.join('assets/white_fighter', 'spr_fighter_white_left_0.png')
            ])

        self.right_sprites = self._load_sprites(
            [
                os.path.join('assets/white_fighter', 'spr_fighter_white_right_0.png')
            ])

        self.sprites = self.idle_sprites

        self.bullets = []

    def draw(self):
        super().draw()

        for entity in self.bullets:
            entity.draw()

    def tick(self):
        super().tick()

        keys_pressed = pygame.key.get_pressed()
        screen_width, screen_height = pygame.display.get_surface().get_size()

        self._set_active_sprites(self.idle_sprites)

        if keys_pressed[pygame.K_LEFT]:
            if self.x > 0:
                self._set_active_sprites(self.left_sprites)
                self.x -= self.velocity

        if keys_pressed[pygame.K_RIGHT]:
            if self.x + self.width < screen_width:
                self._set_active_sprites(self.right_sprites)
                self.x += self.velocity

        if keys_pressed[pygame.K_UP]:
            if self.y > screen_height - 300:
                self.y -= self.velocity

        if keys_pressed[pygame.K_DOWN]:
            if self.y < screen_height - self.height:
                self.y += self.velocity

        if keys_pressed[pygame.K_SPACE]:
            self.bullets.append(
                Rocket.Rocket(self.screen, self.x + self.width / 2 - 10, self.y - self.height / 2, 19, 49, 20))

        delete_list = []

        for index, entity in enumerate(self.bullets):
            if entity.destroy:
                delete_list.insert(0, index)
            entity.tick()

        for index_to_remove in delete_list:
            del self.bullets[index_to_remove]
