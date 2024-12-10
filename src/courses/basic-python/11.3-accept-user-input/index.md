---
lesson_name: Accept User Input
code_editor: False
code_execution: True
adding_file_allowed: False
---

### Accept User Input

In Python, we can accept inputs from users using several methods. The easiest and most common method is to use the `input()` function that comes with the Python language.

For example:

```python
name = input("Enter your name: ")
print(f"Hello {name}!")
```

Try copying the above code into the **game.py** file created in the previous lesson, then run the program and enter your name when prompted.

![Get user input](https://asset.pythonexpert.dev/media/images/courses/python-for-beginners/get_user_input.gif)

<p class="caption">Example of providing an input</p>

```shell
$ python game.py
> Enter your name: James
> Hello James!
```

In addition to receiving input as a string, we can also receive input as a number. However, **the input received from the `input()` function will always be a string type**. Therefore, we need to convert the value from a string to a number using the `int()` or `float()` function.

For example, the code below has not yet converted the input value, so when running the code, the age variable will have the type of string:

```python
age = input("How old are you: ")
print(type(age)) # <class 'str'>
```

When we convert the value received using the `int()` function, the data type will change. For example, in the code below, when the system receives an input, the int function will convert the data type to an integer.

```python
age = int(input("How old are you: "))
print(type(age)) # <class 'int'>
```
