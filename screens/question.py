import random

import pygame

import constants
import util
from constants import window_width, window_height
from screens.credits import CreditsScreen
from screens.gameOver import GameOverScreen
from screens.abstract import AbstractScreen
from util import load_image, draw_button_with_background


class QuestionScreen(AbstractScreen):
    def __init__(self, screen, runner, difficulty: int):
        super().__init__(screen=screen, runner=runner)

        self.score_font = pygame.font.Font("static/fonts/pixelFont.TTF", 35)

        self.difficulty = difficulty
        self.score = 0
        self.cur_ypos = 0
        self.time_left = constants.difficulty_to_time[difficulty]
        self.questions = constants.QUESTIONS
        random.shuffle(self.questions)
        self.current_question_id = 0

        background = load_image('eo_bg.png')
        self.background = pygame.transform.scale(background, (window_width, window_height))

    def handle_events(self, events) -> None:
        for event in events:
            match event.type:
                case pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.change_cursor_position(d=-1)

                    if event.key == pygame.K_DOWN:
                        self.change_cursor_position(d=1)

                    if event.key == pygame.K_RETURN:
                        self.change_screen_according_to_answer()

    def change_screen_according_to_answer(self, force_fail: bool = False):
        if self.current_question_id + 1 >= len(self.questions):
            self.runner.change_screen(CreditsScreen(screen=self.screen, runner=self.runner, score=self.score))
            return

        if force_fail or self.cur_ypos + 1 != self.questions[self.current_question_id].correct_answer_id:
            self.runner.change_screen(GameOverScreen(screen=self.screen, runner=self.runner))
            return

        self.current_question_id += 1
        self.score += 1
        self.time_left = constants.difficulty_to_time[self.difficulty]

    def display_question_text(self):
        util.print_text(self.screen, self.questions[self.current_question_id].text, 25, 80, 20)

    def display_buttons(self):
        font = pygame.font.Font("static/fonts/pixelFont.TTF", 25)

        for i, a in enumerate(self.questions[self.current_question_id].answers, start=1):
            draw_button_with_background(
                width=950, height=75, border_width=5,
                border_color=(255, 255, 0) if self.cur_ypos == i - 1 else (0, 0, 0),
                background_color=(128, 128, 0) if self.cur_ypos == i - 1 else (128, 128, 128),
                blit=True, x=25, y=200 + 100 * i, screen=self.screen
            )
            self.screen.blit(font.render(self.questions[self.current_question_id].answers[a], True, (0, 0, 0)),
                             (50, 220 + 100 * i))

    def change_cursor_position(self, d: int):
        self.cur_ypos = (self.cur_ypos + d) % len(self.questions[self.current_question_id].answers)

    def update_time(self):
        if self.runner.frame == 0:
            self.time_left -= 1

        if self.time_left <= 0:
            self.change_screen_according_to_answer(force_fail=True)

    def update(self, events, **kwargs) -> None:
        self.handle_events(events)

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.background, (0, 0))

        self.update_time()
        self.screen.blit(
            self.score_font.render(f"Ваш счет: {self.score} | Осталось времени: {self.time_left} сек", True, (0, 0, 0)),
            (25, 20))
        surface = pygame.Surface((constants.window_width, constants.window_height))
        surface.set_alpha(64)
        surface.fill((32, 32, 32))
        self.screen.blit(surface, (0, 0))

        self.display_question_text()
        self.display_buttons()
