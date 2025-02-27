from .abstract import AbstractScreen
from .title import TitleScreen
from .chooseDifficulty import ChooseDifficultyScreen

text_to_screen = {
    "AbstractScreen": AbstractScreen,
    "TitleScreen": TitleScreen,
    "chooseDifficulty": chooseDifficulty,
}
