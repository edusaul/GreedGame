from Dice import DiceSet
from Score import score

class NumberOfPlayersError(Exception):
    pass


class Player:
    NUMBER_OF_DICE_FACES = 7

    def __init__(self):
        self._total_score = 0
        self._points = 0
        self._dice = DiceSet()
        self._last_roll = None

    @property
    def total_score(self):
        return self._total_score

    def score(self, roll):
        points = score(roll)

        if points == 0:
            self._points = 0
            self.end_turn()
        else:
            self._points += points

        return self._points

    def end_turn(self):
        if self._total_score + self._points >= 300:
            self._total_score += self._points

        self._points = 0
        self._last_roll = None
        return self

    def roll(self):
        number_of_dices = 5
        if self._last_roll != None:
            aux = []
            for i in range(self.NUMBER_OF_DICE_FACES): aux.append((i, self._last_roll.count(i)))
            for i, ni in aux:
                while ni > 0:
                    if ni > 2:
                        ni -= 3
                        number_of_dices -= 3
                    else:
                        if i == 1 or i == 5:
                            number_of_dices -= ni
                        ni = 0
        self._dice.roll(number_of_dices)
        self._last_roll = self._dice.values
        return self._last_roll


class GreedGame:
    def __init__(self):
        self._player = [Player()] * 2

    @property
    def number_of_players(self):
        return len(self._player)

    @number_of_players.setter
    def number_of_players(self, n_of_players):
        if n_of_players < 2:
            raise NumberOfPlayersError('There must be at least two players')
        else:
            self._player = [Player()] * n_of_players

    def total_score(self, player):
        return self._player[player].total_score

    def score(self, player, roll):
        return self._player[player].score(roll)

    def end_turn(self, player):
        return self._player[player].end_turn()

    def roll(self, player):
        return self._player[player].roll()

