---
lesson_name: Using While Loop for Hints
code_editor: True
code_execution: False
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: game.py
        file_type: python
        id: 50
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

## Use a while loop to give hints

We will use the `randint()` and `input()` functions along with a `while loop` to randomly generate a number that the player must guess, along with giving hints if the guessed number is incorrect. The game will end when the correct number is guessed.

Write the code according to the example below and run the program.

<div class="alert-info text-sm">
We recommend writing the code yourself instead of copying everything to create a sense of confidence in coding.
</div>

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

Let's take a look at the operation of each set of code that we have written.

```python
import random
```

The code in the first line is importing a module named "random", which is a module that has functions for generating random numbers and performing other random operations.

```python
number = random.randint(1, 100)
```

This code generates a random integer between 1 and 100 using the `randint()` function from the random module.

```python
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

At the top of this code block is the `while` keyword which causes the code inside the block to repeat until the specified condition is `False`. In this case, we set the condition to `True`, which causes the program to continue running indefinitely until it encounters the `break` keyword. In each loop, the program executes the following code:

```python
guess = int(input("Guess the number between 1 and 100: "))
```

This code snippet is asking the user to input a number using the `input()` function and then convert the input to an integer using the int function. This is done so that the input value can be compared using the `<` or `>` operators with the correct answer.

```python
if guess == number:
    print(f"You guessed right! The correct number is {number}")
    break
elif guess < number:
    print("Too low. Try again.")
elif guess > number:
    print("Too high. Try again.")
```

This `if else` code checks the value entered by the user with the initial answer number set. It checks according to the following conditions:

- If the guessed number is equal to the correct answer, display a message with break out of the while loop.
- If the guessed number is less than the correct answer, display a message to let the player guess again.
- If the guessed number is greater than the correct answer, display a message to let the player guess again.

### Make changes to your code

Try to understand the code and we recommend trying to make some changes to better understand how it works. For example, change from importing the module directly to only importing the functions we need, or try swapping the conditions in the `if else`.

```python
# Example
import random
number = random.randint(1, 100)

# Change to
from random import randint
number = randint(1, 100)
```

When you reach this point, the code in our **game.py** file should look like the code below or in the editor.

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
