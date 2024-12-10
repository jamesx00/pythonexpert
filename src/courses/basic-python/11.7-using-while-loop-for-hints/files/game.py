import random

number = random.randint(1, 100)

while True:
    guess = int(input("Guess the number between 1 and 100: "))

    if guess == number:
        print(f"You guessed right! The correct number is {number}")
        break
    elif guess < number:
        print("Too low. Try again.")
    elif guess > number:
        print("Too high. Try again.")