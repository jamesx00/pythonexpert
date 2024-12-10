---
lesson_name: Stopping the Program
code_editor: True
code_execution: False
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: game.py
        file_type: python
        id: 58
        is_closable: false
        is_edit_focus: true
        is_editable: false
        is_hidden: false
        is_main: true
        is_test_file: false
        source: game.py
    id: 1
    name: Python
---

## Stopping the Program

In our guess the number game, we ask the user to input their guess in each round. However, sometimes the player may want to stop the game while playing. At the moment, the player could stop the game by sending the interrupt signal to the program, which raises the `KeyboardInturrupt` exception. In most cases, this occurs when the user presses `Ctrl+C` on the keyboard, but the exact key or signal can vary depending on the platform and configuration.

### Stop the game with the KeyboardInterrupt exception

When a `KeyboardInterrupt` exception is raised, it interrupts the normal execution of the program and allows the user to stop the program's execution. This can be useful in situations where the program is stuck or taking too long to complete a task.

See below for an example of what happens when the player press `Ctrl+C` during the guess the number game execution.

![keyboard-interrupt-example](https://asset.pythonexpert.dev/media/images/courses/python-for-beginners/keyboard-interrupt-en.gif)

<p class="caption">Keyboard Interrupt Example</p>

```bash
Guess the number between 1 and 100: ^CTraceback (most recent call last):
  File "/Users/james/python/pythonexpert/01-guess-the-number/game.py", line 29, in <module>
    game()
  File "/Users/james/python/pythonexpert/01-guess-the-number/game.py", line 9, in game
    guess = input("Guess the number between 1 and 100: ")
KeyboardInterrupt
```

Knowing that, we can update the `game()` function and add another `try-except` block to catch the `KeyboardInterrupt` exception within the game logic, like so:

```python
def game():
    number = random.randint(1, 100)
    attempts = 0

    try:
        while True:
            guess = input("Guess the number between 1 and 100: ")

            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            attempts += 1

            if guess == number:
                print(
                    f"Congratulations! You guessed the number in {attempts} attempts."
                )
                break
            elif guess < number:
                print("Too low. Try again.")
            elif guess > number:
                print("Too high. Try again.")
    except KeyboardInterrupt:
        print("Game interrupted. Thanks for playing!")
```

When the exception is caught, the program will print a message informing the user that the game has been interrupted, and the round will end, prompting the user if they would like to play another round.

```shell
❯ python game.py
Guess the number between 1 and 100: 50
Too high. Try again.
Guess the number between 1 and 100: ^CGame interrupted. Thanks for playing!
Do you want to play again? (y/n): n
Thanks for playing!
```

### Stop the game with the player's input

While using a `KeyboardInterrupt` exception to stop the round is a working solution, some players may not know that pressing `Ctrl+C` will stop the game, and the shortcut may be different depending on their system as well.

Instead of using the previous method, we could instead accept an additional input to stop the round.

Update the `game()` function to ask the player to type "s" during the number guessing step to stop the round and add another `if` statement to break out of the `while` loop:

```python
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
```

Try and run the program again to see the result:

```shell
❯ python game.py
Guess the number between 1 and 100 or "s" to stop the round: 50
Too low. Try again.
Guess the number between 1 and 100 or "s" to stop the round: s
Do you want to play again? (y/n): n
Thanks for playing!
```

And this is the complete code for our number guessing game:

```python
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
```
