import random
import operator
from genNumSet import generate_numbers_and_goal
from score_system import ScoreSystem

class GameLogic:
    def __init__(self, numbers, goal):
        self.numbers = numbers
        self.goal = goal

    def calculate(self, num1, num2, operation):
        if operation == '+':
            return num1 + num2
        elif operation == '-':
            return num1 - num2
        elif operation == '*':
            return num1 * num2
        elif operation == '/':
            return num1 / num2

    def play_round(self, num1, num2, operation):
        if num1 in self.numbers and num2 in self.numbers:
            self.numbers.remove(num1)
            self.numbers.remove(num2)
            result = self.calculate(num1, num2, operation)
            self.numbers.append(result)
            if len(self.numbers) == 1 and self.numbers[0] == self.goal:
                return "You won!"
            else:
                return result
        else:
            return "Invalid input"

    def check_goal(self):
        if abs(self.goal - self.numbers[0]) <= 10:
            return "You get two stars for being close to the goal number!"
        elif self.goal == self.numbers[0]:
            return "You get three stars for reaching the goal number!"
        else:
            return "Keep going!"

class UserInterface:
    ...

    def __init__(self):
        numbers, goal = generate_numbers_and_goal()
        self.game = GameLogic(numbers, goal)
        self.score_system = ScoreSystem()

    def play_game(self):
        self.display_instructions()
        self.display_numbers_and_goal()
        while len(self.game.numbers) > 1:
            num1, num2, operation = self.get_user_input()
            result = self.game.play_round(num1, num2, operation)
            if result != "Invalid input":
                print(result)
                self.display_numbers_and_goal()
        print("Thank you for playing the Digits game!")
        print(self.game.check_goal())
