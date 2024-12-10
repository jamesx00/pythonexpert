---
lesson_name: Combine If Statement with Else
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: tests.py
        file_type: python
        id: 236
        is_closable: false
        is_edit_focus: false
        is_editable: false
        is_hidden: true
        is_main: false
        is_test_file: true
        source: tests.py
      - file_name: main.py
        file_type: python
        id: 235
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

### Combine if statement with else

In Python, `else` is a keyword that is used with an if statement to specify a block of code to be executed when the condition of the if statement evaluates to `False`.

Here's how to write your code using `else` with if statement:

```python
if condition:
    # block of code to be executed if the condition is True
else:
    # block of code to be executed if the condition is False
```

For example:

```python
age = 18

if age >= 18:
    print("You are an adult.")
else:
    print("You are not an adult.")
```

In this example, we check if the `age` variable is greater than or equal to 18. If it is, we print `"You are an adult."` If it's not, we print `"You are not an adult."`.

---

### Exercise

Change the code within the function `is_longer_than_5_characters` to use the `else` keyword:

- If `text` is longer than 5 characters, it prints out only `"That is longer than 5 characters."`.
- If `text` is not longer than 5 characters, it prints out only `"That is not longer than 5 characters."`.

#### Tests

<ul>
<li id="test-1"><code>is_longer_than_5_characters("1234")</code> should print the message <code>"That is not longer than 5 characters."</code></li>
<li id="test-2"><code>is_longer_than_5_characters("12345")</code> should print the message <code>"That is not longer than 5 characters."</code></li>
<li id="test-3"><code>is_longer_than_5_characters("123456")</code> should print the message <code>"That is longer than 5 characters."</code></li>
</ul>
