import random
from art import logo
print(logo)

easy_attempts = 10
hard_attempts = 5

def check_answer(user_guess, actual_answer, attempt):
    if user_guess > actual_answer:
        print("To High")
        return attempt - 1
    elif user_guess < actual_answer:
        print("To Low")
        return attempt - 1
    else:
        print(f"You Guessed it right! The answer was {actual_answer}")


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return easy_attempts
    else:
        return hard_attempts




def game():
    print("Welcome to Number Guessing Game! ")
    number = list(range(1, 101))
    print("I'm think of a number between 1 and 100")
    chosen_number = int(random.choice(number))

    attempt = set_difficulty()

    user = 0
    while user != chosen_number:
        print(f"you have {attempt} attempts remaining to guess the number")
        user = int(input("Make a guess: "))
        attempt = check_answer(user, chosen_number, attempt)
        if attempt == 0:
            print("You've run out of guesses, you lose.")
            return
        elif user != chosen_number:
            print("Guess again.")

game()