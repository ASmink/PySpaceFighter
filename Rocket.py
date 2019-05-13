import os
import GameEntity


class Rocket(GameEntity.GameEntity):
    def __init__(self, screen, x, y, width, height, velocity):
        super().__init__(screen, x, y, width, height, velocity)

        self.idle_sprites = self._load_sprites(
            [
                os.path.join('assets/white_fighter', 'spr_missile_white_0.png')
            ])

        self.sprites = self.idle_sprites

    def draw(self):
        super().draw()

    def tick(self):
        super().tick()

        self.y -= self.velocity

        if self.y < 0:
            self.destroy = True
