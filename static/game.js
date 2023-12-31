class GameLogic {
    constructor(numbers, goal) {
        this.numbers = numbers;
        this.goal = goal;
    }

    calculate(num1, num2, operation) {
        switch(operation) {
            case '+':
                return num1 + num2;
            case '-':
                return num1 - num2;
            case '*':
                return num1 * num2;
            case '/':
                return num1 / num2;
        }
    }

    playRound(num1, num2, operation) {
        let index1 = this.numbers.indexOf(num1);
        let index2 = this.numbers.indexOf(num2);
        if (index1 !== -1 && index2 !== -1) {
            this.numbers.splice(index1, 1);
            this.numbers.splice(index2, 1);
            let result = this.calculate(num1, num2, operation);
            this.numbers.push(result);
            if (this.numbers.length === 1 && this.numbers[0] === this.goal) {
                return "You won!";
            } else {
                return result;
            }
        } else {
            return "Invalid input";
        }
    }

    checkGoal() {
        if (Math.abs(this.goal - this.numbers[0]) <= 10) {
            return "You get two stars for being close to the goal number!";
        } else if (this.goal === this.numbers[0]) {
            return "You get three stars for reaching the goal number!";
        } else {
            return "Keep going!";
        }
    }
}