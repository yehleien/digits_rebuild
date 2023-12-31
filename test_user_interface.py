import unittest
from unittest.mock import patch, call
from io import StringIO
from user_interface import UserInterface
import itertools

class TestUserInterface(unittest.TestCase):
    def setUp(self):
        self.ui = UserInterface()

    @patch('builtins.print')
    def test_display_instructions(self, mock_print):
        self.ui.display_instructions()
        calls = [
            "Welcome to the Digits game!",
            "You are given six numbers that you can add, subtract, multiply, or divide together to reach a goal number.",
            "You can, for example, multiply two of the numbers together and then add that total to one of the others.",
            "You get three stars if you reach the exact goal number, but if you’re close, you’ll get one or two stars.",
            "Let's start the game!"
        ]
        mock_print.assert_has_calls([call(s) for s in calls])

    @patch('builtins.print')
    def test_display_numbers_and_goal(self, mock_print):
        self.ui.display_numbers_and_goal()
        calls = [
            call("Your numbers are: ", self.ui.game.numbers),
            call("Your goal is: ", self.ui.game.goal)
        ]
        mock_print.assert_has_calls(calls)

    @patch('builtins.input', side_effect=['5', '5', '+'])
    def test_get_user_input(self, mock_input):
        num1, num2, operation = self.ui.get_user_input()
        self.assertEqual(num1, 5)
        self.assertEqual(num2, 5)
        self.assertEqual(operation, '+')

    @patch('builtins.print')
    @patch('builtins.input', side_effect=['3', '4', '+'])
    def test_play_game(self, mock_input, mock_print):
        self.ui.play_game()
        calls = [
            call("Welcome to the Digits game!"),
            call("You are given six numbers that you can add, subtract, multiply, or divide together to reach a goal number."),
            call("You can, for example, multiply two of the numbers together and then add that total to one of the others."),
            call("You get three stars if you reach the exact goal number, but if you’re close, you’ll get one or two stars."),
            call("Let's start the game!"),
            call("Your numbers are: ", self.ui.game.numbers),
            call("Your goal is: ", self.ui.game.goal),
            call("Your score for this round is: ", self.ui.score_system.get_total_score()),
            call("Your total score is: ", self.ui.score_system.get_total_score()),
            call("Your average score is: ", self.ui.score_system.get_average_score()),
            call("Thank you for playing the Digits game!")
        ]
        mock_print.assert_has_calls(calls)

if __name__ == "__main__":
    unittest.main()
