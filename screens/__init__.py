from .abstract import AbstractScreen
from .title import TitleScreen
from .chooseDifficulty import ChooseDifficultyScreen
from .question import QuestionScreen

text_to_screen = {
    "AbstractScreen": AbstractScreen,
    "TitleScreen": TitleScreen,
    "chooseDifficulty": chooseDifficulty,
    "QuestionScreen": QuestionScreen
}
