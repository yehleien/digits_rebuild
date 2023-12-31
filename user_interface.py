from game_logic import GameLogic
from genNumSet import generate_numbers_and_goal
from score_system import ScoreSystem

class UserInterface:
    def __init__(self):
        numbers, goal = generate_numbers_and_goal()
        self.game = GameLogic(numbers, goal)
        self.score_system = ScoreSystem()

    def display_instructions(self):
        print("Welcome to the Digits game!")
        print("You are given six numbers that you can add, subtract, multiply, or divide together to reach a goal number.")
        print("You can, for example, multiply two of the numbers together and then add that total to one of the others.")
        print("You get three stars if you reach the exact goal number, but if you’re close, you’ll get one or two stars.")
        print("Let's start the game!")

    def display_numbers_and_goal(self):
        print("Your numbers are: ", self.game.numbers)
        print("Your goal is: ", self.game.goal)

    def get_user_input(self):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")
        return num1, num2, operation

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

if __name__ == "__main__":
    ui = UserInterface()
    ui.play_game()
