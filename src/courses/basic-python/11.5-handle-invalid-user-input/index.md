---
lesson_name: Handle Invalid User Input
code_editor: True
code_execution: False
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: game.py
        file_type: python
        id: 56
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

## Handle Invalid User Input

In the previous lesson, we learned about the `try-except` block, a powerful construct in Python for handling errors and exceptions that might occur during the execution of a program.

Our current code will break when the user gives non-numeric input because the `int()` function will raise a `ValueError` exception if the input is not a valid integer. When the exception is raised, the program will stop with an error message, and the user will not be able to continue with the guessing game.

Here's an example of what happens when the user enters non-numeric input:

```bash
❯ python game.py
Guess the number between 1 and 100: abc
Traceback (most recent call last):
  File "game.py", line 7, in <module>
    guess = int(input("Guess the number between 1 and 100: "))
ValueError: invalid literal for int() with base 10: 'abc'
```

To handle this error, we can use a try-except block to catch the `ValueError` exception and handle it gracefully by informing the user that they need to enter a valid integer.

We will add a `try-catch` block to our code before incrementing the variable `attempts` as below:

```python
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
```

In this updated version of the code, we've added a `try-except` block around the data type conversion statement. If the user enters a non-numeric value, such as a letter, the `int()` function will raise a `ValueError`. The `except` block will then catch the error and print a message telling the user that their input was invalid. The continue statement will then return the program to the start of the loop, so the user can try again.

```bash
> python game.py
Guess the number between 1 and 100: abc
Invalid input! Please enter a number.
Guess the number between 1 and 100:
```

<div class="alert-warning text-sm">
It is important to place the try-except block before the attempts incrementing statement because if the user enters a non-numeric input, the attempts counter should not be incremented. If we put the attempts incrementing statement before the try-except block, it would be executed regardless of whether the input was valid or not. As a result, the attempts counter would be incremented even if the user entered an invalid input. By placing the try-except block before the attempts incrementing statement, we ensure that the attempts counter is only incremented when the user enters a valid input.
</div>
