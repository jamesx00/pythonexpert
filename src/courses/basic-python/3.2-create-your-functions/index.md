---
lesson_name: Create Your Functions
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 219
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 218
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
    id: 1
    name: Python
---

### What are Functions

In programming, writing reusable code is an essential part that helps us work more efficiently. It reduces the time to perform a task, breaks down complex tasks into smaller parts, and reduces the chances of bugs in the program. Writing a function is a way of creating a set of commands that can be called repeatedly without having to rewrite the code every time.

In Python, the functions that come with the program are called **built-in functions**. We have already used some of them in previous lessons, such as type, which is used to find the data `type()`, or `print()`, which is used to display the result.

### Creating a New Function

The syntax for creating a function in Python is to use the `def` keyword followed by the name of the function you want to create and the `():` sign. Then, the code block inside the function will be the code for that gets executed when the function is called. Notice the leading space before the inner code block inside the function. We will explain this in the next lesson.

```python
def function_name():
    # code block for the function
```

Here's an example of creating a function:

```python
def print_hello_world():
    print("Hello World!")

print_hello_world()
print_hello_world()
```

```bash
Output:
Hello World!
Hello World!
```

In this example, we have created a function called `print_hello_world` that will print the string `"Hello World!"` when called. We then call the function twice, and each time it prints the same string.

---

### Exercise

Create your own function and call the function

#### Tests

<ul>
<li id="test-1">Create a new function named <code>say_hi</code></li>
<li id="test-2"><code>say_hi()</code> should print out the word <code>"Hello World!"</code> once when called.</li>
<li id="test-3">Call the function once.</li>
</ul>
