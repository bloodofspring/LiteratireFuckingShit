import pygame

from screens.abstract import AbstractScreen
from util import load_image
from constants import window_width, window_height


class TitleScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)

        self.welcome_text_font = pygame.font.Font("static/fonts/pixelFont.TTF", 50)

        background = load_image('eo_bg.png')
        self.background = pygame.transform.scale(background, (window_width, window_height))

        self.welcome_text_alpha: int = 255
        self.flicker_frequency = 1
        self.alpha_change_delta: int = 5

        self.jumping: bool = False
        self.jump_counter = 0

        self.title_text_1 = pygame.font.Font("static/fonts/pixelFont.TTF", 190).render("ВИКТОРИНА", True, (0, 0, 0))
        self.title_text_2 = pygame.font.Font("static/fonts/pixelFont.TTF", 49).render('по роману в стихах "Евгений Онегин"', True, (0, 0, 0))

    def handle_events(self, events) -> None:
        for event in events:
            match event.type:
                case pygame.KEYUP:
                    if event.key == pygame.K_RETURN:
                        pass
                        # self.runner.change_screen(TeamChoosingScreen(screen=self.screen, runner=self.runner))

    def update_welcome_text(self) -> None:
        if self.runner.frame % self.flicker_frequency:
            rendered_text = self.welcome_text_font.render("Press  Enter  to  start", True, self.welcome_text_alpha)
            self.screen.blit(rendered_text, (260, 370))

            return

        if self.welcome_text_alpha == 255:
            self.alpha_change_delta = abs(self.alpha_change_delta) * -1

        if self.welcome_text_alpha == 0:
            self.alpha_change_delta = abs(self.alpha_change_delta)

        rendered_text = self.welcome_text_font.render("Press  Enter  to  start", True, (0, 0, 0))
        self.welcome_text_alpha = (self.welcome_text_alpha + self.alpha_change_delta) % 256
        rendered_text.set_alpha(self.welcome_text_alpha)
        self.screen.blit(rendered_text, (190, 450))

    def update(self, events, **kwargs) -> None:
        self.handle_events(events)

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.title_text_1, (25, 30))
        self.screen.blit(self.title_text_2, (25, 220))

        self.update_welcome_text()
