from .abstract import AbstractScreen
from .title import TitleScreen
from .chooseDifficulty import ChooseDifficultyScreen
from .question import QuestionScreen
from .gameOver import GameOverScreen
from .credits import CreditsScreen

text_to_screen = {
    "AbstractScreen": AbstractScreen,
    "TitleScreen": TitleScreen,
    "chooseDifficulty": chooseDifficulty,
    "QuestionScreen": QuestionScreen,
    "GameOverScreen": GameOverScreen,
    "CreditsScreen": CreditsScreen,
}
