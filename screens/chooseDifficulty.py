import pygame

from screens.question import QuestionScreen
from screens.abstract import AbstractScreen
from util import load_image, draw_button_with_background
from constants import window_width, window_height


class ChooseDifficultyScreen(AbstractScreen):
    def __init__(self, screen, runner):
        super().__init__(screen=screen, runner=runner)

        background = load_image('eo_bg.png')
        self.background = pygame.transform.scale(background, (window_width, window_height))

        self.cur_xpos = 0
        self.cur_ypos = 0

        self.title_text_1 = pygame.font.Font("static/fonts/pixelFont.TTF", 90).render("Выберите сложность:", True, (0, 0, 0))

    def handle_events(self, events) -> None:
        for event in events:
            match event.type:
                case pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.change_cursor_position(d_y=1)

                    if event.key == pygame.K_RIGHT:
                        self.change_cursor_position(d_x=1)

                    if event.key == pygame.K_DOWN:
                        self.change_cursor_position(d_y=-1)

                    if event.key == pygame.K_LEFT:
                        self.change_cursor_position(d_x=-1)

                    if event.key == pygame.K_RETURN:
                        self.runner.change_screen(QuestionScreen(screen=self.screen, runner=self.runner, difficulty=self.difficulty))

    @property
    def difficulty(self):
        if self.cur_xpos == 0 and self.cur_ypos == 0:
            return 0

        if self.cur_xpos == 1 and self.cur_ypos == 0:
            return 1

        if self.cur_xpos == 0 and self.cur_ypos == 1:
            return 2

        return 3

    def change_cursor_position(self, *, d_x: int = 0, d_y: int = 0):
        self.cur_xpos = (self.cur_xpos + d_x) % 2
        self.cur_ypos = (self.cur_ypos + d_y) % 2

    def display_buttons(self):
        font = pygame.font.Font("static/fonts/pixelFont.TTF", 50)

        draw_button_with_background(
            width=400, height=200, border_width=5,
            border_color=(255, 255, 0) if self.cur_xpos == 0 and self.cur_ypos == 0 else (0, 0, 0),
            background_color=(128, 128, 0) if self.cur_xpos == 0 and self.cur_ypos == 0 else (128, 128, 128),
            blit=True, x=75, y=220, screen=self.screen
        )
        self.screen.blit(font.render("Очень легко", True, (0, 0, 0)), (120, 290))

        draw_button_with_background(
            width=400, height=200, border_width=5,
            border_color=(255, 255, 0) if self.cur_xpos == 1 and self.cur_ypos == 0 else (0, 0, 0),
            background_color=(128, 128, 0) if self.cur_xpos == 1 and self.cur_ypos == 0 else (128, 128, 128),
            blit=True, x=500, y=220, screen=self.screen
        )
        self.screen.blit(font.render("Легко", True, (0, 0, 0)), (620, 290))

        draw_button_with_background(
            width=400, height=200, border_width=5,
            border_color=(255, 255, 0) if self.cur_xpos == 0 and self.cur_ypos == 1 else (0, 0, 0),
            background_color=(128, 128, 0) if self.cur_xpos == 0 and self.cur_ypos == 1 else (128, 128, 128),
            blit=True, x=75, y=450, screen=self.screen
        )
        self.screen.blit(font.render("Нормально", True, (0, 0, 0)), (135, 525))

        draw_button_with_background(
            width=400, height=200, border_width=5,
            border_color=(255, 255, 0) if self.cur_xpos == 1 and self.cur_ypos == 1 else (0, 0, 0),
            background_color=(128, 128, 0) if self.cur_xpos == 1 and self.cur_ypos == 1 else (128, 128, 128),
            blit=True, x=500, y=450, screen=self.screen
        )
        self.screen.blit(font.render("Сложно", True, (0, 0, 0)), (610, 525))

    def update(self, events, **kwargs) -> None:
        self.handle_events(events)

        self.screen.fill((255, 255, 255))

        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.title_text_1, (25, 50))

        self.display_buttons()
