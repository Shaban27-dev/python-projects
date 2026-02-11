#          DAY-18
#Mini Game Framework
# Base Game class
# Child classes for different games
import random


# ---------------- Base Framework ----------------
class Game:
    def __init__(self):
        self.score = 0

    def start_menu(self):
        print("\n---- Welcome to Mini Games ----")
        print("1. Guess the Number")
        print("2. Quiz Game")
        print("3. Rock Paper Scissors")
        print("4. Exit")

    def end_game(self):
        print("\nGame Over!")
        print(f"Your score: {self.score}")

    def play_game(self):
        raise NotImplementedError("Child class must implement play_game()")


# ---------------- Game 1: Guess the Number ----------------
class GuessTheNumber(Game):
    def __init__(self):
        super().__init__()

    def play_game(self):
        print("\nStarting Guess the Number Game!")
        computer_choice = random.randint(0, 20)

        while True:
            try:
                guess = int(input("Make a guess between 0 and 20: "))
            except ValueError:
                print("Please enter a valid number between 0 and 20.")
                continue

            if guess < 0 or guess > 20:
                print("Out of range! Please choose between 0 and 20.")
                continue

            if guess < computer_choice:
                print("Too low!")
            elif guess > computer_choice:
                print("Too high!")
            else:
                print("Correct! 🎉")
                self.score += 1
                break

        self.end_game()


# ---------------- QuizBrain Helper Class ----------------
class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        q = self.question_list[self.question_no]
        print(f"\nQ{self.question_no + 1}: {q['question']}")

        for key, value in q["options"].items():
            print(f"   {key}. {value}")

        while True:
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()
            if user_answer in q["options"]:
                break
            print("Invalid choice. Please enter A, B, C, or D.")

        if user_answer == q["answer"]:
            print("Correct! ✅")
            self.score += 1
        else:
            print("Wrong! ❌")

        print(f"Correct answer: {q['answer']}")
        print(f"Score: {self.score}/{self.question_no + 1}")

        self.question_no += 1


# ---------------- Game 2: Quiz Game ----------------
class QuizGame(Game):
    def __init__(self):
        super().__init__()

    def play_game(self):
        print("\nStarting Quiz Game!")

        questions = [
            {
                "question": "Which planet is known as the Red Planet?",
                "options": {"A": "Earth", "B": "Mars", "C": "Jupiter", "D": "Venus"},
                "answer": "B"
            },
            {
                "question": "What is the capital of France?",
                "options": {"A": "Berlin", "B": "Madrid", "C": "Paris", "D": "Rome"},
                "answer": "C"
            },
            {
                "question": "Which data type is immutable in Python?",
                "options": {"A": "List", "B": "Dictionary", "C": "Tuple", "D": "Set"},
                "answer": "C"
            },
            {
                "question": "Who wrote 'Hamlet'?",
                "options": {"A": "Charles Dickens", "B": "William Shakespeare", "C": "Leo Tolstoy", "D": "Mark Twain"},
                "answer": "B"
            },
            {
                "question": "Which gas do humans need to survive?",
                "options": {"A": "Carbon Dioxide", "B": "Oxygen", "C": "Nitrogen", "D": "Hydrogen"},
                "answer": "B"
            },
            {
                "question": "What is the largest mammal on Earth?",
                "options": {"A": "Elephant", "B": "Blue Whale", "C": "Giraffe", "D": "Hippopotamus"},
                "answer": "B"
            },
            {
                "question": "Which keyword is used to define a function in Python?",
                "options": {"A": "func", "B": "def", "C": "function", "D": "lambda"},
                "answer": "B"
            },
            {
                "question": "Which continent is the Sahara Desert located in?",
                "options": {"A": "Asia", "B": "Africa", "C": "Australia", "D": "South America"},
                "answer": "B"
            },
            {
                "question": "What is the chemical symbol for water?",
                "options": {"A": "O2", "B": "H2O", "C": "CO2", "D": "HO"},
                "answer": "B"
            },
            {
                "question": "Which year did World War II end?",
                "options": {"A": "1940", "B": "1945", "C": "1950", "D": "1939"},
                "answer": "B"
            }
        ]

        new_questions = random.sample(questions, 5)
        quiz = QuizBrain(q_list=new_questions)

        while quiz.still_has_question():
            quiz.next_question()

        percentage = (quiz.score / len(new_questions)) * 100
        print("\nQuiz Completed!")
        print(f"Final Score: {quiz.score}/{len(new_questions)}")
        print(f"Percentage: {percentage:.2f}%")

        self.score += quiz.score
        self.end_game()


# ---------------- Game 3: Rock Paper Scissors ----------------
class RockPaperScissors(Game):
    def __init__(self):
        super().__init__()

    def play_game(self):
        print("\nStarting Rock Paper and Scissors Game!")

        choices = ["rock", "paper", "scissors"]
        user_score = {"wins": 0, "lose": 0, "draws": 0}
        round_no = 1

        while True:
            print(f"\n_____ Round {round_no} _____")
            user_choice = input("Pick one (rock/paper/scissors): ").lower().strip()

            if user_choice not in choices:
                print("Invalid input. Please type rock, paper, or scissors.")
                continue

            computer_choice = random.choice(choices)
            print(f"Computer choice: {computer_choice}")

            if user_choice == computer_choice:
                print("It's a draw!")
                user_score["draws"] += 1

            elif (user_choice == "rock" and computer_choice == "scissors") or \
                 (user_choice == "paper" and computer_choice == "rock") or \
                 (user_choice == "scissors" and computer_choice == "paper"):
                print("You Win! ✅")
                user_score["wins"] += 1
                self.score += 1
            else:
                print("You lose! ❌")
                user_score["lose"] += 1

            print(f"Scoreboard: wins={user_score['wins']} | loses={user_score['lose']} | draws={user_score['draws']}")
            round_no += 1

            if user_score["wins"] == 5:
                print("You are the champion! 🏆")
                break
            elif user_score["lose"] == 5:
                print("Computer is the champion! 😢")
                break

        self.end_game()


# ---------------- Launcher ----------------
launcher = Game()

while True:
    launcher.start_menu()
    choice = input("Choose a game (1-4): ").strip()

    if choice == "1":
        GuessTheNumber().play_game()
    elif choice == "2":
        QuizGame().play_game()
    elif choice == "3":
        RockPaperScissors().play_game()
    elif choice == "4":
        print("Thanks for playing. Goodbye! 👋")
        break
    else:
        print("Invalid choice. Please try again.")