from Exceptions.NumberOfPlayersException import NumberOfPlayersError
from Player import Player


class GreedGame:
    def __init__(self):
        self._player = None
        self._whos_turn = None

    @property
    def number_of_players(self):
        return len(self._player)

    @number_of_players.setter
    def number_of_players(self, n_of_players):
        if n_of_players < 2:
            raise NumberOfPlayersError('There must be at least two players')
        else:
            self._player = [Player()] * n_of_players

    @property
    def whos_turn(self):
        return 'It is turn for player ' + str(self._whos_turn+1)

    def start_game(self, n_of_players=2):
        self.number_of_players = n_of_players
        self._whos_turn = 0
        return self

    def end_game(self):
        self._player = None

    def total_score(self, player):
        return self._player[player].total_score

    def score(self, player, roll):
        return self._player[player].score(roll)

    def end_turn(self, player):
        self._player[player].end_turn()
        if self._whos_turn + 2 <= self.number_of_players:
            self._whos_turn += 1
        else:
            self._whos_turn = 0
        return self.whos_turn

    def roll(self, player):
        return self._player[player].roll()
