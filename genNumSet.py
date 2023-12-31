import random
import operator

def generate_numbers_and_goal():
    numbers = [random.randint(1, 99) for _ in range(6)]
    operations = [operator.add, operator.mul]
    goal = numbers[0]

    for num in numbers[1:]:
        operation = random.choice(operations)
        goal = operation(goal, num)

    while goal < 99 or goal > 1000:
        goal = numbers[0]
        for num in numbers[1:]:
            operation = random.choice(operations)
            goal = operation(goal, num)

    return numbers, goal
