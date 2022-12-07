import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# This class mainly choose 5 random numbers for winning numbers ranged from 1 up to 20 and
# choose one random number for winner power ball ranged from 1 to 10
class WhiteBall:
    def __init__(self, value = None ):
        self.value = value
    @property
    def WhiteBallGetter(self):
        return self.value

    def winner(self):
        winnerRandom = random.sample(range(1, 20), k = 5)
        self.value = winnerRandom
        return winnerRandom

    def Lucky(self):
        luckyRandom = random.sample(range(1, 20),  k = 5)
        self.value = luckyRandom

        return luckyRandom

# This class mainly choose 5 random numbers for lucky numbers ranged from 1 up to 20 and
# choose one random number for lucky power ball ranged from 1 to 10
class PowerBall:
    def __init__(self, value = None ):
        self.value = value
    @property
    def PowerBallGetter(self):
        return self.value

    def winner(self):
        winnerRandom = random.randint(1, 10)
        self.value = winnerRandom
        return winnerRandom

    def Lucky(self):
        luckyRandom = random.randint(1, 10)
        self.value = luckyRandom
        return luckyRandom