import unittest

from GreedGame import *


class MyTestCase(unittest.TestCase):
    def test_number_of_players_must_be_at_least_two(self):

        greed_game = GreedGame()

        result = None
        try:
            greed_game.number_of_players = 1
        except Exception as ex:
            result = ex.args[0]

        self.assertEqual('There must be at least two players', result)

    def test_start_game(self):

        greed_game = GreedGame()

        self.assertEqual([], greed_game._player)

        number_of_players = 2
        greed_game.start_game(number_of_players)

        self.assertEqual(2, len(greed_game._player))

    def test_end_game(self):

        greed_game = GreedGame()
        greed_game.start_game()

        self.assertEqual(2, len(greed_game._player))

        greed_game.end_game()

        self.assertEqual([], greed_game._player)

    def test_score_of_players_begins_with_0_pints(self):

        greed_game = GreedGame()
        greed_game.start_game()
        score_p1 = greed_game.total_score(0)
        score_p2 = greed_game.total_score(1)

        self.assertEqual(0, score_p1)
        self.assertEqual(0, score_p2)

        greed_game.number_of_players = 3
        score_p3 = greed_game.total_score(2)

        self.assertEqual(0, score_p1)
        self.assertEqual(0, score_p2)
        self.assertEqual(0, score_p3)

    def test_player_score_and_ends_turn_with_less_than_300_points_accumulated(self):

        greed_game = GreedGame()
        greed_game.start_game()

        p1_score = greed_game.score(0, [1, 2, 3, 4, 5])
        greed_game.end_turn(0)
        p1_total_score = greed_game.total_score(0)

        self.assertEqual(150, p1_score)
        self.assertEqual(0, p1_total_score)

    def test_player_1_score_and_ends_turn_with_more_than_300_points_accumulated(self):

        greed_game = GreedGame()
        greed_game.start_game()
        greed_game._player[0]._total_score = 1000

        p1_score = greed_game.score(0, [1, 2, 3, 4, 5])
        greed_game.end_turn(0)
        p1_total_score = greed_game.total_score(0)

        self.assertEqual(150, p1_score)
        self.assertEqual(1150, p1_total_score)

    def test_number_of_dice_for_rolling(self):

        greed_game = GreedGame()
        greed_game.start_game()

        self.assertEqual(len(greed_game.roll(0)), 5)

        greed_game._player[0]._last_roll = [1, 2, 3, 4, 5]

        self.assertEqual(len(greed_game.roll(0)), 3)

        greed_game._player[0]._last_roll = [1, 1, 3, 4, 5]

        self.assertEqual(len(greed_game.roll(0)), 2)

        greed_game._player[0]._last_roll = [1, 1, 1, 4, 5]

        self.assertEqual(len(greed_game.roll(0)), 1)

        greed_game._player[0]._last_roll = [2, 2, 2, 4, 4]

        self.assertEqual(len(greed_game.roll(0)), 2)

        greed_game._player[0]._last_roll = [2, 2, 3, 3, 4]

        self.assertEqual(len(greed_game.roll(0)), 5)

        greed_game._player[0]._last_roll = [1, 1, 1, 5, 5]

        self.assertEqual(len(greed_game.roll(0)), 5)

    def test_player1_scores_rolls_again_scoring_and_end_turn(self):

        greed_game = GreedGame()
        greed_game.start_game()

        greed_game.score(0, [1, 1, 1, 4, 3])
        p1_total_score = greed_game.total_score(0)

        self.assertEqual(p1_total_score, 0)

        greed_game.score(0, [5, 3])
        greed_game.end_turn(0)
        p1_total_score = greed_game.total_score(0)

        self.assertEqual(p1_total_score, 1050)

    def test_turn_ends_when_scoring_equals_zero_and_score_is_lost(self):

        greed_game = GreedGame()
        greed_game.start_game()

        roll = greed_game.roll(0)
        greed_game.score(0, [1, 1, 1, 4, 3])
        p1_total_score = greed_game.total_score(0)

        self.assertEqual(greed_game._player[0]._last_roll, roll)
        self.assertEqual(p1_total_score, 0)

        greed_game.score(0, [3, 4])

        self.assertEqual(greed_game._player[0]._last_roll, None)
        self.assertEqual(p1_total_score, 0)

    def test_first_turn_for_player1_then_turn_for_player2_then_player1(self):

        greed_game = GreedGame()
        greed_game.start_game()

        self.assertEqual('It is turn for player 1', greed_game.whos_turn)

        turn = greed_game.end_turn(0)

        self.assertEqual('It is turn for player 2', turn)

        turn = greed_game.end_turn(1)

        self.assertEqual('It is turn for player 1', turn)

    def test_game_returs_correct_points_after_both_players_score(self):

        greed_game = GreedGame()
        greed_game.start_game()

        greed_game.score(0, [1, 1, 1, 2, 2])
        greed_game.end_turn(0)

        greed_game.score(1, [1, 1, 5, 2, 2])
        greed_game.score(1, [1, 1, 5, 2, 2])
        greed_game.end_turn(1)

        self.assertEqual(1000, greed_game.total_score(0))
        self.assertEqual(500, greed_game.total_score(1))


    def test_last_round_starts_when_player_scores_3000_points(self):

        greed_game = GreedGame()
        greed_game.start_game()

        self.assertFalse(greed_game.is_last_round)

        greed_game.score(0, [1, 1, 1, 2, 2])
        greed_game.score(0, [1, 1, 1, 2, 2])
        greed_game.score(0, [1, 1, 1, 2, 2])
        greed_game.end_turn(0)

        self.assertTrue(greed_game.is_last_round)

    def test_game_ends_after_last_round_for_all_players(self):

        greed_game = GreedGame()
        greed_game.start_game()

        greed_game.score(0, [1, 1, 1, 2, 2])
        greed_game.score(0, [1, 1, 1, 2, 2])
        greed_game.score(0, [1, 1, 1, 2, 2])
        greed_game.end_turn(0)

        greed_game.end_turn(1)

        self.assertEqual([], greed_game._player)

    def test_player_with_greater_score_after_final_round_wins(self):

        greed_game = GreedGame()
        greed_game.start_game()

        greed_game.score(0, [1, 1, 1, 2, 2])
        greed_game.score(0, [1, 1, 1, 2, 2])
        greed_game.score(0, [1, 1, 1, 2, 2])
        greed_game.end_turn(0)

        end_game = greed_game.end_turn(1)

        self.assertEqual('Player 1 wins!!!\nFinal score:\n Player 1 = 3000 points\n Player 2 = 0 points\n', end_game)

        greed_game.start_game()

        greed_game.score(0, [1, 1, 1, 2, 2])
        greed_game.end_turn(0)

        greed_game.score(1, [1, 1, 1, 2, 2])
        greed_game.end_turn(1)

        greed_game.end_turn(0)

        greed_game.score(1, [1, 1, 1, 2, 2])
        greed_game.score(1, [1, 1, 1, 2, 2])
        greed_game.score(1, [5, 3, 4, 2, 2])
        greed_game.end_turn(1)

        end_game = greed_game.end_turn(0)

        self.assertEqual('Player 2 wins!!!\nFinal score:\n Player 1 = 1000 points\n Player 2 = 3050 points\n', end_game)

    def test_can_not_start_game_with_already_started_game(self):
        greed_game = GreedGame()
        greed_game.start_game()

        result = None
        try:
            greed_game.start_game()
        except Exception as ex:
            result = ex.args[0]

        self.assertEqual("Finish the current game to start a new one!", result)

    def test_can_not_finish_turn_when_is_not_players_turn(self):
        greed_game = GreedGame()
        greed_game.start_game()

        greed_game.end_turn(0)
        result = None
        try:
            greed_game.end_turn(0)
        except Exception as ex:
            result = ex.args[0]

        self.assertEqual("It is not your turn!", result)

    def test_can_not_score_when_is_not_players_turn(self):
        greed_game = GreedGame()
        greed_game.start_game()

        result = None
        try:
            greed_game.score(1, [1, 1, 1, 2, 2])
        except Exception as ex:
            result = ex.args[0]

        self.assertEqual("It is not your turn!", result)

    def test_can_not_roll_when_is_not_players_turn(self):
        greed_game = GreedGame()
        greed_game.start_game()

        result = None
        try:
            greed_game.roll(1)
        except Exception as ex:
            result = ex.args[0]

        self.assertEqual("It is not your turn!", result)

if __name__ == '__main__':
    unittest.main()
