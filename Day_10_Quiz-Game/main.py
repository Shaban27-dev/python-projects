#          DAY-10
# Quiz Game (ask 5 questions, show score).
print('''________        .__           ________                     ._.
\_____  \  __ __|__|_______  /  _____/_____    _____   ____| |
 /  / \  \|  |  \  \___   / /   \  ___\__  \  /     \_/ __ \ |
/   \_/.  \  |  /  |/    /  \    \_\  \/ __ \|  Y Y  \  ___/\|
\_____\ \_/____/|__/_____ \  \______  (____  /__|_|  /\___  >_
       \__>              \/         \/     \/      \/     \/\/''')

questions = {
    "Q1) What is the meaning of D in 'BODMAS'? ": "divide",
    "Q2) Which planet is no longer a part of our solar system? ": "pluto",
    "Q3) Who made a sacrifice of his life on 'Avengers: Endgame' movie? ": "ironman",
    "Q4) Which is the largest continent in the world? ": "asia",
    "Q5) How many countries are there in the world? ": "195",
}

score = 0

for question, correct_answer in questions.items():
    user_answer = input(question).strip().lower()

    if user_answer == correct_answer.lower():
        score += 1
        print("Correct! ✅")
    else:
        print(f"Wrong! ❌ The correct answer was {correct_answer}.")

print(f"\nYou got {score} out of {len(questions)} correct!")
print(f"Your total score is: {score}/{len(questions)} 🎉")
percentage = (score / len(questions)) * 100
print(f"You got {percentage:.2f}% correct answers out of 100%.")