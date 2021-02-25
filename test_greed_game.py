import unittest

from GreedGame import *

class MyTestCase(unittest.TestCase):
    def test_number_of_players_must_be_at_least_two(self):
        # with self.assertRaises(AttributeError): GreedGame(1)

        greed_game = GreedGame()

        result = None
        try:
            greed_game.number_of_players = 1
        except Exception as ex:
            result = ex.args[0]

        self.assertEqual('There must be at least two players', result)

    def test_score_of_players_begins_with_0_pints(self):

        greed_game = GreedGame()
        score_p1 = greed_game.total_score(0)
        score_p2 = greed_game.total_score(1)

        self.assertEqual(0, score_p1)
        self.assertEqual(0, score_p2)

        greed_game.number_of_players = 3
        score_p3 = greed_game.total_score(2)

        self.assertEqual(0, score_p1)
        self.assertEqual(0, score_p2)
        self.assertEqual(0, score_p3)

    def test_player_1_score_and_ends_turn_with_less_than_300_points_accumulated(self):

        greed_game = GreedGame()

        p1_score = greed_game.score(0, [1, 2, 3, 4, 5])
        greed_game.end_turn(0)
        p1_total_score = greed_game.total_score(0)

        self.assertEqual(150, p1_score)
        self.assertEqual(0, p1_total_score)

        p1_score = greed_game.score(0, [1, 1, 3, 4, 1])
        greed_game.end_turn(0)
        p1_total_score = greed_game.total_score(0)

        self.assertEqual(1000, p1_score)
        self.assertEqual(1000, p1_total_score)

    def test_player_1_score_and_ends_turn_with_more_than_300_points_accumulated(self):

        greed_game = GreedGame()
        greed_game._player[0]._total_score = 1000

        p1_score = greed_game.score(0, [1, 2, 3, 4, 5])
        greed_game.end_turn(0)
        p1_total_score = greed_game.total_score(0)

        self.assertEqual(150, p1_score)
        self.assertEqual(1150, p1_total_score)

    def test_number_of_dice_for_rolling(self):

        greed_game = GreedGame()

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

    def test_player1_scores_rolls_again_scoring_and_end_turn(self):

        greed_game = GreedGame()

        au = greed_game.score(0, [1, 1, 1, 4, 3])
        p1_total_score = greed_game.total_score(0)

        self.assertEqual(p1_total_score, 0)

        au = greed_game.score(0, [5, 3])
        greed_game.end_turn(0)
        p1_total_score = greed_game.total_score(0)

        self.assertEqual(p1_total_score, 1050)

    def test_turn_ends_when_scoring_equals_zero_and_score_is_lost(self):

        greed_game = GreedGame()

        roll = greed_game.roll(0)
        greed_game.score(0, [1, 1, 1, 4, 3])
        p1_total_score = greed_game.total_score(0)

        self.assertEqual(p1_total_score, 0)
        self.assertEqual(greed_game._player[0]._last_roll, roll)

        greed_game.score(0, [3, 4])

        self.assertEqual(greed_game._player[0]._last_roll, None)
        self.assertEqual(p1_total_score, 0)


if __name__ == '__main__':
    unittest.main()
