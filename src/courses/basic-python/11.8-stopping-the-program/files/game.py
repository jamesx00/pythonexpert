import random


def game():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input('Guess the number between 1 and 100 or "s" to stop the round: ')

        if guess.lower() == "s":
            break

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        attempts += 1

        if guess == number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")


while True:
    game()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thanks for playing!")
        break