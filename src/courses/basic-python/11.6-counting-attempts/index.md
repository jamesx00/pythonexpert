---
lesson_name: Counting Attempts
code_editor: True
code_execution: False
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: game.py
        file_type: python
        id: 54
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

## Counting Attempts

From the last chapter, our code is currently looking like this:

```python
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
```

We want to know how many attempts the player guessed before guessing the correct number. To do that, we will declare a new variable named `attempts` and set the value to `0` before the while loop. And within the while loop, we will increment the value of `attempts` by `1` every time the player guesses:

```python
import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number between 1 and 100: "))

    attempts += 1

    if guess == number:
        print(f"You guessed right! The correct number is {number}")
        break
    elif guess < number:
        print("Too low. Try again.")
    elif guess > number:
        print("Too high. Try again.")
```

We will also change the message when the player guesses the correct number to show how many guesses the player took. Instead of:

```python
if guess == number:
    print(f"You guessed right! The correct number is {number}")
    break
```

We will print the below message instead:

```python
if guess == number:
    print(f"Congratulations! You guessed the number in {attempts} attempts.")
    break
```

Now the code in **game.py** should look like the code below. You can try and play the game by running the command `python game.py` or `python3 game.py` and see the number of attempts you just implemented:

```python
import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Guess the number between 1 and 100: "))

    attempts += 1

    if guess == number:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break
    elif guess < number:
        print("Too low. Try again.")
    elif guess > number:
        print("Too high. Try again.")
```
