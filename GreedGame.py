from Exceptions.NumberOfPlayersException import NumberOfPlayersError
from Player import Player


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

