
import unittest
from game_logic import GameLogic

class TestGameLogic(unittest.TestCase):
    def setUp(self):
        self.game = GameLogic()

    def test_calculate(self):
        self.assertEqual(self.game.calculate(2, 3, '+'), 5)
        self.assertEqual(self.game.calculate(5, 2, '-'), 3)
        self.assertEqual(self.game.calculate(3, 3, '*'), 9)
        self.assertEqual(self.game.calculate(9, 3, '/'), 3)

    def test_check_goal(self):
        self.game.goal = 10
        self.assertEqual(self.game.check_goal(10), 3)
        self.assertEqual(self.game.check_goal(8), 2)
        self.assertEqual(self.game.check_goal(5), 1)
        self.assertEqual(self.game.check_goal(0), 0)

    def test_validate_input(self):
        self.game.numbers = [1, 2, 3, 4, 5, 6]
        self.game.operations = {'+': None, '-': None, '*': None, '/': None}
        self.assertTrue(self.game.validate_input(1, 2, '+'))
        self.assertFalse(self.game.validate_input(10, 2, '+'))
        self.assertFalse(self.game.validate_input(1, 2, '^'))

    def test_play_round(self):
        self.game.numbers = [1, 2, 3, 4, 5, 6]
        self.game.goal = 10
        self.assertEqual(self.game.play_round(1, 2, '+'), 0)
        self.assertEqual(self.game.play_round(5, 5, '+'), 3)
        self.assertEqual(self.game.play_round(10, 2, '+'), "Invalid input")

if __name__ == '__main__':
    unittest.main()

