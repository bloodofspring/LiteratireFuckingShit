import pygame

from screens.abstract import AbstractScreen
from util import load_image, get_screen
from constants import window_width, window_height


class CreditsScreen(AbstractScreen):
    def __init__(self, screen, runner, score):
        super().__init__(screen=screen, runner=runner)

        font = pygame.font.Font("static/fonts/pixelFont.TTF", 85)
        self.gratitude_text = font.render("Вы прошли викторину!", True, (0, 0, 0))  # Спасибо за игру


        background = load_image('eo_bg.png')
        self.background = pygame.transform.scale(background, (window_width, window_height))

        self.very_small_font = pygame.font.Font("static/fonts/pixelFont.TTF", 50)
        self.second_gratitude_text = self.very_small_font.render(f"Спасибо за игру! Ваш счет: {score}", True, (0, 0, 0))  # Спасибо за игру
        self.flicker_frequency = 1
        self.alpha_delta = 5
        self.current_alpha: int = 255

    def handle_events(self, events) -> None:
        for event in events:
            if event.type != pygame.KEYUP:
                continue

            self.runner.change_screen(get_screen(name="TitleScreen")(screen=self.screen, runner=self.runner))

    def update_flickering_text(self) -> None:
        if self.runner.frame % self.flicker_frequency:
            return

        rendered_text = self.very_small_font.render("Press any key", True, (0, 0, 0))

        if self.current_alpha == 255:
            self.alpha_delta = abs(self.alpha_delta) * -1

        if self.current_alpha == 0:
            self.alpha_delta = abs(self.alpha_delta)

        self.current_alpha = (self.current_alpha + self.alpha_delta) % 256
        rendered_text.set_alpha(self.current_alpha)
        self.screen.blit(rendered_text, (300, 480))

    def update(self, events, **kwargs) -> None:
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))

        self.screen.blit(self.gratitude_text, (25, 100))
        self.screen.blit(self.second_gratitude_text, (80, 200))
        self.update_flickering_text()

        self.handle_events(events=events)
