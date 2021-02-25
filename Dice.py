import random

class DiceSet:
    def __init__(self):
        self._values = None

    @property
    def values(self):
        return self._values

    def roll(self, n):
        # Needs implementing!
        # Tip: random.randint(min, max) can be used to generate random numbers
        rolls = []
        for i in range(n):
            rolls.append(random.randint(1,6))
        self._values = rolls