#          DAY-14
# MCQ Quiz App
# Questions stored in a list/dict
# Score tracking
# Replay option
import random
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
random.shuffle(questions)

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
            else:
                print("Invalid choice. please enter A, B, C and D.")

        if user_answer == q["answer"]:
            print("Correct! ✅")
            self.score += 1
        else:
            print("Wrong! ❌")

        print(f"Correct answer: {q['answer']}")
        print(f"Score: {self.score}/{self.question_no + 1}")
        
        self.question_no += 1
    
    def reset(self):
        self.question_no = 0
        self.score = 0
            

quiz = QuizBrain(q_list=questions)

while True:
    while quiz.still_has_question():
        quiz.next_question()

    percentage = (quiz.score / len(quiz.question_list)) * 100
    print("\nQuiz Completed!")
    print(f"Final Score: {quiz.score}/{len(questions)}")
    print(f"Percentage: {percentage:.2f}%")

    play_again = input("Do you want to play again? (Y/N): ").lower()
    if play_again == "y":
        random.shuffle(questions)
        quiz.reset()
    else:
        print("Thanks for playing! 👋")
        break