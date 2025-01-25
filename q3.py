import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:  
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too Low!")
        elif user_guess > number_to_guess:
            print("Too High!")
        else:
            print(f"Congratulations! You've guessed the number in {attempts} attempts.")
            break

if __name__ == "__main__":
    number_guessing_game()