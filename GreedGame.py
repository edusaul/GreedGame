from Exceptions.NotYourTurnException import NotYourTurnException
from Exceptions.NumberOfPlayersException import NumberOfPlayersError
from Exceptions.StartWithGameRunningException import StartWithGameRunningException
from Player import Player


class GreedGame:
    def __init__(self):
        self._player = []
        self._whos_turn = None
        self._last_round = False
        self._last_round_started_by = None

    @property
    def number_of_players(self):
        return len(self._player)

    @number_of_players.setter
    def number_of_players(self, n_of_players):
        if n_of_players < 2:
            raise NumberOfPlayersError('There must be at least two players')
        else:
            for i in range(n_of_players):
                self._player.append(Player())

    @property
    def whos_turn(self):
        return 'It is turn for player ' + str(self._whos_turn + 1)

    @property
    def is_last_round(self):
        return self._last_round

    def start_game(self, n_of_players=2):
        if self._player:
            raise StartWithGameRunningException("Finish the current game to start a new one!")
        self.number_of_players = n_of_players
        self._whos_turn = 0
        return 'First turn is for player ' + str(self._whos_turn + 1)

    def end_game(self):
        message = 'Player ' + str(self.who_wins() + 1) + ' wins!!!\nFinal score:\n'
        for i in range(self.number_of_players):
            message += ' Player ' + str(i + 1) + ' = ' + str(self.total_score(i)) + ' points\n'

        self._player = []
        self._whos_turn = None
        self._last_round = False
        self._last_round_started_by = None
        return message

    def who_wins(self):
        scores = []
        for i in range(self.number_of_players):
            scores.append(self.total_score(i))
        winner = scores.index(max(scores))
        return winner

    def total_score(self, player):
        return self._player[player].total_score

    def score(self, player, roll):
        if player != self._whos_turn:
            raise NotYourTurnException("It is not your turn!")
        return self._player[player].score(roll)

    def end_turn(self, player):
        if player != self._whos_turn:
            raise NotYourTurnException("It is not your turn!")
        player_score = self._player[player].end_turn()
        if player_score >= 3000 and self._last_round == False:
            self._last_round = True
            self._last_round_started_by = player
        return self.next_turn()

    def next_turn(self):
        if self._whos_turn + 2 <= self.number_of_players:
            self._whos_turn += 1
        else:
            self._whos_turn = 0
        if self._last_round_started_by == self._whos_turn:
            return self.end_game()
        return self.whos_turn

    def roll(self, player):
        if player != self._whos_turn:
            raise NotYourTurnException("It is not your turn!")
        return self._player[player].roll()
