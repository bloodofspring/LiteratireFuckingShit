import pygame
import os

import screens


def print_text(screen, message, x, y, end=0, font_color=(255, 255, 255)):
    pygame.font.init()
    font_type = pygame.font.Font("static/fonts/pixelFont.TTF", 60)
    text = font_type.render(message, True, font_color)
    if end > 1:
        words = []
        for i in message.split():
            words.append(i)
            if len(" ".join(words)) > end:
                end *= 2
                words.append('-')

        message = " ".join(words)
        list_words = message.split('-')
        list_length = len(list_words)
        for i in range(0, list_length):
            list_text = font_type.render(list_words[i].strip(), True, font_color)
            screen.blit(list_text, (x, y + 65 * i))
    else:
        screen.blit(text, (x, y))


def draw_button_with_background(
        width: int, height: int,
        border_width: int | None, border_color: tuple[int, int, int] | str | None,
        background_color: tuple[int, int, int] | str, alpha: int = 128,
        blit: bool = False, x: int | None = None, y: int | None = None, screen: pygame.Surface | None = None
) -> pygame.Surface:
    surface = pygame.Surface((width, height))
    surface.set_alpha(alpha)
    surface.fill(background_color)

    if border_width is not None and border_width > 0:
        pygame.draw.rect(surface, border_color, (0, 0, width, height), border_width)

    if blit:
        screen.blit(surface, (x, y))

    return surface


def load_image(name, colorkey=None, path="static/images"):
    fullname = os.path.join(path, name)

    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        exit("Resource file not found")

    image = pygame.image.load(fullname)

    if colorkey is None:
        return image.convert_alpha()

    image = image.convert()

    if colorkey == -1:
        colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)

    return image


def get_screen(name: str):
    try:
        return screens.text_to_screen[name]
    except IndexError:
        raise ValueError
