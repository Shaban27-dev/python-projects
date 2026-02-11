#          DAY_3
# Number Guessing Game (computer picks random number, user guesses).
import random

def num_guessing(attempt, max_num):
    computer_choice = random.randint(0, max_num)
    
    while attempt > 0:
        try:
            user_choice = int(input(f"Make a guess between 0 and {max_num}: "))
        except ValueError:
            print(f"Please make a guess between 0 and {max_num}")
            continue

        if user_choice < computer_choice:
            print("Your guess is too low!")
            print(f"Hint: Make guess between {user_choice + 1} and {max_num}")
        elif user_choice > computer_choice:
            print("Your guess is too high!")
            print(f"Hint: Make a guess between 0 and {user_choice - 1}")
        else:
            attempt -= 1
            print("Your guess is correct!")
            score = attempt * 10
            print(f"you guessed it in {attempt} attempts!")
            return score
            break

        if abs(user_choice - computer_choice) <= 3:
            print("You are very close!")
        elif abs(user_choice - computer_choice) <= 5:
            print("You are close!")

        attempt -= 1
        print(f"Attempts left: {attempt}")

        if attempt == 0:
            print(f"You ran out of attempts. Computer guess was {computer_choice}")
            return 0
        
best_score = 0
worst_score = 0

while True:
    difficulty_level = input("How much difficulty do you want to go with? (Easy, Medium or Hard): ").lower()
    if difficulty_level == "easy":
        attempt = 10
        max_num = 50
    elif difficulty_level == "medium":
        attempt = 5
        max_num = 75
    else:
        attempt = 3
        max_num = 100

    score = num_guessing(attempt, max_num)
    if score is not None:
        if score > best_score:
            best_score = score
            print("New high score!")
        elif score < best_score:
            worst_score = score
            print("Worst score")
    
    print(f"Best score so far {best_score}\n")
    print(f"Worst score so far {worst_score}\n")   
 
    play_again = input("Do you want to play again? (YES/NO): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break