---
lesson_name: Missing Colon
code_editor: True
code_execution: True
adding_file_allowed: False
file_groups:
  - common: false
    files:
      - file_name: main.py
        file_type: python
        id: 326
        is_closable: false
        is_edit_focus: true
        is_editable: true
        is_hidden: false
        is_main: true
        is_test_file: false
        source: main.py
      - file_name: tests.py
        file_type: python
        id: 327
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

### Missing colon

The colon `:` is an essential part of the syntax for defining code blocks, such as in `if` statements, `for` loops, function definitions (`def`), and more. Forgetting to include a colon after such statements can lead to a common syntax error. Let's explore how to recognize and resolve missing colon errors.

When you forget to include a colon after a statement that requires one, Python raises an error `SyntaxError` with the message `expected ':'`. With older versions, Python raises the error with the message `invalid syntax` instead.

To identify a missing colon error, carefully review the line of code where the error occurs. Look for statements like `if`, `for`, `while`, `def`, and `class` that are followed by a code block, which requires a colon.

Here's an example of incorrect code:

```python
if x > 10 # Missing colon
    print("x is greater than 10")
```

And this is the output with the error message you would see:

```python
File "main.py", line 1
    if x > 10 # Missing colon
              ^^^^^^^^^^^^^^^
SyntaxError: expected ':'
```

---

### Exercise

- Add colons in the code so that the program runs without errors.

#### Tests

<ul>
<li id="test-1"><code>can_you_vote(18)</code> should print the message <code>"You are eligible to vote."</code></li>
<li id="test-2"><code>can_you_vote(15)</code> should print the message <code>"You are not eligible to vote."</code></li>
</ul>
