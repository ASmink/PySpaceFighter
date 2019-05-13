import pygame
import os
import Fighter


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Space Fighter")

        self.screen = pygame.display.set_mode((1200, 900))
        self.clock = pygame.time.Clock()
        self.running = True
        self.bg = pygame.transform.scale(pygame.image.load(os.path.join('assets', 'bg_space.png')), (1200, 900))

        self.entities = self._load_initial_entities()

    def start_game(self):
        while self.running:
            self.clock.tick(60)
            self._tick()
            self._draw()

        pygame.quit()

    def _draw(self):
        self.screen.fill((0, 0, 0))

        self.screen.blit(self.bg, (0, 0))

        for entity in self.entities:
            entity.draw()

        pygame.display.update()

    def _tick(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            self.running = False

        delete_list = []

        for index, entity in enumerate(self.entities):
            if entity.destroy:
                delete_list.insert(0, index)
            entity.tick()

        for index_to_remove in delete_list:
            del self.entities[index_to_remove]

    def _load_initial_entities(self):
        screen_width, screen_height = pygame.display.get_surface().get_size()

        # Fighter
        fighter_width = 94
        fighter_height = 100
        fighter_x = round(screen_width / 2 - fighter_width / 2)
        fighter_y = screen_height - fighter_height

        return [Fighter.Fighter(self.screen, fighter_x, fighter_y, fighter_width, fighter_height, 30)]


if __name__ == "__main__":
    print("Starting Game")
    game = Game()
    game.start_game()
    print("Closing Game")
