---
lesson_name: Adding Multiple Rounds
code_editor: True
code_execution: False
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: game.py
        file_type: python
        id: 57
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

## Adding Multiple Rounds

At the moment, we can only play a single round of guess the number game when we run the command `python game.py`. We can now add multiple rounds functionality by using the `while loop` and use `functions` to make it easier to run multiple rounds of the game.

We will first start by wrapping the game logic inside a function called `game()`. We **do not** need to include the `import` statement inside the function definition. And call the function right after the function definition ends.

```python
import random

def game():
    number = random.randint(1, 100)
    attempts = 0


    while True:
        guess = input("Guess the number between 1 and 100: ")

        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if guess == "s":
            break

        attempts += 1

        if guess == number:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
        elif guess < number:
            print("Too low. Try again.")
        elif guess > number:
            print("Too high. Try again.")

game()
```

Now run the command `python game.py` to play the game. You will see that all the functionality remains the same.

```shell
$ python game.py
Guess the number between 1 and 100: 50
Too high. Try again.
Guess the number between 1 and 100: 25
Too high. Try again.
Guess the number between 1 and 100: 12
Too high. Try again.
Guess the number between 1 and 100: 11
Congratulations! You guessed the number in 4 attempts
```

Now that we can play the game by calling the function `game()`, we can use `while loop` to introduce multiple rounds. Instead of calling the function `game()` only once, wrap the function call inside another `while loop` like so:

```python
while True:
    game()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thanks for playing!")
        break
```

With the example above, when the file is run, the first round of the game will start. The player will be prompted with a question about whether to continue playing or stop the game. If the player answers with anything other than **Y** or **y**, the game will stop.

Now the code should look like this:

```python
import random

def game():
    number = random.randint(1, 100)
    attempts = 0

    while True:
        guess = input("Guess the number between 1 and 100: ")

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

Try starting the game again and see the difference.

<div class="alert-info text-sm">
We do not need to wrap the game logic inside the function game(), but doing so makes the code more organized and easier to maintain.
</div>
