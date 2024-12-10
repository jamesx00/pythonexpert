---
lesson_name: Accept a Variable Number of Arguments with Args
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 269
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 270
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
    id: 1
    name: Python
---

### Accept a variable number of arguments with args

In some cases, we may not know in advance how many arguments will be passed to a function. Python allows us to accept an unlimited number of arguments by creating a function and specifying a variable with an asterisk symbol `*`, such as:

```python
def say_hello(*args):
    for name in args:
        print(f"Hello {name}")

say_hello("Jacob", "Jordan", "Andrew")
```

```bash
Output:
Hello Jacob
Hello Jordan
Hello Andrew
```

When the function is called, all arguments are turned into a tuple that is assigned to the args variable, which we can loop through. If we define additional variables, the values specified in the function call will be assigned to those variables, and any remaining values will be collected into a tuple. For example:

```python
def say_hello(first_person, *args):
    print(f"The first person on the list is {first_person}")
    for name in args:
        print(f"Hello {name}")

say_hello("Jacob", "Jordan", "Andrew")
```

```bash
Output:
The first person on the list is Jacob
Hello Jordan
Hello Andrew
```

---

### Exercise

Create a function named `accept_all` that accepts any number of positional arguments.

#### Tests

<ul>
<li id="test-1">Create a function named <code>accept_all</code></li>
<li id="test-2">Function <code>accept_all</code> should accept any number of positional arguments</li>
</ul>
